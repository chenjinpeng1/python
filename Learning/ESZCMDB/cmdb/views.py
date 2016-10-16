from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt # 不经过csrf验证
import json
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from cmdb import core,models
# Create your views here.
@csrf_exempt
def assert_report(request):
    if request.method == 'POST':
        print(request.POST)
        if request.POST.get("hostid") != "*":
            ass_handler = core.Asset(request)
            if ass_handler.data_is_valid():
                print("----asset data valid:")
                ass_handler.data_inject()
                #return HttpResponse(json.dumps(ass_handler.response))
            else:
                print(ass_handler.response)
            return HttpResponse(json.dumps(ass_handler.response))
    else:pass
        #return render(request,'assets/asset_report_test.html',{'response':ass_handler.response})
        #else:
            #return HttpResponse(json.dumps(ass_handler.response))

    return HttpResponse('--test--')

def acc_login(request):
    if request.method == 'POST':
        print(request.POST)
        user = authenticate(username=request.POST.get('user'),
                            password=request.POST.get('passwd'))
        if user is not None:
            #pass authentication
            login(request,user)
            return HttpResponseRedirect(request.GET.get('next') or '/manage')
        else:
            log_error = "Wrong username or password!"
            return render(request,'cmdb/pages/examples/login.html',{'log_error':log_error})
    return render(request,'cmdb/pages/examples/login.html')

def acc_logout(request):
    logout(request)
    return HttpResponseRedirect('/bbs')
@login_required
def ServerDashboard(request):
    return render(request,"cmdb/index.html")

def assetslist(request):
    data = []
    servers = models.Asset.objects.filter(assert_type='server')
    # serverdata['servers'].append(servers)
    for server in servers:

        tmp = {}
        ram_size = 0
        disk_size = 0
        for i in server.ram_set.select_related():
            ram_size += i.capacity
        for i in server.disk_set.select_related():
            disk_size += i.capacity
        tmp['hostname'] = server.name
        tmp['manageip'] = server.management_ip
        tmp['idc'] = server.id
        tmp['business_unit'] = server.business_unit
        tmp['os'] = server.server.os_release
        tmp['cpu_count'] = server.cpu.cpu_count
        tmp['ram_size'] =  ram_size
        tmp['disk_size'] = disk_size
        tmp['hostid'] = server.id
        data.append(tmp)

    #     print("servername:",server.name,"manageIp:",server.management_ip,'idc:',server.idc,'业务线:',server.business_unit,"cpu_count:",server.cpu.cpu_count)
    return render(request,'cmdb/assets/index.html',{
                                            'hostsdata':data
    })
# @login_required
def hostdetail(request,id):
    obj = models.Asset.objects.get(id=id)
    classname = obj._meta.verbose_name
    print(obj.name,obj._meta.verbose_name)
    return render(request,'cmdb/assets/assetdetail.html',{'asset_obj':obj,
                                                          'classname':classname})
