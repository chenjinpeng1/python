#python 3.5环境，解释器在linux需要改变
#阅读手册查询readme文件
#作者：S12-陈金彭
import time
import threading

def run(n):

    print('[%s]------running----\n' % n)
    time.sleep(2)
    print('--done--')

def main():
    for i in range(5):
        t = threading.Thread(target=run,args=[i,])
        #time.sleep(1)
        t.start()
        print('starting thread', t.getName())


m = threading.Thread(target=main,args=[])
m.setDaemon(True) #将主线程设置为Daemon线程,它退出时,其它子线程会同时退出,不管是否执行完任务
m.start()
m.join()
print("---main thread done----")