#python 3.5环境,解释器在linux需要改变
# -*- encoding:utf-8 -*-
#Auth  ChenJinPeng
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket

ip_port = ('127.0.0.1',9999)

sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)

while True:
    print ('server waiting...')
    conn,addr = sk.accept()
    client_data = conn.recv(1024)
    print (str(client_data,'utf-8'))
    conn.sendall(bytes('我是晨 我是晨 我是晨','utf-8'))
    while True:
        client_data = sk.recv(1024)
        conn.sendall(client_data)
    # conn.close()

