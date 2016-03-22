#!/usr/bin/env python
# -*- coding:utf-8 -*-
#_*_coding:utf-8_*_
# This is the Twisted Fast Poetry Server, version 1.0

import optparse, os # optparse 类似于sys.argv 处理用户的输入的参数

from twisted.internet.protocol import ServerFactory, Protocol


def parse_args():
    usage = """usage: %prog [options] poetry-file

This is the Fast Poetry Server, Twisted edition.
Run it like this:

  python twisted_sendfile.py <path-to-poetry-file>

If you are in the base directory of the twisted-intro package,
you could run it like this:

  python twisted-server-1/fastpoetry.py poetry/ecstasy.txt

to serve up John Donne's Ecstasy, which I know you want to do.
"""

    parser = optparse.OptionParser(usage) #创建实例

    help = "The port to listen on. Default to a random available port."
    parser.add_option('--port', type='int', help=help)#设置参数，如果用户输入的是--port，规定必须为int

    help = "The interface to listen on. Default is localhost."
    parser.add_option('--iface', help=help, default='localhost')# 指定地址 默认localhost

    options, args = parser.parse_args() # 解析用户输入的参数
    print("--arg:",args) #解析用户除参数以为的字符串，这里为文件名
    print("-->",options) #解析用户输入的参数，类型为字典--> {'iface': 'localhost', 'port': 123}

    if len(args) != 1: #判断用户是否输入文件里，这里只能指定一个文件
        parser.error('Provide exactly one poetry file.')
    poetry_file = args[0]

    if not os.path.exists(args[0]): #判断文件是否存在
        parser.error('No such file: %s' % poetry_file)

    return options, poetry_file #返回用户输入的字符串


class PoetryProtocol(Protocol): #handle
    def connectionMade(self):
        self.transport.write(self.factory.poem)
        self.transport.loseConnection()


class PoetryFactory(ServerFactory): #基础类
    protocol = PoetryProtocol# 导入自定义的类，因为ServerFactory类里并没有做任何事情,所以我们只能亲历而为了
    def __init__(self, poem):#因为基类无法添加形参，自定义一个构造方法，让用户传入文件内容
        self.poem = poem

def main():
    options, poetry_file = parse_args()#options 用户传入的参数,poetry_file 文件名
    poem = open(poetry_file).read() # 打开文件
    factory = PoetryFactory(poem) # 初始化基类
    from twisted.internet import reactor # 导入事件分发器
    port = reactor.listenTCP(options.port or 9000, factory,
                             interface=options.iface) # 绑定端口，默认9000，interface 指定主机地址
    print ('Serving %s on %s.' % (poetry_file, port.getHost()))
    reactor.run()


if __name__ == '__main__':
    main()