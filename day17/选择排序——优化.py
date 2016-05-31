#python 3.5环境,解释器在linux需要改变
# -*- encoding:utf-8 -*-
#Auth  ChenJinPeng
import random
def select_sort(num):
    for i in range(len(num)):
        smallvalue_index = i
        for j in range(i+1,len(num)):
            if num[smallvalue_index] > num[j]:
                smallvalue_index =j
        tmp = num[i]
        num[i] = num[smallvalue_index]
        num[smallvalue_index] = tmp
    return num


if __name__ == "__main__":
    a = []
    import time
    start_time = time.time()
    for i in range(50000):
        a.append(random.randrange(100000))
    print(select_sort(a))
    stop_time = time.time()
    sum_time = stop_time-start_time
    print(sum_time)