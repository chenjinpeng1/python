#python 3.5环境,解释器在linux需要改变
# -*- encoding:utf-8 -*-
#Auth  ChenJinPeng
import os
from django.db.models import F,Q
os.environ['DJANGO_SETTINGS_MODULE']='day18.settings'
import django
django.setup()
from crm import models
# 多对多展示
# data = models.Customer.objects.all()
# print(data)
# for i in data:
#     m2m=i.class_list.all()# 这里如果想获取每个对象对应的字段值要循环字段
#     print(m2m)
#     for i in m2m:
#         print(i)
# fields = models.Customer._meta._get_fields()
# for i in fields:
#     print(i.name)
print("--------------------")
# fields=models.Customer._meta.fields # 此方法不能获取多对多字段
# for i in fields:
#     print(i.name)

# for i in data:
#     for field in fields:
#         if hasattr(field,'verbose_name'):
#             if hasattr(i,field.name):
#                 if field.many_to_many:
#                     datas = getattr(i,field.name).all()
#                     # print("m2m",str(datas))
#                 elif field.choices:
#                     print(field.name)
#                     datas = getattr(i,"get_%s_display"%field.name)
#                     print(datas)
#                 else:
#                     datas = getattr(i,field.name)
#                     # print(datas)
#-------------------django modelform

from crm import Model_Forms
# formname = models.ClassList.objects.all()
# for i in formname:
#     print(i.id)
# form =Model_Forms.ModelForm() # 更新数据
# print(form)
# dir(form)
# print(models)
# datas = models.ClassList.objects.get(id=2)
# print(datas)
# print(datas.get_course_type_display())
# print(dir(models.__name__))
# for i in dir(models):
#     model_obj = getattr(models,i)
#     print (model_obj._meta.app_label)
u1 = models.ClassList.objects.get(id=28)# 外键查询
print(u1)
print(u1.course)
u2 = models.Course.objects.get(id=1) # 反向查询
print(u2.customer_set.select_related())

#多对多查询
a1 = models.UserProfile.objects.get(id=2) # 反向查询
print(a1)
print(a1.school_set.select_related())

a2 = models.School.objects.get(id=1)
print(a2)
print(a2.staffs.select_related())



