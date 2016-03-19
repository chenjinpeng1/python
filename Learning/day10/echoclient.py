from twisted.internet import reactor, protocol


# a client protocol

class EchoClient(protocol.Protocol):
    """Once connected, send a message, then print the result."""

    def connectionMade(self): # 发送函数
        self.transport.write("hello alex!") # 发送一个消息到服务端

    def dataReceived(self, data):#接收函数
        "As soon as any data is received, write it back."
        print "Server said:", data # 打印接收的数据
        self.transport.loseConnection() #loseConnection的意思为将所有挂起的数据写入，执行关闭链接操作

    def connectionLost(self, reason): # 执行完毕后调用该函数  类似finish
        print "connection lost"

class EchoFactory(protocol.ClientFactory):
    protocol = EchoClient # 客户端必须重写自己的类使用（protocol定义必须重写）

    def clientConnectionFailed(self, connector, reason):
        print "Connection failed - goodbye!"
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print "Connection lost - goodbye!"
        reactor.stop()


# this connects the protocol to a server running on port 8000
def main():
    f = EchoFactory() # 实例化定义的类
    reactor.connectTCP("localhost", 1234, f)
    reactor.run()

# this only runs if the module was *not* imported
if __name__ == '__main__':
    main()