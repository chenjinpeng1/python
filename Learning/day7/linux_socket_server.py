#!/usr/bin/env python3.5
# Auth -chenjinpeng-
import socket,subprocess,time

Ip_port = ('127.0.0.1',9999)

Ftp = socket.socket()
Ftp.bind(Ip_port)
Ftp.listen(5) # 最大允许连5个？

while True:
        print ("server waiting...")
        conn,addr = Ftp.accept() #等待用户连接操作，addr表示获取客户端的ip和端口 conn表示生成实例

        while True:
                #try:
                client_data = conn.recv(1024) # 收客户端的消息 阻塞
                if not client_data:break # 如果接受不到消息 则退出循环
                cmd = client_data.decode().strip() # 将获取到的消息进行转码,将bytes转换为str用decode
                cmd_call = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE) # 将读取到的命令通过管道符进行输出到变量
                #Server_input = input("S >>>:").strip()
                cmd_result = cmd_call.stdout.read() # 获取命令的结果（此执行结果为bytes类型）
                if len(cmd_result) == 0:
                        cmd_result = b"cmd execution has no output!"
                cmd_len=bytes(str("cmd_long|%s"%str(len(cmd_result))),'utf8')  # 第一次首先将结果的长度发过去
                conn.sendall(cmd_len)
                ack=conn.recv(50) # 确认用户收到后回复。进行下一步操作
                if ack:
                        if ack.decode() == "ack":
                                conn.sendall(cmd_result) # 因为为bytes类型 直接发送
                else:break
        conn.close()