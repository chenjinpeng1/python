#python 3.5环境,解释器在linux需要改变
# -*- encoding:utf-8 -*-
#Auth  ChenJinPeng
import random,time
def quick_sort(array,start,end):
    if start>=end:
        return
    k = array[start]
    left_flag = start
    right_flag = end
    while left_flag < right_flag:
        #右边小旗子往左移动
        while  left_flag < right_flag and array[right_flag] > k:
            right_flag-=1
        tmp = array[left_flag]
        array[left_flag] = array[right_flag]
        array[right_flag] = tmp
        #左边小旗子往右移动
        while left_flag < right_flag and array[left_flag] <= k:
            left_flag+=1
        tmp = array[left_flag]
        array[left_flag]=array[right_flag]
        array[right_flag]=tmp

    quick_sort(array,start,left_flag-1)
    quick_sort(array,left_flag+1,end)
    return array

if __name__ == "__main__":
    # a = []
    a = [22,1,6,3,88,12,339,57,27,666]
    print(a)
    import time
    start_time = time.time()
    # for i in range(5000000):
    #     a.append(random.randrange(10000))
    ret = quick_sort(a,0,len(a)-1)
    stop_time = time.time()
    sum_time = stop_time-start_time
    # print(sum_time)
    print(ret)