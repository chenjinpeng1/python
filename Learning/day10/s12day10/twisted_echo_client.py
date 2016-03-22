#!/usr/bin/env python
# -*- coding:utf-8 -*-
from twisted.internet import reactor, protocol

# a client protocol

class EchoClient(protocol.Protocol):
    """Once connected, send a message, then print the result."""
    def connectionMade(self): #连接一建立成功，就会自动调用 此方法
        print("connection is build, sending data...")
        self.transport.write(bytes("hello alex!","utf8")) # 向server端send一条消息

    def dataReceived(self, data): # 接受server端返回的消息
        "As soon as any data is received, write it back."
        print ("Server said:", data.decode())
        self.transport.loseConnection()
        # exit('exit')

    def connectionLost(self, reason):
        print ("====connection lost===")

class EchoFactory(protocol.ClientFactory): # client也必须定义自己的类，继承ClientFactory类，重写方法
    protocol = EchoClient  #handle 父类调用了protocol，但是在父类里protocol为空，类似于handle，所以你要定义一个类被这里调用

    def clientConnectionFailed(self, connector, reason): # 父类里的该方法为空，你必须自己定义 （如果连接失败了，直接执行该方法）
        print ("Connection failed - goodbye!")
        reactor.stop()

    def clientConnectionLost(self, connector, reason): # 同理（如果连接关闭了，执行该方法）
        print ("Connection lost - goodbye!")
        reactor.stop()


# this connects the protocol to a server running on port 8000
def main():
    f = EchoFactory() # 实例化自定义的类
    reactor.connectTCP("localhost", 1234, f)
    reactor.run()

# this only runs if the module was *not* imported
if __name__ == '__main__':
    main()