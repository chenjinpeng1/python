from django.shortcuts import render,HttpResponse,redirect
from django.shortcuts import  HttpResponse,HttpResponseRedirect
from cmdb import models
import json
# Create your views here.
def login(request):
    # return HttpResponse("OK")
    if request.method == "POST":
        username = request.POST['username']
        passwd = request.POST['passwd']
        userinfo = models.UserInfo.objects.filter(username=username,password=passwd)
        if userinfo:
            hostinfo = models.HostInfo.objects.all()
            print("login ok")
            return HttpResponseRedirect('/cmdb/index/')
        else:
            return render(request,'login.html',{'error':'账号密码错误'})
    else:
        return render(request,'login.html')
def index(request):
    return render(request,'index.html')

def regist(request):
    return render(request,'regist.html')

def HostManage(request):
    if request.method == "POST":
        data =  json.loads(request.POST['data'])
        for i in data:
            print(i)
            selecthost = models.HostInfo.objects.filter(id=i['id'],hostname=i['hostname'],port=i['port'],ip=i['ipaddress'])
            if not selecthost:
                models.HostInfo.objects.filter(id=i['id']).update(hostname=i['hostname'],port=i['port'],ip=i['ipaddress'])
        # hostinfo = models.HostInfo.objects.all()
        # return render(request,'backmanage.html',{'hostinfo':hostinfo})
        return HttpResponse("OK")

    else:
        hostinfo = models.HostInfo.objects.all()
        return render(request,'backmanage.html',{'hostinfo':hostinfo})

def selectedit(request):
    if request.method == 'POST':
        data = json.loads(request.POST['data'])
        print(data['id'],data['hostname'])
        checkinfo = models.HostInfo.objects.filter(id=data['id'],hostname=data['hostname'],ip=data['ipaddress'],port=data['port'])
        print(checkinfo)
        if not checkinfo:
            models.HostInfo.objects.filter(id=data['id']).update(hostname=data['hostname'],ip=data['ipaddress'],port=data['port'])
        return HttpResponse("OK")

def AddHost(request):
    if request.method == "POST":
        # data = json.loads(request.POST['data'])
        data = request.POST
        print(data)
        # print(data)
        checkhost = models.HostInfo.objects.filter(hostname=data['AddHostName'],ip=data['AddIp'],port=data['AddPort'])
        if not checkhost:
            models.HostInfo.objects.create(hostname=data['AddHostName'],ip=data['AddIp'],port=data['AddPort'])
            data = models.HostInfo.objects.all()
            return render(request,'backmanage.html',{'hostinfo':data})
        else:
            return HttpResponse("主机存在")