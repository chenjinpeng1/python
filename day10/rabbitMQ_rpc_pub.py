#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pika,sys
import uuid # uuid模块在这里用作生产一串随机数当做返回的Q

class FibonacciRpcClient(object):
    def __init__(self): # 初始化配置
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
                host='localhost')) # 创建链接
        self.channel = self.connection.channel() # 建立隧道
        self.channel.exchange_declare(exchange="cmd",type="fanout")
        result = self.channel.queue_declare(exclusive=True) #生产随机Q ，链接断开后自动删除这个Q
        self.callback_queue = result.method.queue#获取随机Q
        # print(self.callback_queue)
        self.channel.basic_consume(self.on_response, no_ack=True,queue=self.callback_queue) #（订阅方），用于接收Q中的数据 【这里订阅方是写到构造方法了，初始化的时候就先订阅这个Q。】

    def on_response(self, ch, method, props, body): #回调方法
        print(body.decode())
        # res=" "
        # for i in body.decode().split("-"):
        #     res+=i
        # print(res)
        # self.response = res
    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4()) # 设定一个随机数
        print(self.corr_id)
        self.channel.basic_publish(exchange='cmd', # 交换器
                                   routing_key='', #client的 发布方的Q
                                   properties=pika.BasicProperties(
                                         reply_to = self.callback_queue, # reply_to 表示回调队列（Q）,客户端通过我传给你的这个Q给我返回消息，这个Q在初始化的时候已经给服务端了
                                         correlation_id = self.corr_id, # 传入UUID，服务端返回的时候带上UUID，客户端就能确认是自己本次要接收的消息了，（为什么加这个呢？个人理解：如果由N个客户端向rpcQ里发消息，都要求返回，或者你发了多个消息都要求返回，那返回来的结果你如何判断一一对应呢）
                                         ),# 持久化消息
                                   body=str(n))
        while self.response is None:
            self.connection.sleep(0) # 如果response的结果为NONE，就一直等待接收
        # return self.response

fibonacci_rpc = FibonacciRpcClient()
argv = sys.argv[1]
response = fibonacci_rpc.call(argv)