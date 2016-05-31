from django.shortcuts import render,HttpResponse,redirect
from crm import models
from django.db.models.base import ModelBase
import collections
from crm import Model_Forms
# Create your views here.
def index(request):
    classnames = collections.OrderedDict()
    for i in dir(models):
        if isinstance(getattr(models,i),ModelBase):
            name = getattr(models,i)._meta.verbose_name
            classnames[name]=(getattr(models,i).__name__)
    return render(request,'index.html',{'classnames':classnames})

def func(request,obj):
    if hasattr(models,obj):
        func = getattr(models,obj) #获取传入的参数对应的类
    else:
        return HttpResponse("error")
    class_verbose_name = func._meta.verbose_name_plural # 获取自定义表名
    # field_list = func._meta.fields #获取所有字段集合,不包含多对多字段
    field_list = func._meta._get_fields() #获取所有字段集合
    field_verbose_name = []
    #--------------获取自定义字段名
    for i in field_list:
            if hasattr(i,'verbose_name'):
                field_verbose_name.append(i.verbose_name)
    #------------------获取数据
    datas = func.objects.all() #获取所有数据集合
    field_values = []
    STR_FIELD = []
    for data in datas:
        tmp_value = []
        for field in field_list:
            if hasattr(field,'verbose_name'):
                if field.many_to_many:
                    if hasattr(data,field.name):
                        values = getattr(data,field.name).all()
                        tmp = []
                        for value in values:
                            tmp.append(str(value))
                        tmp_value.append([str(field.name),tmp])
                elif field.choices:
                    value = getattr(data,"get_%s_display"%field.name)
                    tmp_value.append([str(field.name),value])
                else:
                    value = getattr(data,field.name)
                    tmp_value.append([str(field.name),str(value)])
        print(tmp_value)
        field_values.append(tmp_value)
        print(field_values)
    return render(request, 'show_field_info/field_dis_model.html', {'field_verbose_name':field_verbose_name,
                                                        'class_verbose_name':class_verbose_name,
                                                        'field_values':field_values,
                                                        'classname':obj,
                                                        'field_list':field_list,
                                                        'DATAS':datas})

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