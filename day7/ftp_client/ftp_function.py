#python 3.5环境,解释器在linux需要改变
# -*- encoding:utf-8 -*-
#Auth  ChenJinPeng
import sys,os
DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(DIR)
class FtpClient(object):
    def __init__(self,conection):
        self.connection = conection
    def help(self):
        print("ls-----查看家目录文件")
        print("pwd-----查看当前目录")
        print("cd-----切换到目录")
        print("rm-----删除操作")
        print("rename-----更改文件或者目录名操作")
        print("get-----下载文件")
        print("put-----上传文件")
        print("q-----退出")
    def ls(self):
        print("ls")
        self.connection.sendall(bytes("dir".encode('utf8')))
        client_recv=self.connection.recv(1024)
        self.connection.sendall(bytes("ack".encode('utf8')))
        client_recv=self.connection.recv(1024)
        print(client_recv)
    def pwd(self):
        pass
    def cd(self):
        pass
    def rm(self):
        pass
    def rename(self):
        pass
    def get(self):
        pass
    def put(self):
        while True:
            P_file=input('输入上传的文件名：')
            self.connection.sendall(bytes(P_file,'utf8'))
            self.connection.recv(1024)
            while True:
                fr = open("ftp-client.py","r")
                for i in fr.readlines():
                    self.connection.sendall(i)

    def q(self):
        pass