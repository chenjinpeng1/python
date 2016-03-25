#!/usr/bin/env python
# -*- coding:utf-8 -*-
# This is the Twisted Get Poetry Now! client, version 3.0.

# NOTE: This should not be used as the basis for production code.

import optparse

from twisted.internet.protocol import Protocol, ClientFactory


def parse_args():
    usage = """usage: %prog [options] [hostname]:port ...

This is the Get Poetry Now! client, Twisted version 3.0
Run it like this:

  python get-poetry-1.py port1 port2 port3 ... 指定服务器端的端口，可以同时接受多个文件
"""
    parser = optparse.OptionParser(usage)
    _, addresses = parser.parse_args() # _表示过滤掉第一个值
    print('==addr:',_,addresses) #==addr: {} ['111', '222', '333']
    if not addresses:# 如果没输入地址，打印help
        print (parser.format_help())
        parser.exit()

    def parse_address(addr):# 区分用户指定的主机和端口，默认为127.0.0.1
        if ':' not in addr:
            host = '127.0.0.1'
            port = addr
        else:
            host, port = addr.split(':', 1)
        if not port.isdigit():
            parser.error('Ports must be integers.')
        return host, int(port) # 返回（主机地址，端口）
    #return  parse_address(addresses)
    return map(parse_address, addresses)
class PoetryProtocol(Protocol): # handle
    poem = ''
    def dataReceived(self, data): # 接受数据
        self.poem += data
        # self.factory = PoetryClientFactory
        print('[%s] -----recv-----:[%s]' %(self.transport.getPeer(),len(self.poem)))

    def connectionLost(self, reason): # 连接关闭后执行此函数
        self.poemReceived(self.poem)
    def poemReceived(self, poem): #
        self.factory.poem_finished(poem)
class PoetryClientFactory(ClientFactory):#定义基类继承指定的类
    protocol = PoetryProtocol #绑定和server交互的类
    def __init__(self, callback):
        self.callback = callback
    def poem_finished(self, poem):
        self.callback(poem) #执行回调的那个函数
        #self.get_poem(poem)
def get_poetry(host, port, callback):
    """
    Download a poem from the given host and port and invoke
      callback(poem)
    when the poem is complete.
    """
    from twisted.internet import reactor
    factory = PoetryClientFactory(callback) # 实例化ProtryClientFactory 将传入的回调函数传入
    reactor.connectTCP(host, port, factory) # 链接
def poetry_main():
    addresses = parse_args() #((172.0.0.1,9000),(...))
    from twisted.internet import reactor
    poems = []
    def got_poem(poem):
        poems.append(poem)
        if len(poems) == len(addresses):
            reactor.stop()

    for address in addresses:#循环列表 获取地址和端口
        host, port = address
        get_poetry(host, port, got_poem) # 将got_poem函数链接函数
    reactor.run()

    print("main loop done...")
    #for poem in poems:
    #    Eprint poem

if __name__ == '__main__':
    poetry_main()