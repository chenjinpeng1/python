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
AUTH=True
while AUTH:
    print("用户配置文件在ftp_server 初始用户为chen 密码 123")
    User = input("user:").strip()
    if len(User) == 0:continue
    Passwd = input("Password:")
    MD5=hashlib.md5()
    MD5.update(bytes(Passwd,"utf8"))
    Passwd1=MD5.hexdigest() #将密码加密传入实例
    client.sendall(bytes("%s|%s"%(User,Passwd1),"utf8"))
    UP_RES = client.recv(1024)
    if UP_RES.decode() == "ACK_OK": # 如果密码正确
        print("login success")
        while True:
            try:
                User_input = input("cmd >>>:")
                if len(User_input) == 0:continue
                if User_input == "q":
                    AUTH=False
                    break
                User_input_split = User_input.split(" ") # 分割用户输入，判断执行什么操作
                FUNC=ftp_function.FtpClient(client)
                if hasattr(FUNC,User_input_split[0]):
                    func = getattr(FUNC,User_input_split[0])
                    func(User_input)
                else:
                    print("no function！")
            except Exception:
                print("error...")
                break
    else: # 密码错误 打印error
        print("login error!")

