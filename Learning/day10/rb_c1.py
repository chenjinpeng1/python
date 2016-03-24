#!/usr/bin/env python
import pika

# ########################## 消费者 ##########################

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost')) # 客户段链接rabbitmq
channel = connection.channel() # 建立隧道

channel.queue_declare(queue='hello')# 客户端也建立一个队列（防止在客户端先启动的情况下，隧道中没有这个队列报错）

def callback(ch, method, properties, body): # 接受消息
    print(" [x] Received %r" % body)
    import time
    time.sleep(10)
    print("ok")
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(callback,#接收到消息后交给回调函数处理
                      queue='hello',#队列名称
                      no_ack=False) #在客户端接收到消息后断开链接了，队列里不在存储这个消息

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()# 启动 接收消息