#python 3.5环境,解释器在linux需要改变
# -*- encoding:utf-8 -*-
#Auth  ChenJinPeng
import sys,os
DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(DIR)
import ftp_function
import socket,hashlib

Ip_port = ('127.0.0.1',9999)
client=socket.socket()
client.connect(Ip_port)
while True:
    User = input("user:").strip()
    if len(User) == 0:continue
    Passwd = input("Password:")
    MD5=hashlib.md5()
    MD5.update(bytes(Passwd,"utf8"))
    Passwd1=MD5.hexdigest()
    print(Passwd1)
    client.sendall(bytes("%s|%s"%(User,Passwd1),"utf8"))
    UP_RES = client.recv(1024)
    print(UP_RES.decode())
    if UP_RES.decode() == "ACK_OK":
        print("login success")
        while True:
            # try:
            User_input = input("cmd >>>:")
            if len(User_input) == 0:continue
            if User_input == "q":break
            User_input_split = User_input.split(" ") # 分割用户输入，判断执行什么操作
            FUNC=ftp_function.FtpClient(client)
            if hasattr(FUNC,User_input_split[0]):
                func = getattr(FUNC,User_input_split[0])
                func(User_input)
            else:
                print("no function！")
            # except Exception:
            #     print("error...")
            #     break
    else:
        print("login error!")
        del MD5# 重新定义MD5变量 防止继续更新  坑中

