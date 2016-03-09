#python 3.5环境，解释器在linux需要改变
#阅读手册查询readme文件
#作者：S12-陈金彭
import sys,hashlib,os,subprocess
# os.chdir('C:/Users/chen/PycharmProjects/python/day7/chen')
# print(os.getcwd())
# a=os.path.join(os.getcwd(),)
# b=os.getcwd()
# print(b)
# a=os.chdir("./")
# print(os.getcwd())
# cmd_call = subprocess.Popen("rename chen chen1",shell=True) # 将读取到的命令通过管道符进行输出到变量
# cmd_result = cmd_call.stdout.read()
# print(cmd_call)
'''
aaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaa
aaaaaaaaaaaa
aaaaaaaaaaaa
aaaaaaaaaaaa
'''
# file = input(">>>:")
# AA=os.path.isfile(file)
# # print(AA)
# # if AA is not True:
# #     print("wocao")
# # if A is not True:
# #     print(A)
# # else:
# #     print("exit")
# a=open("bb.pdf","rb")
# # # aa=open("cc.pdf","wb")
# # b=0
# for i in a.readlines():
#     aa=hashlib.md5()
#     aa.update(i)
#     print(i)
#     print(aa.hexdigest())
#     aa.write(i)
#     b+=1
# print(b)
# if os.path.isfile("作业思路分析.txt") is True:print("aaaaaaaa")
# CUR_PATH=os.path.dirname(os.path.abspath(__file__)).replace("\\","/")
# print(CUR_PATH)
# print(os.stat("./"))
#!/usr/bin/env python
# -*- coding=utf-8 -*-
#Using GPL v2
#Author: ihipop@gmail.com
#2010-10-27 22:07
"""
Usage:
Just A Template
"""
# a=os.path.abspath("./")
# print(a)
# print(os.getcwd())

import time
# for i in range(100000):
#     # percent = 1.0 * i / 100000 * 100
#     # print('complete percent:%10.8s%s'%(str(percent),'%'),end='\r')
#     # time.sleep(0.3)
#     print("aaa",end="\r")

import os,sys
# import codecs
# f = open("aa.txt", "wb")
# with codecs.open("作业思路分析.txt","rb","utf8") as fread:
#     while True:
#         A=fread.read(100)
#         print(A)
#         if len(A) == 0:break
#         print(fread.tell())
info={}
# b["1"]=[1,2,3]
# import pickle,codecs
# f = open("chen/tmp.log","wb")
# info["chen"]=["aa","0","0",0]
# f.write(pickle.dumps(info))
# f.close()

# f = open("chen/movie/tmp.log","rb")
# a=pickle.loads(f.read())
# print(a)
# a=os.path.abspath(__file__)
# print(a)
# b=a.replace("\\","/").replace("C:/Users/chen/PycharmProjects","")[1:]
# print(b)
# print(os.getcwd())
# a="a|b"
# print(a.split("|")[0],a.split("|")[1])
# /aa/bb/cc/chen/movie
#movie
#/aa/bb/chen

# a = {"chen":"taishuai"}
# B=pickle.dumps(a)
# print(type(B))
# C=pickle.loads(B)
# print(C)
# a=os.getcwd()
# print(a)
# b={"chen":['|aa.txt',0,0,0]}
# a=b["chen"][0].split("|")
# print(a)

#--------------------
# f = open("作业思路分析.txt","ab")
# f.write(pickle.dumps("wowowowowowowo"))
# f.close()

# a="/aa/bb/aa.txt"
# b=a.split("/")
# print(b)
# if len(b) == 1:
#     print(b[0])
# else:
#     print(b[-1])
#     print("eeeee")







# print('-------------------------')
# d = open("chen/tmp.log","rb")
# a=pickle.loads(d.read())
# print(a)
# read = codecs.open("作业思路分析.txt","rb")
# read.seek(10)
# print(read.read(10))
#b'\x80\x81\xe8\xb4\xa6\xe5\x8f\xb7\xe5\xaf'
#b'client\r\n1\xe3\x80\x81\xe8\xb4\xa6\xe5\x8f\xb7\xe5\xaf'

#!/usr/bin/env python
# import sys,os;
# def DIR_SIZE(name,num):
#     B=os.listdir(name)
#     print(name,B)
#     for i in B:
#         C="%s/%s"%(name,i)
#         num+=os.path.getsize(C)
#     print(name,num)
#     return num
# def ALL_SIZE(name):
#     num = 0
#     a=0
#     LIST=os.listdir(name)
#     print(LIST)
#     for i in LIST:
#         aaa="%s/%s"%(name,i)
#         d=os.path.isdir(aaa)
#         if d:
#             a+=1
#             num=DIR_SIZE(aaa,num)
#         else:
#             num+=os.path.getsize(aaa)
#     print(num)
#
# ALL_SIZE("./")
class Foo():

    def __init__(self, name):
        self.name = name

    def ord_func(self):
        """ 定义普通方法，至少有一个self参数 """

        # print self.name
        print ('普通方法')

    @classmethod
    def class_func(cls):
        """ 定义类方法，至少有一个cls参数 """

        print ('类方法')

    @staticmethod
    def static_func():
        """ 定义静态方法 ，无默认参数"""

        print ('静态方法')


# 调用普通方法
f = Foo("chen")
f.ord_func()

# 调用类方法
Foo.class_func()

# 调用静态方法
Foo.static_func()




