#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pika,subprocess
import time
connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost')) # 链接主机
channel = connection.channel() # 创建隧道
channel.exchange_declare(exchange="cmd",type="fanout")
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue
channel.queue_bind(exchange="cmd",queue=queue_name)
# channel.queue_declare(queue='rpc_queue') #创建q名称

def fib(CMD): # 计算函数
    cmd=subprocess.Popen(CMD,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    result="-%s====%s%s"%("1","\n",cmd.stdout.read().decode())
    return  result
#服务端接收到客户端的命令后进行计算。计算完在通过初始定义的q返回
def on_request(ch, method, props, body): # 接收客户端的数据
    # print("props",props.reply_to) # props 接收到的是client生成的随机Q
    # print("reply_to",props.correlation_id) # 客户端通过UUID生产的随机Q
    print(" [.] fib(%s)" % body)
    response = fib(body) # 调用计算函数
    # 向client发送计算完的数据（发布方）
    ch.basic_publish(exchange='', # 使用默认交换器
                     routing_key=props.reply_to, #client自动生成的随机q（返回q）
                     properties=pika.BasicProperties(correlation_id =props.correlation_id),body=str(response)) #props.correlation_id 表示客户端发送的另一个随机Q
    # ch.basic_ack(delivery_tag = method.delivery_tag) # 消息持久化

channel.basic_qos(prefetch_count=1) #公平分发（表示如果我这个数据没处理完，将不在接收新的数据）
channel.basic_consume(on_request, queue=queue_name,no_ack=True) # 接收rpc队列中的数据（订阅方），on_request表示回调函数CALLBACK，回调函数中处理了数据，又充当了发布方

print(" [x] Awaiting RPC requests") # 打印开始接收消息
channel.start_consuming() # 开始接收