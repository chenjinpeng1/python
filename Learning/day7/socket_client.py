#python 3.5环境,解释器在linux需要改变
# -*- encoding:utf-8 -*-
#Auth  ChenJinPeng
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
ip_port = ('127.0.0.1',9999)

sk = socket.socket()
sk.connect(ip_port)
while True:
    user_input = input('>>:'.strip())
    sk.sendall(bytes(user_input,'utf-8'))
    server_reply = sk.recv(1024)
    print (str(server_reply,'utf-8'))






