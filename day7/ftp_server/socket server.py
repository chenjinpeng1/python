#!/usr/bin/env python3.5
# Auth -chenjinpeng-
import socket,subprocess,time,hashlib,sys,os
import  configparser
config = configparser.ConfigParser()
config.read("ftp.config")

class S_FUNC(object):
    def __init__(self,func,name): # 服务端将socket连接传入
        self.func = func
        self.name = name

    def MD5(self,Str):
        MD5_mes=hashlib.md5()
        MD5_mes.update(bytes(Str,"utf8"))
        return MD5_mes.hexdigest()
    def dir(self,cmd):
        try:
            cmd_call = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE) # 将读取到的命令通过管道符进行输出到变量
            cmd_result = cmd_call.stdout.read()
            cmd_len = bytes("cmd_long|%s"%len(cmd_result),'utf8')
            self.func.send(cmd_len)
            ack = self.func.recv(1024)
            if ack.decode() == "ack":
                self.func.sendall(cmd_result)
        except Exception:
            print("ERROR COMMAND...")
    def pwd(self,cmd):
        try:
            cmd_call = subprocess.Popen("echo %cd%",shell=True,stdout=subprocess.PIPE) # 将读取到的命令通过管道符进行输出到变量
            cmd_result = cmd_call.stdout.read()
            cmd_len = bytes("cmd_long|%s"%len(cmd_result),'utf8')
            self.func.send(cmd_len)
            ack = self.func.recv(1024)
            if ack.decode() == "ack":
                self.func.sendall(cmd_result)
        except Exception:
            print("ERROR COMMAND...")
            self.func.sendall(bytes("ERROR COMMAND"))

    def cd(self,cmd):
        try:
            cmd_res=cmd.split(" ")
            cmd_res_split=cmd_res[1]
            print(cmd_res_split)
            cur_path=os.getcwd()
            os.chdir(cmd_res_split)
            new_path = os.getcwd()
            print(len(new_path))
            print(len(config["HOME"][self.name]))
            if len(str(new_path)) < len(config["HOME"][self.name]):
                print(new_path)
                print(config["HOME"][self.name])
                print("没有权限访问目录")
                os.chdir(cur_path)
                self.func.sendall(bytes("权限超出","utf8"))
            else:
                self.func.sendall(bytes("cd success","utf8"))
            # res = self.func.sendall(bytes)
        except Exception:
            print("error")
            pass
    def rm(self,cmd):
        try:
            cmd_res=cmd.split(" ")
            cmd_res_split=cmd_res[1]
            print(cmd_res_split)
            cmd_res_split_res=os.path.isdir(cmd_res_split)
            if cmd_res_split_res:
                os.rmdir(cmd_res_split)
            else:
                os.remove(cmd_res_split)
        except Exception:
            print("error")

    def rename(self,cmd):
        try:
            cmd_res=cmd.split()
            os.rename(cmd_res[1],cmd_res[2])
            self.func.sendall(bytes("执行成功",'utf8'))
        except Exception:
            self.func.sendall(bytes("error",'utf8'))

    def put(self,cmd):
        F_info_b=self.func.recv(50)
        F_info=F_info_b.decode().split(",")
        F_name=F_info[0]
        F_size=F_info[1]
        print(F_name,F_size)
        with open(F_name,"a") as f:f.close()
        F_name_recv=self.func.sendall(bytes("创建文件完毕","utf8"))
        with open(F_name,"a") as wf:
            while True:
                print("cccccd")
                W_file_b = self.func.recv(1024)
                W_file_split=W_file_b.decode().split(",")
                print(W_file_split)
                W_file=W_file_split[0]
                F_MD5=self.MD5(W_file)
                print(F_MD5)
                print(W_file_split[1])
                if F_MD5==W_file_split[1]:
                    print("aaaaaa")
                    self.func.sendall(bytes("MD5校验成功","utf8"))
                    wf.write(W_file)
                    print("bbbbb")








Ip_port = ('127.0.0.1',9999)

Ftp = socket.socket()
Ftp.bind(Ip_port)
Ftp.listen(5) # 最大允许连5个？


while True:
    print("server waiting...")
    conn,addr = Ftp.accept()
    AUTH=True
    while AUTH:
        try:
            U_P_recv = conn.recv(1024) # 接收用户输入的账号密码
            if len(U_P_recv) == 0:break
            U_P_SPLIT=U_P_recv.decode().split("|") # 转换为列表
            PASSWD=config["USER_PASS"][U_P_SPLIT[0]]
            MD5=hashlib.md5()
            MD5.update(bytes(PASSWD,"utf8"))
            PASSWD=MD5.hexdigest()
            if U_P_SPLIT[0] in config["USER_PASS"] and U_P_SPLIT[1] == PASSWD: # 判断用户密码
                U_P_AUTH = conn.send(bytes("ACK_OK",'utf8'))
                LOGIN_AUTH = True # 设置成功标志位
                os.chdir('C:/Users/chen/PycharmProjects/python/day7/chen')
                print(os.getcwd())
                break
            else:
                U_P_AUTH = conn.send(bytes("ACK_ERROR",'utf8'))
                break
        except Exception:
            break
# ------------------login success------------------------------
    while LOGIN_AUTH:
        # try:
        MES_INFO = conn.recv(1024) # 第一步收取用户传来的命令
        if len(MES_INFO) == 0:
            AUTH=False
            break
        MES_ACK = conn.send(bytes("ack","utf8")) # 发送ack回执
        MES_INFO_SPLIT=MES_INFO.decode().split(" ")
        FUNC=S_FUNC(conn,U_P_SPLIT[0]) # 实例化Server的类，反射调用方法
        if hasattr(FUNC,MES_INFO_SPLIT[0]):
            func = getattr(FUNC,MES_INFO_SPLIT[0])
            func(MES_INFO.decode())
        else:print('error......')
        # except Exception:
        #     AUTH=False
        #     break

