#python 3.5环境,解释器在linux需要改变
# -*- encoding:utf-8 -*-
#Auth  ChenJinPeng
import sys,os,hashlib,time,pickle
import time
DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(DIR)
class FtpClient(object):
    def __init__(self,conection,User):
        self.connection = conection
        self.User=User
    def Md5(self,Str):
        MD5=hashlib.md5()
        MD5.update(Str)
        return MD5.hexdigest()

    def help(self,cmd):
        print("程序只在windows下测试过")
        print("dir-----查看当前目录文件(暂只试用windows)")
        print("pwd-----查看当前目录")
        print("cd-----切换到目录")
        print("rm-----删除操作")
        print("rename-----更改文件或者目录名操作")
        print("get-----下载文件")
        print("put-----上传文件")
        print("q-----退出")
        print("----进度条未完成")
        print("----多用户登陆为完成")
        print("----断点续传未完成")

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
        cd_error=self.connection.recv(50)
        print(cd_error.decode())
        if cd_error.decode() == "error":
            pass
        else:
            # cd_res=self.connection.recv(1024)
            print(cd_error.decode())

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

    def get1(self,func):
        self.connection.sendall(bytes(func,"utf8"))
        S_MES=self.connection.recv(50)
        GET_FILE_NAME=input("请输入下载的文件名称：")
        self.connection.sendall(bytes(GET_FILE_NAME,"utf8"))
        one_res=self.connection.recv(50)
        if one_res.decode() == "exit":
            c_file=open(GET_FILE_NAME,"wb")
            self.connection.sendall(bytes("touch_file_ok","utf8"))
            one_res2 = self.connection.recv(50).decode() # 获取下载文件总大小
            AUTH=True
        else:
            one_res1=self.connection.recv(50)
            print("服务器文件不存在")
            AUTH=False
        while AUTH:
            S_SIZE=os.path.getsize(GET_FILE_NAME)
            if int(S_SIZE) == int(one_res2):
                AUTH=False
                break
            one_res3=self.connection.recv(50).decode() # 获取文件第一行的长度
            self.connection.sendall(bytes("总长度收到","utf8"))
            res = b""
            default_len=0
            while default_len < int(one_res3):
                one_res4=self.connection.recv(1024)
                res+=one_res4
                default_len+=len(one_res4)
            else:
                c_file.write(res)
                c_file.flush()
                self.connection.sendall(bytes("下载完成","utf8"))

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
            NEXT_RES=self.connection.recv(50)
            if NEXT_RES.decode() == "file exit":
                print("发现文件存在")
                NEXT=input("文件存在，是否覆盖，yes覆盖,任意键退出")
                if NEXT == "yes":
                    self.connection.sendall(bytes("ok","utf8"))
                else:
                    self.connection.sendall(bytes("no","utf8"))
            fr = open(P_file,"rb")
            for i in fr.readlines():
                a=bytes(str(len(i)),"utf8")
                self.connection.sendall(a)   # 发送长度
                len_recv=self.connection.recv(50) # 接收长度回复信息
                if len_recv.decode() == "ok":
                    self.connection.sendall(i) # 发送数据
                    client_res=self.connection.recv(50) # 我知道你接收完了
                    self.connection.sendall(bytes("ok","utf8")) # OK 你发给我百分比吧
                    baifenbi=self.connection.recv(50) # 接收百分比
                    # print(baifenbi.decode())
                    self.jindutiao(baifenbi.decode())
            print("\n")
            break

    def jindutiao(self,num):
        a="###########"
        # for i in range(10):
        # b=a*num2
        sys.stdout.write("\r%s | %s"%(a,num))
        sys.stdout.flush()
        time.sleep(0.01)

    def get(self,func):
        info = {}
        self.connection.sendall(bytes(func,"utf8")) # 发送服务器做的操作
        FUNC_ACK=self.connection.recv(1024) # 接受Server调用方法的回复消息
        BEFORE_TRS=self.connection.recv(1024)
        if BEFORE_TRS.decode()=="before_trs_faild":
            print(BEFORE_TRS.decode())
            AFTER_INPUT=input("是否继续上次的传输 y/n :")
            self.connection.sendall(bytes(AFTER_INPUT,"utf8"))
            if AFTER_INPUT == "y":
                DICT_RECV=self.connection.recv(1024) # 接收字典信息
                info=pickle.loads(DICT_RECV)
                print(info)
                self.connection.sendall(bytes("DICT IS OK","utf8")) # 回复server
                FileName=info[self.User][0] # 文件名
                FileSize=info[self.User][1] # 总文件大小
                FileTELL=info[self.User][2] #文件指针
                FileStatus=info[self.User][3]#  文件状态
                CUR_FILE_SIZE=os.path.getsize(FileName) # 获取当前文件大小
                f=open(FileName,"ab")
                while int(CUR_FILE_SIZE)< int(FileSize):
                    #-----------------------
                    tmp_log = open("tmp.log","wb")
                    print("接受文件大小",CUR_FILE_SIZE)
                    print("总文件大小:",FileSize)
                    A=self.connection.recv(1024) # 第一次接收到的数据为发送的字节
                    self.connection.sendall(bytes("数据已接受","utf8"))
                    print("接收到数据",A)
                    TELL=self.connection.recv(1024) # 接受指针
                    print("接受到指针",TELL.decode())
                    f.write(A)
                    f.flush()
                    default_size = os.path.getsize(FileName)
                    print("文件大小",default_size)
                    info[self.User] = [FileName,FileSize,TELL.decode(),1] # [文件名，文件大小，指针]
                    print(info)
                    tmp_log.write(pickle.dumps(info))
                    print("写入指针")
                    tmp_log.flush()
                    tmp_log.close()
                    print("文件关闭")
                    self.connection.sendall(bytes("TELL_OK","utf8"))
                    CUR_FILE_SIZE=os.path.getsize(FileName) # 获取当前文件大小
                else:
                    print(info[self.User][-1])
                    info[self.User][-1]=0
                    print(info)
                    tmp_log=open("tmp.log","wb")
                    tmp_log.write(pickle.dumps(info))
                    print("chongxie~~~~~~~~~~~~~~~~~~~~~~")
                    tmp_log.close()
                    f = open("tmp.log","rb")
                    a=pickle.loads(f.read())
                    print(a)

        else:
            BEFORE_TRS_success_ack=self.connection.sendall("")
            print(BEFORE_TRS_success.decode())
            FileName = input("输入文件名：")
            self.connection.sendall(bytes(FileName,"utf8")) #传入Server文件名
            FileSize=self.connection.recv(1024) #接受文件大小,顺便判断文件是否存在
            print(FileSize.decode())
            if FileSize.decode() == "No File Exit": # 接受Server的判断文件是否存在
                print(FileSize.decode())
            else:
                f = open(FileName,"wb")
                self.connection.sendall(bytes("file size ok","utf8")) #告知服务端已收到文件大小
                print("进行查看现在文件大小")
                default_size = 0
                print(default_size)
                while default_size < int(FileSize.decode()): #接受文件大小小于文件总大小则循环
                    tmp_log = open("tmp.log","wb")
                    print("接受文件大小",default_size)
                    print("总文件大小:",int(FileSize.decode()))
                    A=self.connection.recv(1024) # 第一次接收到的数据为发送的字节
                    self.connection.sendall(bytes("数据已接受","utf8"))
                    print("接收到数据",A)
                    TELL=self.connection.recv(1024) # 接受指针
                    print("接受到指针",TELL.decode())
                    f.write(A)
                    f.flush()
                    print(os.getcwd())
                    default_size = os.path.getsize(FileName)
                    print("文件大小",default_size)
                    info[self.User] = [FileName,FileSize.decode(),TELL.decode(),1] # [文件名，文件大小，指针]
                    print(info)
                    tmp_log.write(pickle.dumps(info))
                    print("写入指针")
                    tmp_log.flush()
                    tmp_log.close()
                    print("文件关闭")
                    self.connection.sendall(bytes("TELL_OK","utf8"))
                else:
                    print(info[self.User][-1])
                    info[self.User][-1]=0
                    print(info)
                    tmp_log=open("tmp.log","wb")
                    tmp_log.write(pickle.dumps(info))
                    print("chongxie~~~~~~~~~~~~~~~~~~~~~~")
                    tmp_log.close()
                    f = open("tmp.log","rb")
                    a=pickle.loads(f.read())
                    print(a)


    def q(self,func):
        pass
