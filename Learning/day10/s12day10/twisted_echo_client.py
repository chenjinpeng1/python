#!/usr/bin/env python
# -*- coding:utf-8 -*-
from twisted.internet import reactor, protocol
# a client protocol
class EchoClient(protocol.Protocol):
    def connectionMade(self): #连接一建立成功，就会自动调用 此方法
        print("connection is build, sending data...")
        self.transport.write("hello") # 向server端send一条消息
    def dataReceived(self, data): # 接受server端返回的消息
        print ("Server said:", data.decode())
        self.transport.loseConnection() # 调用次方法自动执行connectionLost方法
        # exit('exit')
    def connectionLost(self, reason):
        print ("====connection lost===")
class EchoFactory(protocol.ClientFactory): # client也必须定义自己的类，继承ClientFactory类，重写方法
    protocol = EchoClient  #封装EchoClient类，内部执行类里的方法
    def clientConnectionFailed(self, connector, reason): # 父类里的该方法为空，你必须自己定义 （如果连接失败了，直接执行该方法）
        print ("Connection failed - goodbye!")
        reactor.stop()
    def clientConnectionLost(self, connector, reason): # 同理（如果连接关闭了，执行该方法）
        print ("Connection lost - goodbye!")
        reactor.stop()
def main():
    f = EchoFactory() # 实例化自定义的类
    reactor.connectTCP("localhost", 9000, f) #绑定端口，传入类实例
    reactor.run()

if __name__ == '__main__':
    main()