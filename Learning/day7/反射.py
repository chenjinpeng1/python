#python 3.5环境，解释器在linux需要改变
#阅读手册查询readme文件
#作者：S12-陈金彭
import sys
class Webserver(object):
    def __init__(self,host,port):
        self.host = host
        self.port = port
    def start(self):
        print('Server is starting...')
    def stop(self):
        print('Server is stoping...')
    def restart(self):
        self.stop()
        self.start()
        print('Server is restarting')
def test(ins,name): # ins这里类似于self
    print('test...')
    ins.stop()
if __name__ == "__main__":
    server = Webserver('local',333)
    if hasattr(server,sys.argv[1]):  #返回对象是否具有给定名称的属性。
        func = getattr(server,sys.argv[1]) #从一个对象获得命名属性;getattr(x,y)相当于x.y。
        func()
    setattr(server,'test_run',test)   #  强函数test方法加入到类Webserver里 server为实例名称，test_run为加入到类下的方法名称 test为要加入到类中的方法
    server.test_run(server,'name') # 将单独的方法加入到类中，方法内向调用类中的其他方法必须传入实例
    if sys.argv[1] == 'restart':
        server.restart()
    #------------------------------删除方法，传入实例的话不能删除类下的普通方法，只能删除静态方法或者通过setattr增加的方法（传入类名，可删除类下的方法）
    print(server.host)
    delattr(server,'host')
    print(server.host)     #>>正确

    server.test_run(server,'name')
    delattr(server,'test_run')
    server.test_run(server,'name')    #>>正确

    server.start()
    delattr(server,'start')
    server.start()    #>>错误