#python 3.5环境,解释器在linux需要改变
# -*- encoding:utf-8 -*-
#Auth  ChenJinPeng
# try:
#     # import aa
#     a = [11,22]
#     # print(a[3])
#     if bb == 3:
#         print("aaa")
#     bb=input(">>>:")
#     aa = int(bb)
# # except IndexError as e:
# #     print("indexError")
# #     print(e)
#
# except ImportError as e:
#     print('importError')
#     print(e)
#
# except AttributeError as e:
#     print("AttributeError")
#     print(e)
# except IOError as e:
#     print('IOError')
#     print(e)
# class ChenException(Exception):
#     def __init__(self,msg):
#         self.message = msg
#     def __str__(self):
#         return self.message
# # a=1
# try:
#     raise ChenException("我的异常")
# except Exception as e:
#     print(e)
# ChenException("我的异常")
# D=[]
# def A(num):
#     try:
#         for i in num:
#             for ii in A(i):
#                 print(ii)
#                 D.append(ii)
#                 # yield ii
#         return D
#     except:
#         pass
# B=[[1,2],[3,4],[5]]
# E=A(B)
# print(E)
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
import threading

def run(n):

    print('[%s]------running----\n' % n)
    time.sleep(2)
    print('--done--')

def main():
    for i in range(5):
        t = threading.Thread(target=run,args=[i,])
        t.start()
        print('starting thread', t.getName())


m = threading.Thread(target=main,args=[])
m.setDaemon(True) #将主线程设置为Daemon线程,它退出时,其它子线程会同时退出,不管是否执行完任务
m.start()
m.join(timeout=3)
print("---main thread done----")
from multiprocessing import Process
Process
