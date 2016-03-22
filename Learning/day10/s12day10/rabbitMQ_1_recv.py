#!/usr/bin/env python
# -*- coding:utf-8 -*-
#_*_coding:utf-8_*_

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost'))
channel = connection.channel()


#You may ask why we declare the queue again ‒ we have already declared it in our previous code.
# We could avoid that if we were sure that the queue already exists. For example if send.py program
#was run before. But we're not yet sure which program to run first. In such cases it's a good
# practice to repeat declaring the queue in both programs.
#channel.queue_declare(queue='task_q',durable=True)

def callback(ch, method, properties, body):
    print("-->ch")
    print(" [x] Received %r" % body)
    ch.basic_ack(delivery_tag = method.delivery_tag)


channel.basic_consume(callback,
                      queue='task_q',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()