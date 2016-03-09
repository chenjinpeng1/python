#python 3.5环境，解释器在linux需要改变
#阅读手册查询readme文件
#作者：S12-陈金彭
import socketserver
class MyTcpServer(socketserver.BaseRequestHandler):
    def handle(self):
        print("NEW:",self.client_address)
        while True:
            try:
                Server_recv=self.request.recv(1024)
                if len(Server_recv) == 0:break
                print("client:",Server_recv.decode())
                self.request.send(Server_recv)
            except Exception:
                break
class STR():
    def start(self):
        HOST,PORT = "localhost",5007
        Server= socketserver.ThreadingTCPServer((HOST,PORT),MyTcpServer)
        Server.serve_forever()

    def stop(self):
        pass

from multiprocessing import Process
import os

# 子进程要执行的代码


