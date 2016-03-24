#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

# make message persistent
channel.queue_declare(queue='hello1',durable=True)


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    # import time
    # time.sleep(10)
    # print ('ok')
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=2)

channel.basic_consume(callback,
                      queue='hello1',
                      no_ack=False)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()