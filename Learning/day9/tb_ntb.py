#python 3.5环境，解释器在linux需要改变
#阅读手册查询readme文件
#作者：S12-陈金彭
import gevent
def task(pid):
    """
    Some non-deterministic task
    """
    gevent.sleep(0.5)
    print('Task %s done' % pid)

def synchronous():
    for i in range(1,10):
        task(i)
def asynchronous():
    threads = [gevent.spawn(task, i) for i in range(10)]
    gevent.joinall(threads)
print('Synchronous:')
synchronous()
print('Asynchronous:')
asynchronous()
