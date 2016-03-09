#python 3.5环境，解释器在linux需要改变
#阅读手册查询readme文件
#作者：S12-陈金彭
import socket
HOST,PORT=("localhost",5007)
client = socket.socket()
client.connect((HOST,PORT))
while True:
    User_input = input(">>>:")
    client.send(bytes(User_input,"utf8"))
    Server_recv=client.recv(1024)
    print("server:",Server_recv.decode())