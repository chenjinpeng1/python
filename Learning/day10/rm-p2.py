#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# make message persistent
channel.queue_declare(queue='hello1',durable=True)#durable定义持久化q（这里为什么不用之前的hello，是因为之前已经定义了hello为不持久化，所以你必须重新生成一个q，设置持久化或者删除之前的hello）

channel.basic_publish(exchange='',
                      routing_key='hello1',
                      body='Hello World88!',
                      properties=pika.BasicProperties(
                        delivery_mode=2, #持久化消息
                      ))
print(" [x] Sent 'Hello World2!'")
connection.close()