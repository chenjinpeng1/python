from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required
from bbs import models
# Create your views here.
import queue,json,time
GLOBAL_MSG_QUEUES={}
GLOBAL_MSG_COUNTS={}
@login_required()
def dashboard(request):
    return render(request,'webchat/dashboard.html')

@login_required()
def send_msg(request):
    print(request.POST)
    msg_data = request.POST.get('data')
    print('send msg',msg_data)
    if msg_data:
        msg_data = json.loads(msg_data)
        msg_data['timestamp'] = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        if msg_data['type'] == 'single':
            friend_id = models.UserProfile.objects.get(id=int(msg_data['form']))
            friend_img = str(friend_id.head_img).replace("uploads","/static")
            print('user img',friend_img)
            msg_data['img'] = friend_img
            # check_Q(request) # 判断消息Q和消息数目Q对于用户是否存在，不存在创建
            if not GLOBAL_MSG_QUEUES.get(int(msg_data['to']) ):
                print("[%s]创建对方Q"%request.user)
                GLOBAL_MSG_QUEUES[int(msg_data["to"])] = queue.Queue()
            GLOBAL_MSG_QUEUES[int(msg_data['to'])].put(msg_data) # 上传消息到用户的消息队列
        if msg_data['type'] == 'group':
            print("发现是组消息")
    print('------Queue',GLOBAL_MSG_QUEUES)
    return HttpResponse("----msg recv")
@login_required()
def get_new_msgs(request):
    if request.user.userprofile.id not in GLOBAL_MSG_QUEUES:
        print('【%s】创建Q'%request.user)
        GLOBAL_MSG_QUEUES[request.user.userprofile.id] = queue.Queue()
    msg_count = GLOBAL_MSG_QUEUES[request.user.userprofile.id].qsize()
    print('[%s] 来收消息,消息大小[%s]'%(request.user,msg_count))
    q_obj = GLOBAL_MSG_QUEUES[request.user.userprofile.id]
    msg_list = []
    if msg_count > 0:
        for msg in range(msg_count):
            msg_list.append(q_obj.get())
        print('list_ret--',msg_list)
    else: #没消息 挂起
        try:
            msg_list.append(q_obj.get(timeout=60))
        except queue.Empty:
            print("------------------- time out")
    return HttpResponse(json.dumps(msg_list))