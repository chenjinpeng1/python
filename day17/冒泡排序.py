# #python 3.5环境,解释器在linux需要改变
# # -*- encoding:utf-8 -*-
# #Auth  ChenJinPeng
# import random
# array = [22,1,55,7,24,67,111,666,222,12,2,999,223,432,123,456]
#
# def array_sort(num):
#     a = 0
#     for i in range(len(num)):
#         for j in range(len(num)-1-i):
#             if num[j] > num[j+1]:
#                 tmp = num[j]
#                 num[j] = num[j+1]
#                 num[j+1] = tmp
#                 a+=1
#         print(num)
#     print(a)
#     return num
#
# aa = []
# import time
# start_time = time.time()
# for i in range(50000):
#     aa.append(random.randrange(1000))
# print(array_sort(aa))
# stop_time = time.time()
# sum_time = stop_time-start_time
# print(sum_time)
import os
print(os.path.abspath(__file__))