#!/usr/bin/env python
# -*- coding:utf-8 -*-
from twisted.internet import protocol # protocol模块里定义了__all__ 制定导入的类
from twisted.internet import reactor

class Echo(protocol.Protocol):
    def dataReceived(self, data):#只要twisted一收到 数据 ，就会调用 此方法
        print data
        self.transport.write(data) # 把收到的数据 返回给客户端

def main():
    MYCLASS = protocol.ServerFactory() #实例基础工厂类
    MYCLASS.protocol = Echo #封装Echo类（类似 socketserver 中handle）

    reactor.listenTCP(9000,MYCLASS) # 绑定端口和实例
    reactor.run()# 运行事件分发器

if __name__ == '__main__':
    main()