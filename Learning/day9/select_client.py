#python 3.5环境,解释器在linux需要改变
# -*- encoding:utf-8 -*-
#Auth  ChenJinPeng
import socket
cl=socket.socket()
cl.connect(("127.0.0.1",10000))
while True:
    data=input("==>>>:")
    cl.sendall(bytes(data,"utf8"))
    msg=cl.recv(1024)
    print(msg.decode())
