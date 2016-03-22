from twisted.internet import protocol
from twisted.internet import reactor   #reactor是twisted事件循环的核心，它提供了一些服务的基本接口，像网络通信、线程和事件的分发
class Echo(protocol.Protocol):    #必须自己定义一个类,继承protocol，成为protocol的子类
    def dataReceived(self, data): # 只要twisted收到数据就会调用此方法
        self.transport.write(data)  #写入数据到物理链接     类似send发送数据

def main():
    factory = protocol.ServerFactory() #protocol.ServerFactor是一个基础工厂类，里面为空，但是你必须要定义，将你自定义的类作为参数传入
    factory.protocol = Echo #定义类下的方法，默认在ServerFactory里protocol是None
    reactor.listenTCP(1234,factory)#reactor绑定端口和重新定义的类，客户端连接过来的操作在自定义的类里完成
    reactor.run() #  启动分发器 | 类似于select的监听，有连接就触发重新定义类里的操作 （因为在上面已经绑定了类）

if __name__ == '__main__':
    main()