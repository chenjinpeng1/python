#python 3.5环境，解释器在linux需要改变
#阅读手册查询readme文件
#作者：S12-陈金彭
import time
import queue
def consumer(name):
    print("--->starting eating baozi...")
    while True:
        new_baozi = yield
        print("[%s] is eating baozi %s" % (name,new_baozi))
        #time.sleep(1)

def producer():

    r = con.__next__()
    r = con2.__next__()
    n = 0
    while n < 5:
        n +=1
        con.send(n)
        con2.send(n)
        print("\033[32;1m[producer]\033[0m is making baozi %s" %n )


if __name__ == '__main__':
    con = consumer("c1")
    con2 = consumer("c2")
    p = producer()