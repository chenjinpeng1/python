import select
import socket,time
from queue import Queue
server = socket.socket()
# server.setblocking(0)
server_address = ('localhost', 10000)
server.bind(server_address)
server.listen(5)
INPUT = [server,] # INPUT 在此的作用为 讲服务端的socket句柄加入到列表，让select初始监听服务端的socket句柄，如果客户端连接进来，则将客户端的socket句柄加入到input列表中
# print(INPUT)
OUTPUT=[]
message={}
while True:
    r,w,e=select.select(INPUT,OUTPUT,INPUT,1) # # r,w,e代表客户端的输入（sys.stdin，），输出(sys.stdout),异常错误(except)
    # time.sleep(2)
    # 读写分离
    #如果r有数据，读
    #读到数据了 将客户端的socket写入到w
    for i in r:
        if i == server: #循环r，如果没有客户端请求，for循环一直循环r,client请求server,则触发select,加入到INPUT列表中，判断是否是server被触发，是则接受客户端的请求
            conn,address = i.accept() #
            INPUT.append(conn)# 将客户端的socket加入到列表中监听
        #在此的效果为：
            '''
            message{
            　　conn1:[data1,data2,data3...] # conn1表示客户端1的socket地址
            　　conn2:[data1,data2,data3...] # conn2表示客户端2的socket地址
            }
            '''
        else: #如果被select触发的客户端过来的socket，则进行接收
            try:
                client_data=i.recv(1024)
                if len(client_data) != 0:
                    message[i] = Queue() # 将message字典的值设置为队列。
                    message[i].put(client_data) # 将接收的数据上传到队列中
                    OUTPUT.append(i) # 接收到客户端的数据了
            except Exception:
                INPUT.remove(i)

    for wi in w:
        wi.send(message[wi].get())
        OUTPUT.remove(wi) # 发送过去数据后移除OUTPUT里client的socket句柄，因为每次接收时候也会创建，如果不删除客户端断开后句柄也会存在，这样就慢慢就增大了内存
        message.pop(wi) # 移除message里的client的socket句柄
