#python 3.5环境,解释器在linux需要改变
# -*- encoding:utf-8 -*-
#Auth  ChenJinPeng
# import configparser
# config = configparser.ConfigParser()
# config['Log'] = {'ServerAliveInterval':'45',
#                  'Compression' : 'yes',
#                  'CompressionLevel': '9'}
# config['esuizhen'] = {}
# config['esuizhen']['User'] = '1'
# with open('aa.log','w') as A:
#     config.write(A)
# Read_log=configparser.ConfigParser()
# Read_log.read('aa.log')
# print(Read_log['esuizhen']['User'])
# A=Read_log.options('esuizhen')
# print(A)
# A=Read_log.items('esuizhen')
# print(A)
# A=Read_log.get('esuizhen','User')
# print(A)
# A=Read_log.getint('esuizhen','User')  #get 和getint的区别是getint 对于获取的值必须可以转换为int类型
# print(A)
# ############### 定义 ###############
# class Foo():
#
#     def func(self):
#         print('aa')
#     # 定义属性
#     @property
#     def prop(self):
#         print('bb')
# # ############### 调用 ###############
# foo_obj = Foo()
# foo_obj.func()
# foo_obj.prop   #调用属性
# A=Foo()
# print(A.func())

class C(object):

    def __init__(self):
        self.__foo = "私有字段"

    def func(self):
        print(self.__foo)#　类内部访问

class D(C):

    def show(self):
        print (self.foo) #派生类中访问
#
obj = C()
# # obj.__foo     # 通过对象访问    ==> 错误
obj.func()  # 类内部访问        ==> 正确
obj_son = D();
obj_son.func()  # 派生类中访问  ==> 错误
#
# print(obj_son._C__foo)
#!/usr/bin/env python
# -*- coding:utf-8 -*-

class C:

    def __init__(self):
        self.name = 'wupeiqi'








