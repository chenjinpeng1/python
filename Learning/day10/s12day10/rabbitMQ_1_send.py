#!/usr/bin/env python
# -*- coding:utf-8 -*-
#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost'))
channel = connection.channel()

#声明queue
#hannel.queue_declare(queue='task_q',durable=True)

#n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
channel.basic_publish(exchange='',
                      routing_key='task_q',
                      body='Hello World! 35',
                      properties=pika.BasicProperties(
                        delivery_mode = 2, # make message persistent
                      )
                      )
print(" [x] Sent 'Hello World!'")
connection.close()