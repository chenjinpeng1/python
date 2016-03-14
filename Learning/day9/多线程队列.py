#python 3.5环境,解释器在linux需要改变
# -*- encoding:utf-8 -*-
#Auth  ChenJinPeng
import time
import queue
import threading
q=queue.Queue()
def consumer(n):
    while True:
        print("consumer [%s] get task %s"%(n,q.get()))
        time.sleep(1)
        q.task_done()
def producer(n):
    count = 1
    while True:
        print("prodcer [%s] produced a new task:%s"%(n,count))
        q.put(count)
        count+=1
        q.join()
        print("all talks has been cosumed by consumers...")
c1=threading.Thread(target=consumer,args=[1,])
c2=threading.Thread(target=consumer,args=[2,])
c3=threading.Thread(target=consumer,args=[3,])
c1.start()
c2.start()
c3.start()
p1=threading.Thread(target=producer,args=["A"])
p2=threading.Thread(target=producer,args=["B"])
p1.start()
p2.start()

