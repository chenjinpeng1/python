
#!/usr/bin/env python3.5
# - Auth chenjinpeng -

import socket
Ip_port = ('127.0.0.1',9999)

Client = socket.socket()
Client.connect(Ip_port)

#Client.sendall(bytes('请求占领地球','utf8'))
#Server_reply = Client.recv(1024)
#print (str(Server_reply,'utf8'))
while True:
        User_input = input(">>>:").strip()
        if len(User_input) == 0:continue
        if User_input == 'q':break

        Client.sendall(bytes(User_input,'utf8'))
        cmd_result_msg=Client.recv(100) # 第一次接受的是服务器发来的字符串长度
        cmd_result_len=str(cmd_result_msg.decode()) # 转换str
        cmd_result_len_result=cmd_result_len.split("|") # 分割列表
        if cmd_result_len_result[0] == "cmd_long": # 判断是否是分割的数据
                cmd_result_size = int(cmd_result_len_result[1]) # 取出返回的字符长度
        else:
                print ("error !")
                continue
        Client.sendall(bytes("ack",'utf8')) # 发送ack确认消息，服务端正式开始发送数据
        cmd_len_default=0 # 定义输出读取的字符长度
        res = '' # 定义空字符 循环增加每次读取的字符
        while cmd_len_default < cmd_result_size: # 判断字符是否读完。如果小于服务端发送过来的长度，则代表没接收完
                Server_reply = Client.recv(500) # 每次收取500字符
                cmd_len_default+=len(Server_reply) # 每次字符长度加上已经读取的字符长度
                res += str(Server_reply.decode()) # 读取过的字符相加，循环完毕后统一打印
        else:
                print (res)
                print ("-------last time-----")
Client.close()