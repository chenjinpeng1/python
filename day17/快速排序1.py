#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li
import random,time
def quick_sort(array,start,end):
    print("-->",start,end)
    if start == end:
        return
    k = array[start]
    left_flag = start
    right_flag = end
    while left_flag <right_flag:
        while array[right_flag] > k: # 代表要继续往左边移动小旗子
            right_flag -=1
        tmp = array[left_flag]
        array[left_flag] = array[right_flag]
        array[right_flag] = tmp

        #左边小旗子开始向右移动
        while  array[left_flag] < k :
            left_flag +=1
        #上面的loop一跳出，代表左边小旗子 现在所处的位置的值是比k大的，
        tmp = array[left_flag]
        array[left_flag] = array[right_flag]
        array[right_flag] = tmp
        print(array,left_flag,right_flag)
    #开始把问题分半

    quick_sort(array,start,left_flag)
    quick_sort(array,left_flag+1,end)
if __name__ == '__main__':



    array =[64, 77,10, 68] #67, 8, 6,14, 84, 55,14, 20, 43] #[871, 100, 160, 755, 614, 621, 403, 671, 256, 915, 174, 906, 253, 973, 199, 370, 950, 970, 287, 648]
    #[55,64,64,67,77,84] 58
    #for i in range(50000):
    #    array.append(random.randrange(100000))
    #print('list generate done ')
    print(array)
    time_start = time.time()
    quick_sort(array,0,len(array)-1)
    time_end = time.time()
