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

    def md5_auth(self,passwd):
        A=hashlib.md5()
        A.update(bytes(passwd,"utf8"))
        return A.hexdigest()

    def MD5(self,Str):
        MD5_mes=hashlib.md5()
        MD5_mes.update(Str)
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
            self.func.sendall(bytes("error","utf8"))
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
        F_size=int(F_info[1])
        HOME=config["HOME"][self.name]
        print(os.getcwd())
        if os.path.isfile(F_name) is True:
            self.func.sendall(bytes("file exit","utf8"))
            F_E_R=self.func.recv(50)
            if F_E_R.decode() == "ok":
                os.remove(F_name)
                NEXT_RES=True
            else:
                self.func.sendall(bytes("no","utf8"))
                NEXT_RES=False
        else:
            self.func.sendall(bytes("ok","utf8"))
            NEXT_RES =True
        while NEXT_RES:
            wf = open(F_name,"wb")
            while True:
                File_info = os.stat(F_name)
                S_FILE_SIZE=File_info.st_size
                if S_FILE_SIZE == F_size:
                    NEXT_RES=False
                    break
                C_len=self.func.recv(50)
                self.func.sendall(bytes("ok","utf8"))
                res = b""
                res_len=0
                #-------------接受文件---------------
                while res_len < int(C_len.decode()):
                    W_file_b = self.func.recv(1024) # 接收数据
                    res+=W_file_b
                    res_len+=len(W_file_b)
                else:
                    wf.write(res)
                    wf.flush()
                    self.func.sendall(bytes("ok","utf8")) # OK 接收完了
                    zb_bfb=self.func.recv(50) # 好的
                    CUR_SIZE=os.path.getsize(F_name)
                    baifenbi = (int(CUR_SIZE) / int(F_size)) * 100
                    baifenbi_1 = float("%.2f"%baifenbi)
                    self.func.sendall(bytes("%s %s "%(baifenbi_1,"%"),"utf8")) # 发送百分比


    def get1(self,cmd):
        F_name = self.func.recv(50)
        F_E=os.path.isfile(F_name.decode())
        if F_E:
            self.func.sendall(bytes("exit","utf8"))
            one_res1=self.func.recv(50)
            if one_res1.decode() == "touch_file_ok":
                file_size=os.path.getsize(F_name.decode())
                self.func.sendall(bytes("%s"%file_size,"utf8"))# 发送文件总大小
                Auth = True
        else:
            self.func.sendall(bytes("no_exit","utf8"))
        if Auth:
            r_file = open(F_name,"rb")
            for i in r_file.readlines():
                a=bytes(str(len(i)),"utf8")
                self.func.sendall(a) # 发送长度
                one_res2 = self.func.recv(50) # 收取客户端返回收到长度的状态
                self.func.sendall(i)
                one_res3=self.func.recv(50)

    def get(self,cmd):
        Recv_Filename=self.func.recv(1024)   # 接受用户的下载的文件名
        print(Recv_Filename.decode())
        if os.path.isfile(Recv_Filename.decode()): # 判断服务器上文件名是否存在
            print("yes! file exit")
            FiteSize=os.path.getsize(Recv_Filename.decode()) # 判断文件大小
            self.func.sendall(bytes(str(FiteSize),"utf8"))# 发送文件大小
            ClientRecvSize=self.func.recv(1024) # Client存在时答复filesize
            with open(Recv_Filename,"rb")as R_file:
                while True:
                    R_file_msg=R_file.read(1024)
                    if len(R_file_msg) == 0:break
                    R_tell = R_file.tell()
                    Send_tell = "%s|%s"%(R_file_msg,R_tell)
                    self.func.sendall(bytes(Send_tell,"utf8")) # 发送数据+指针
                    Client_ack=self.func.recv()
        else:
            print("no file exit!!!")
            self.func.sendall(bytes("No File Exit","utf8"))





if __name__ == "__main__":
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
                S_USER=U_P_SPLIT[0]
                S_PASSWD=U_P_SPLIT[1]
                if S_USER in config["USER_PASS"]: # 判断用户是否存在
                    PASSWD=config["USER_PASS"][S_USER]
                    MD5_FUNC=S_FUNC("pass_md5",S_USER)
                    PASSWD_MD5=MD5_FUNC.md5_auth(PASSWD) # 将用户密码取出md5值
                    if S_PASSWD == PASSWD_MD5:
                        U_P_AUTH = conn.sendall(bytes("ACK_OK",'utf8'))
                        LOGIN_AUTH = True # 设置成功标志位
                        CUR_PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace("\\","/")
                        config["HOME"][S_USER]=''.join("%s/%s"%(CUR_PATH,S_USER))
                        config.write(open("ftp.config","w"))
                        os.chdir(config["HOME"][S_USER])
                        print("diaoyong hanshu")
                        break
                    else:U_P_AUTH2 = conn.sendall(bytes("ACK_ERROR",'utf8'))
                else:
                    U_P_AUTH2 = conn.sendall(bytes("ACK_ERROR",'utf8'))
                    # LOGIN_AUTH=None
                    # break
            except Exception:
                print("异常报错")
                break
    # ------------------login success------------------------------
        while LOGIN_AUTH:
            try:
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
                else:print('error......!')
            except Exception:
                AUTH=False
                break

