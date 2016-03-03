#python 3.5环境,解释器在linux需要改变
# -*- encoding:utf-8 -*-
#Auth  ChenJinPeng
import sys,os,hashlib
DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(DIR)
class FtpClient(object):
    def __init__(self,conection):
        self.connection = conection
    def Md5(self,Str):
        MD5=hashlib.md5()
        MD5.update(bytes(Str,"utf8"))
        return MD5.hexdigest()
    def help(self,cmd):
        print("dir-----查看家目录文件")
        print("pwd-----查看当前目录")
        print("cd-----切换到目录")
        print("rm-----删除操作")
        print("rename-----更改文件或者目录名操作")
        print("get-----下载文件")
        print("put-----上传文件")
        print("q-----退出")
    def dir(self,func):
        # SYSTEM=sys.platform # 判断系统为 什么系统
        try:
            self.connection.sendall(bytes(func.encode('utf8'))) # 发送dir命令
            client_recv=self.connection.recv(1024) # 接收ack回执
            # self.connection.sendall(bytes("ack".encode('utf8')))
            client_recv=self.connection.recv(1024) # 接收Server返回的长度
            client_recv_split = client_recv.decode().split("|")
            if client_recv_split[0] == "cmd_long":
                self.connection.sendall(bytes("ack","utf8"))
                client_recv_len=int(client_recv_split[1])
            Default_res=b""
            Default_len = 0
            while Default_len < client_recv_len:
                S_server_msg = self.connection.recv(1024)
                Default_res+=S_server_msg
                Default_len+=len(S_server_msg)
            else:
                print(Default_res.decode("gb2312"))  # 对于windows的编码转换为gb2312
                print("-----last time-----")
        except Exception:
            print("ERROR COMMAND...")



    def pwd(self,func):
        print("pwd")
        try:
            self.connection.sendall(bytes(func.encode('utf8'))) # 发送dir命令
            client_recv=self.connection.recv(1024) # 接收ack回执
            # self.connection.sendall(bytes("ack".encode('utf8')))
            client_recv=self.connection.recv(1024) # 接收Server返回的长度
            client_recv_split = client_recv.decode().split("|")
            if client_recv_split[0] == "cmd_long":
                self.connection.sendall(bytes("ack","utf8"))
                client_recv_len=int(client_recv_split[1])
            Default_res=b""
            Default_len = 0
            while Default_len < client_recv_len:
                S_server_msg = self.connection.recv(1024)
                Default_res+=S_server_msg
                Default_len+=len(S_server_msg)
            else:
                print(Default_res.decode("gb2312"))  # 对于windows的编码转换为gb2312
                print("-----last time-----")
        except Exception:
            print("ERROR COMMAND...")
    def cd(self,func):
        self.connection.sendall(bytes(func,"utf8"))
        ack_res=self.connection.recv(1024)
        cd_res=self.connection.recv(1024)
        print(cd_res.decode())
    def rm(self,func):
        print("rm")
        self.connection.sendall(bytes(func,'utf8'))
        self.connection.recv(1024)
    def rename(self,func):
        print("rename")
        self.connection.sendall(bytes(func,"utf8"))
        rename_recv=self.connection.recv(1024)
        rename_res=self.connection.recv(1024)
        print(rename_res.decode())
    def get(self):
        pass
    def put(self,func):
        self.connection.sendall(bytes(func,"utf8"))
        self.connection.recv(50)
        while True:
            P_file=input('输入上传的文件名：').strip()
            F_EXIT=os.path.isfile(P_file)
            if F_EXIT is not True:
                print("文件不存在")
                continue
            print("---------------------")
            File_info = os.stat(P_file)
            File_size=File_info.st_size
            print(File_size)
            print("文件大小为：%s"%File_size)
            self.connection.sendall(bytes("%s,%s"%(P_file,File_size),'utf8'))
            ack_mes=self.connection.recv(1024)
            print("%s - 确认消息"%ack_mes.decode())
            fr = open(P_file,"r")
            for i in fr.readlines():
                MD5=self.Md5(i)
                print(MD5)
                print(i)
                self.connection.sendall(bytes("%s,%s"%(i,MD5),"utf8"))
                MD5_RES=self.connection.recv(50)
                if MD5_RES.decode() != "MD5校验成功":
                    print(MD5_RES.decode())
                    break


    def q(self):
        pass