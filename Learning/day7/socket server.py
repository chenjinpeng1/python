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
    print (str(client_data,'utf8'))
    conn.sendall(bytes('不要回答,不要回答,不要回答','utf8'))
    conn.close()

