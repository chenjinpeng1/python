#python 3.5环境,解释器在linux需要改变
# -*- encoding:utf-8 -*-
#Auth  ChenJinPeng

import threading # threading 线程模块
import time

def sayhi(num): #定义每个线程要运行的函数

    print("running on number:%s" %num)

    time.sleep(3)

if __name__ == '__main__':

    t1 = threading.Thread(target=sayhi,args=(1,)) #生成一个线程实例
    t2 = threading.Thread(target=sayhi,args=(2,)) #生成另一个线程实例
    a3 = threading.Thread(target=sayhi,args=(3,)) #生成另一个线程实例

    t1.start() #启动线程
    t2.start() #启动另一个线程
    a3.start()

    print(t1.getName()) #获取线程名
    print(t2.getName())
    print(a3.getName())

# import threading
# import time
# def sayhai(num):
#     print("running on thread - %s"%num)
#     time.sleep(3)
# if __name__ == "__main__":
#     t_list = []
#     for i in range(10):
#         t = threading.Thread(target=sayhai,args=(i,))
#         t.start()
#         print(t.getName())
#         t_list.append(t)
#     # for i in t_list:
#     t.join()
#     print("last start")
from multiprocessing import Process
import os,sys
sys.argv