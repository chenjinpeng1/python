#python 3.5环境,解释器在linux需要改变
# -*- encoding:utf-8 -*-
#Auth  ChenJinPeng
import sys,os
DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(DIR)
import ftp_function
import socket


Ip_port = ('127.0.0.1',9999)
client=socket.socket()
client.connect(Ip_port)
while True:
    User_input = input(">>>:")
    if len(User_input) == 0:continue
    if User_input == "q":break
    FUNC=ftp_function.FtpClient(client)
    if hasattr(FUNC,User_input):
        func = getattr(FUNC,User_input)
        func()