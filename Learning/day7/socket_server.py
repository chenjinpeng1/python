#python 3.5环境,解释器在linux需要改变
# -*- encoding:utf-8 -*-
#Auth  ChenJinPeng
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket

ip_port = ('127.0.0.1',9999)

sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)   # 最大允许连接5个？

while True:
    print ('server waiting...')
    conn,addr = sk.accept()  ##等待用户连接操作，addr表示获取客户端的ip和端口 conn表示生成实例
    while True:
        try:
            client_data = conn.recv(1024) # 阻塞状态 接受客户端的数据 1024代表字节
            # if not client_data.decode():break
            print (str(client_data,'utf-8'))
            A=input('>>>:')
            conn.sendall(bytes(bytes(A,'utf8')))
        except Exception:
            print("error")
            break

