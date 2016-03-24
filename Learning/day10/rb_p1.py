#!/usr/bin/env python
import pika

# ######################### 生产者 #########################

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost')) #链接rabbitmq,默认端口
channel = connection.channel() # 创建一个隧道（服务端和客户端不能直接和rabbitmq直接通信,这样会在多交互的情况下容易乱）

channel.queue_declare(queue='hello')# 在隧道中创建和客户端交互的队列

channel.basic_publish(exchange='', # 讲消息发送到交换器，由交换器发送到指定的队列中，默认为交换器
                      routing_key='hello', # 向队列中发送数据
                      body='Hello World!') # 发送的数据内容
print(" [x] Sent 'Hello World!'")
connection.close()#关闭链接