#python 3.5环境,解释器在linux需要改变
# -*- encoding:utf-8 -*-
#Auth  ChenJinPeng
# import time
# import threading
#
# def addNum():
#     global num #在每个线程中都获取这个全局变量
#     print('--get num:',num )
#     time.sleep(1)
#     num  -=1 #对此公共变量进行-1操作
#
# num = 100  #设定一个共享变量
# thread_list = []
# for i in range(100):
#     t = threading.Thread(target=addNum)
#     t.start()
#     thread_list.append(t)
# t.join()
#
# # for t in thread_list: #等待所有线程执行完毕
# #     t.join()
# print('final num:', num )


# import threading,time
# def addNum():
#     global num
#     print("------get num:",num)
#     time.sleep(1)
#     lock.acquire()
#     num -=1
#     lock.release()
#
# lock = threading.Lock()
# num = 100
# thread_list = []
# for i in range(100):
#     t = threading.Thread(target=addNum())
#     t.start()
#     thread_list.append(t)
# for t in thread_list:
#     t.join()