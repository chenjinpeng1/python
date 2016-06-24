from django.contrib.auth.decorators import login_required
from django.shortcuts import render,HttpResponse
from django.core.cache import cache
# Create your views here.
import os
from webchat import models
import queue,json,time,hashlib
from bbs import models as bbs_modeles
GLOBAL_MSG_QUEUES ={

}
@login_required
def dashboard(request):

    return render(request,'webchat/dashboard.html')


@login_required
def send_msg(request):
    msg_data = request.POST.get('data')
    print('recv html msg--------：',msg_data)
    if msg_data:
        msg_data = json.loads(msg_data)
        msg_data['timestamp'] = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        msg_data['img'] = str(request.user.userprofile.head_img).split("/")[1]
        if msg_data['type'] == 'single':
            if not GLOBAL_MSG_QUEUES.get(int(msg_data['to']) ):
                GLOBAL_MSG_QUEUES[int(msg_data["to"])] = queue.Queue()
            GLOBAL_MSG_QUEUES[int(msg_data["to"])].put(msg_data)
        else:#group
            group_obj = models.WebGroup.objects.get(id=msg_data['to'])
            for member in group_obj.members.select_related():
                if not GLOBAL_MSG_QUEUES.get(member.id): #如果字典里不存在这个用户的queue
                    GLOBAL_MSG_QUEUES[member.id] = queue.Queue()
                if member.id != request.user.userprofile.id:
                    GLOBAL_MSG_QUEUES[member.id].put(msg_data)

    print('--------------------',msg_data)
    #if not GLOBAL_MSG_QUEUES.get()
    return HttpResponse('---msg recevied---')

def get_new_msgs(request):
    if request.user.userprofile.id not in GLOBAL_MSG_QUEUES:
        print("no queue for user [%s]" %request.user.userprofile.id,request.user)
        GLOBAL_MSG_QUEUES[request.user.userprofile.id] = queue.Queue()
    msg_count = GLOBAL_MSG_QUEUES[request.user.userprofile.id].qsize()
    q_obj = GLOBAL_MSG_QUEUES[request.user.userprofile.id]
    msg_list = []
    if msg_count >0:

        for msg in range(msg_count):
            msg_list.append(q_obj.get())

        print("new msgs:",msg_list)
    else:#没消息,要挂起
        print("no new msg for ",request.user,request.user.userprofile.id)
        #print(GLOBAL_MSG_QUEUES)

        try:
            msg_list.append(q_obj.get(timeout=60))
        except queue.Empty:
            print("\033[41;1mno msg for [%s][%s] ,timeout\033[0m" %(request.user.userprofile.id,request.user))
    return HttpResponse(json.dumps(msg_list))

def delete_cache_key(request):
    cache_key = request.GET.get("cache_key")
    cache.delete(cache_key)
    return HttpResponse("cache key [%s] got deleted" % cache_key)

def file_upload(request):
    print('----POST:',request.POST)
    print('----FILE:',request.FILES)
    file_obj = request.FILES.get('file')
    user_home_dir = "uploads/%s" % request.user.userprofile.id
    if not os.path.isdir(user_home_dir):
        os.mkdir(user_home_dir)
    new_file_name= "%s/%s" %(user_home_dir,file_obj.name)
    recv_size = 0
    with open(new_file_name,"wb") as new_file_obj:
        for chunk in file_obj.chunks():
            new_file_obj.write(chunk)
            recv_size += len(chunk)
            cache.set(file_obj.name,recv_size)
    # 上传完之后让对方收到图片
    # 判断对方的Q存不存在
    # if GLOBAL_MSG_QUEUES
    return HttpResponse("--upload success---")

def get_file_upload_progress(request):
    filename = request.GET.get("filename")
    progress = cache.get(filename)
    print('filename',cache)
    print("file[%s] uploading progress[%s]" %(filename,progress))
    return HttpResponse(json.dumps({"recv_size":progress}))

#添加好友步骤
# 1、查找微信号
def info_search(request):
    #info_search
    recv_data = json.loads(request.POST['data'])
    Search_type = recv_data['SearchType']
    Search_Num = recv_data['SearchNum']
    if Search_type == 'User':
        # 定义默认返回的数据格式
        data={}
        data['Check_Friend']='null'
        data['get_user_img']=''
        data['get_user_name']=''
        data['get_user_Num'] = ''
        data['get_user_id'] = ''
        #获取查询的对象是否存在
        Search_ret = bbs_modeles.UserProfile.objects.filter(Wechat_num=Search_Num)
        print('----ret:',Search_ret)
        # 获取这个用户是否是我的朋友
        # My_friends = request.user.userprofile.friends.select_related()
        # print(My_friends)
        if Search_ret:
            Check_Friend = 'Exit'
            print('~~~~~~~~~~~~~~~~~EXIT!!!')
            get_user_img = Search_ret[0].head_img.name
            get_user_name = Search_ret[0].name
            get_user_Num = Search_ret[0].Wechat_num
            get_user_id = Search_ret[0].id
            data['Check_Friend']=Check_Friend
            data['get_user_img']=get_user_img
            data['get_user_name']=get_user_name
            data['get_user_Num']=get_user_Num
            data['get_user_id']=get_user_id
        else:
            Check_Friend = 'NoExit'
            print('~~~~~~~~~~~~~~~~~NoExit')
            # for friend in My_friends:
            #     if Search_ret[0].name == friend.name:
            #         Check_Friend = 'Exit' # 好友存在
            #         print("Friend Exit!!")
            #         break
            # if Check_Friend != 'Exit':
            # 获取查询的用户的头像和名称 返回到前端

    return HttpResponse(json.dumps(data))

#查询好友资料后确认添加好友
def Add_Friend(request):
    if request.method == 'POST':
        data = json.loads(request.POST['data'])
        print("recv:",data)
# recv: {'to': 2, 'from': 5, 'msg_type': 'add_user', 'msg': 10004, 'type': 'add_user'}
        from_user_name = bbs_modeles.UserProfile.objects.get(id=data['from'])
        data['from_name'] = from_user_name.name
        data['use_img'] = from_user_name.head_img.name.split("/")[1]
        data['Wechat_Num'] = from_user_name.Wechat_num
        if not GLOBAL_MSG_QUEUES.get(int(data['to']) ):
            GLOBAL_MSG_QUEUES[int(data["to"])] = queue.Queue()
        GLOBAL_MSG_QUEUES[int(data["to"])].put(data)
    return HttpResponse("OK")

def Confirm_add_user(request):
    if request.method == 'POST':
        friend_id = int(request.POST['data'])
        print(friend_id)
        friend_obj= bbs_modeles.UserProfile.objects.get(id=friend_id)
        self_obj = request.user.userprofile.user
        self_obj.userprofile.friends.add(friend_obj)
    return HttpResponse("Success")

