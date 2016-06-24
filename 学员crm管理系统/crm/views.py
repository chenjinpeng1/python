from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from crm import models
from django.db.models.base import ModelBase
import collections
from crm import Model_Forms
import json
import hashlib
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def index(request):
    classnames = collections.OrderedDict()
    for i in dir(models):
        if isinstance(getattr(models,i),ModelBase):
            name = getattr(models,i)._meta.verbose_name
            classnames[name]=(getattr(models,i).__name__)
    return render(request,'index.html',{'classnames':classnames,
                                        'user':request.user}
                                            )

def get_value(obj):
    if hasattr(models,obj):
        func=getattr(models,obj)
        fields = func._meta._get_fields() # 获取所有字段
        datas = func.objects.all() # 获取所有数据
        field_values = [] #返回字段对应的数据
        for data in datas:
            tmp_value = [] # 临时值
            for field in fields:
                if hasattr(field,'verbose_name'):
                    if field.many_to_many:
                        tmp = [] # 多对多的临时值
                        values = getattr(data,field.name).all()
                        for value in values:
                            tmp.append(str(value))
                        tmp_value.append([field.name,tmp])
                    elif field.choices:
                        values = getattr(data,"get_%s_display"%field.name)()
                        tmp_value.append([field.name,values])
                    else:
                        values = getattr(data,field.name)
                        tmp_value.append([str(field.name),str(values)])
            field_values.append(tmp_value)
        return field_values
def func(request,obj):
    print('------------',request.user)
    if hasattr(models,obj):
        func = getattr(models,obj) #获取传入的参数对应的类
    else:
        return HttpResponse("参数错误")
    if request.method == "POST":
        print(request.POST,obj)
        if hasattr(models,obj):
            func = getattr(models,obj)
        else:
            return HttpResponse("参数错误")
        ID_list = json.loads(request.POST['data'])
        for key,val in ID_list.items():
            # Add的处理
            if key == "id":
                Auth_result = False
                for ID in val:
                    ID=int(ID)
                    auth_data = func.objects.filter(id=ID)
                    if auth_data:
                        auth_data.delete()
                        Auth_result = True
                    else:
                        Auth_result = False
                        break
                if Auth_result:
                    return HttpResponse("True")
                else:
                    return HttpResponse("False")
            else:
                # Search的处理
                get_values = get_value(obj)
                print(get_values)
                field_values = []
                for values in get_values:
                    for value in values:
                        if val == str(value[1]):
                            field_values.append(values)
                            break
                        else:
                            continue
                if len(field_values)== 0:
                    field_values=""
                return HttpResponse(json.dumps(field_values))
    class_verbose_name = func._meta.verbose_name_plural # 获取自定义表名
    # field_list = func._meta.fields #获取所有字段集合,不包含多对多字段
    field_list = func._meta._get_fields() #获取所有字段集合
    field_verbose_name = []
    #--------------获取自定义字段名
    for i in field_list:
            if hasattr(i,'verbose_name'):
                field_verbose_name.append(i.verbose_name)
    field_values = get_value(obj)
    return render(request, 'show_field_info/field_dis_model.html', {
                                                        'field_verbose_name':field_verbose_name,
                                                        'class_verbose_name':class_verbose_name,
                                                        'field_values':field_values,
                                                        'classname':obj,
                                                        'field_list':field_list,
                                                        'Request':request})

def addfunc(request,obj):
    if hasattr(models,obj):
        func=getattr(models,obj)
        objs = Model_Forms.get_form(func)
        if request.method == 'POST':
            objs = Model_Forms.get_form(func,request.POST)
            if objs.is_valid():
                print("OK Auth Success")
                objs.save()
                base_url = "/".join(request.path.split("/")[:-2])
                return redirect(base_url)
        class_verbose_name = func._meta.verbose_name_plural # 获取自定义表名
        return render(request,'Add/index.html',{'forms':objs,
                                            'class_verbose_name':class_verbose_name,
                                            'classname':obj,})

def changefunc(request,obj,id):
    if hasattr(models,obj):
        func = getattr(models,obj)
        get_data = func.objects.get(id=id)
        result_data = Model_Forms.get_form(func,instance=get_data)
        if request.method=="POST":
        #     print(request.POST)
            result_data = Model_Forms.get_form(func,request.POST,instance=get_data)
            if result_data.is_valid():
                result_data.save()
                print("auth ok")
                base_url = "/".join(request.path.split("/")[:-2])
                print(base_url)
                return  redirect(base_url)
        print(dir(result_data.errors))
        print(result_data.errors.get.__getattribute__)
        print(obj,id)
        print(type(obj),type(id))
        return render(request,'update/update_data.html',{'datas':result_data,
                                                         'classname':obj,
                                                         'id':id,

                                                         })

def ac_login(request):
    if request.method =='POST':
        username = request.POST['username']
        passwd = request.POST['password']
        print("用户名：%s 密码:%s"%(username,passwd))
        user = authenticate(username=username,password=passwd)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/crm')
        else:
            log_error = 'Wrong user or Passwd'
            return render(request,'login/index.html',{'log_error':log_error})
    return render(request,'login/index.html')
def ac_logout(request):
    logout(request)
    return HttpResponseRedirect('/')