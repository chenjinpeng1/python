#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                         type='direct')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

severities = sys.argv[1:] # 设定关键字，可以绑定多个关键字 空格分割
if not severities:
    sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0]) # 如果没有设定，则打印 退出
    sys.exit(1)

for severity in severities:
    channel.queue_bind(exchange='direct_logs',
                       queue=queue_name,
                       routing_key=severity) # 绑定关键字

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body)) # method.routing_key获取关键字信息

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()
'''
chen@chen:~/python/Learning/day10$ python3.5 rb_c2.py
Usage: rb_c2.py [info] [warning] [error]

chen@chen:~/python/Learning/day10$ python3.5 rb_c2.py info
 [*] Waiting for logs. To exit press CTRL+C
 [x] 'info':b'nihao'
 [x] 'info':b'Hello World!'
 [x] 'info':b'nihao'

chen@chen:~/python/Learning/day10$ python3.5 rb_c2.py info error
 [*] Waiting for logs. To exit press CTRL+C
 [x] 'info':b'nihao'
 [x] 'error':b'nihao'

'''