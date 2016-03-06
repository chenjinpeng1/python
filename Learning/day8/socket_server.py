#python 3.5环境,解释器在linux需要改变
# -*- encoding:utf-8 -*-
#Auth  ChenJinPeng
import socketserver
class MyTCPHandler(socketserver.BaseRequestHandler):
    # def __init__(self,count):
    #     self.count = count
    #     print(self.count)
    def handle(self):
        print("NEW:",self.client_address)
        while True:
            data = self.request.recv(1024)
            if not data:break
            print("client says:",data.decode())
            self.request.send(data)

if __name__=="__main__":
    HOST,PORT = "127.0.0.1",9999
    count = 0
    SERVER = socketserver.ThreadingTCPServer((HOST,PORT),MyTCPHandler)
    SERVER.serve_forever()