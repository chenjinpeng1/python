#python 3.5环境,解释器在linux需要改变
# -*- encoding:utf-8 -*-
#Auth  ChenJinPeng
import random
def insert_sort(num):
    for i in range(1,len(num)):
        position = i #当前的索引位置
        current_val = num[i] #当前值
        while position > 0 and current_val < num[position-1]: #索引大于0为循环开始和结束条件 当前值小于前一个值为开始条件
            num[position] = num[position-1] # 循环成立表示当前值小于前一个值
            position-=1 # 索引减一，往前继续判断
        num[position]=current_val # 知道判断不成立后赋值
    return num




if __name__ == "__main__":
    a = []
    import time
    start_time = time.time()
    for i in range(50000):
        a.append(random.randrange(100000))
    print(a)
    ret = insert_sort(a)
    print(ret)
    stop_time = time.time()
    sum_time = stop_time-start_time
    print(sum_time)