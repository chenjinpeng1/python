#python 3.5环境，解释器在linux需要改变
#阅读手册查询readme文件
#作者：S12-陈金彭
import time,random
import queue,threading
q = queue.Queue()
def Producer(name):
  count = 0
  while count <5:
    time.sleep(random.randrange(3))
    q.put(count)
    print('Producer %s has produced %s baozi..' %(name, count))
    count +=1
def Consumer(name):
  count = 0
  while count <5:
    time.sleep(random.randrange(4))
    if not q.empty():
        data = q.get()
        print(data)
        print('\033[32;1mConsumer %s has eat %s baozi...\033[0m' %(name, data))
        count +=1
    else:
        print("-----no baozi anymore----")
p1 = threading.Thread(target=Producer, args=('A',))
c1 = threading.Thread(target=Consumer, args=('B',))
p1.start()
c1.start()