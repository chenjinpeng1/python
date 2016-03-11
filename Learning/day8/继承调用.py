#python 3.5环境,解释器在linux需要改变
# -*- encoding:utf-8 -*-
#Auth  ChenJinPeng
# import threading
# import time
# import sys
# class MyThread(threading.Thread):
#     def __init__(self,num):
#         # threading.Thread.__init__(self)
#         super(MyThread,self).__init__()
#         self.num = num
#
#
#     def run(self):
#         print("running on Threading - %s"%self.num)
#         time.sleep(3)
#
# if __name__ == "__main__":
#     t1 = MyThread(1)
#     t2 = MyThread(2)
#     t1.start()
#     t2.start()

import configparser
# info = configparser.ConfigParser()
# info["auth"]={}
# info["auth"]["chen"]="123"
# with open("user.log","a") as f:
#     info.write(f)
import collections
info = collections.OrderedDict()
info ["aa"] = {}
info["aa"]["bb"] = 1
print(info)