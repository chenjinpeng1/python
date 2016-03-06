#python 3.5环境,解释器在linux需要改变
# -*- encoding:utf-8 -*-
#Auth  ChenJinPeng
import socket

IP_ADDR=("127.0.0.1",9999)
CLIENT=socket.socket()
CLIENT.connect(IP_ADDR)
while True:
    C_SAYS = input(">>>:").strip()
    if len(C_SAYS) == 0:continue
    CLIENT.sendall(bytes(C_SAYS,"utf8"))
    CLIENT_reply = CLIENT.recv(1024)
    print("Server replay:",CLIENT_reply.decode())
CLIENT.close()