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
import pickle,codecs
# f = open("chen/tmp.log","wb")
# info["chen"]=["aa","0","0",0]
# f.write(pickle.dumps(info))
# f.close()

f = open("chen/tmp.log","rb")
a=pickle.loads(f.read())
print(a)



# a = {"chen":"taishuai"}
# B=pickle.dumps(a)
# print(type(B))
# C=pickle.loads(B)
# print(C)


#--------------------
# f = open("作业思路分析.txt","ab")
# f.write(pickle.dumps("wowowowowowowo"))
# f.close()









# print('-------------------------')
# d = open("chen/tmp.log","rb")
# a=pickle.loads(d.read())
# duandian=a["chen"][2]
# read = codecs.open("作业思路分析.txt","rb")
# read.seek(10)
# print(read.read(10))
#b'\x80\x81\xe8\xb4\xa6\xe5\x8f\xb7\xe5\xaf'
#b'client\r\n1\xe3\x80\x81\xe8\xb4\xa6\xe5\x8f\xb7\xe5\xaf'



