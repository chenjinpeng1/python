#!/usr/bin/env python3.5
# Auth -chenjinpeng-
import socket,subprocess,time,hashlib,sys,os
import  configparser,pickle
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
        '''
        TMP_LOG_tmp 取出用户主目录
        TMP_LOG 取出主目录下的记录断电续传的文件
        R_tmplog pickle 读取出字典
        :param cmd:
        :return:
        '''
        TMP_LOG_tmp=config["HOME"][self.name]  # 取出用户的主目录
        TMP_LOG=('%s/%s'%(TMP_LOG_tmp,'tmp.log')) # 定义用户的临时文件位置，避免用户任意切换目录后打不开文件
        print("用户的断点传输配置文件为：",TMP_LOG)
        tmplog=open(TMP_LOG,"rb") # 用户下载前先读取记录下载成功失败的记录文件
        R_tmplog=pickle.loads(tmplog.read()) # pickle读取服务端的记录文件
        tmplog.close()
        print("记录断点续传的字典信息，格式为 文件名,文件大小,传输的大小,断点记录值0表示成功",R_tmplog)
        if R_tmplog[self.name][-1]!=0: # 判断文件成功失败，0代表成功
            self.func.sendall(bytes("before_trs_faild","utf8")) # 向client发送失败的消息
            AFTER_RECV=self.func.recv(1024) # 接受client的选择
            print("客户端选择继续下载或者重新下载",AFTER_RECV.decode()) # 打印客户端的选择
            if AFTER_RECV.decode()=="y": # 选择继续下载
                print(R_tmplog)
                TRS_DICT=pickle.dumps(R_tmplog)
                self.func.sendall(TRS_DICT) # 向client发送字典信息
                DICT_STATUS=self.func.recv(1024) #接收client的字典信息回复
                AFTER_TRS_PATH=os.getcwd()
                ENTER_TRS_FILE="%s"%(R_tmplog[self.name][0]) # 客户端上次断点文件的文件位置（次于主目录后开始记录）
                os.chdir(TMP_LOG_tmp) # 先切到根目录在进行传输数据
                with open(ENTER_TRS_FILE,"rb") as R_Enter:
                    R_Enter.seek(R_tmplog[self.name][-2])   # -2 表示上次读取的指针位置
                    while True:
                        R_file_msg=R_Enter.read(1024)
                        print("读取数据中")
                        if len(R_file_msg) == 0:break
                        R_tell = R_Enter.tell()
                        # print("发送数据",R_file_msg)
                        self.func.sendall(R_file_msg) # 发送数据
                        MSGRETURN=self.func.recv(1024)
                        print("client 接受数据的返回")
                        self.func.sendall(bytes(str(R_tell),"utf8"))
                        print("发送指针",R_tell)
                        Client_ack=self.func.recv(1024)
                        print("client接受指针的回复")
                        WRITE_TMP=open(TMP_LOG,"wb")
                        R_tmplog[self.name] = [R_tmplog[self.name][0],R_tmplog[self.name][1],R_tell,1]
                        WRITE_TMP.write(pickle.dumps(R_tmplog))
                        WRITE_TMP.flush()
                        print("写入记录指针的文件")
                        WRITE_TMP.close()
                        print(R_tmplog)
                    if R_tmplog[self.name][1]==R_tmplog[self.name][2]:
                        R_tmplog[self.name][-1]=0
                        WRITE_TMP=open(TMP_LOG,"wb")
                        WRITE_TMP.write(pickle.dumps(R_tmplog))
                        WRITE_TMP.flush()
                        print("文件大小相等，写入完成")
                        WRITE_TMP.close()
                        f = open(TMP_LOG,"rb")
                        a=pickle.loads(f.read())
                        print(a)
                        os.chdir(AFTER_TRS_PATH)
                    else:
                        pass
            else:
                R_tmplog[self.name] = ["None","0","0",0]
                WRITE_TMP=open(TMP_LOG,"wb")
                WRITE_TMP.write(pickle.dumps(R_tmplog))
                WRITE_TMP.flush()
                print("重新写入")
                WRITE_TMP.close()
        else:
            print("oooooo")
            self.func.sendall(bytes("before_trs_success","utf8"))
            print("发送成功")
            Recv_Filename=self.func.recv(1024)   # 接受用户的下载的文件名
            print(Recv_Filename.decode())
            print(os.getcwd())
            CUR_File_PATH1=os.getcwd()
            CUR_File_PATH="%s/%s"%(CUR_File_PATH1,Recv_Filename.decode())
            print(config["HOME"][self.name])
            RE_FILE_PATH=CUR_File_PATH.replace("\\","/").replace(config["HOME"][self.name],"")[1:]
            print(RE_FILE_PATH)
            if os.path.isfile(Recv_Filename.decode()): # 判断服务器上文件名是否存在
                print("yes! file exit")
                FiteSize=os.path.getsize(Recv_Filename.decode()) # 判断文件大小
                self.func.sendall(bytes(str(FiteSize),"utf8"))# 发送文件大小
                ClientRecvSize=self.func.recv(1024) # Client存在时答复filesize
                print("Client Recv Size:",ClientRecvSize.decode())
                info = {}
                with open(Recv_Filename.decode(),"rb")as R_file:
                    while True:
                        R_file_msg=R_file.read(1024)
                        print("读取数据中")
                        if len(R_file_msg) == 0:break
                        R_tell = R_file.tell()
                        print(R_tell)
                        print("发送数据")
                        self.func.sendall(R_file_msg) # 发送数据
                        MSGRETURN=self.func.recv(1024)
                        print("client 接受数据的返回")
                        self.func.sendall(bytes(str(R_tell),"utf8"))
                        print("发送指针",R_tell)
                        Client_ack=self.func.recv(1024)
                        print("client接受指针的回复")
                        # File_PATH="%s%s"%(RE_FILE_PATH,Recv_Filename.decode())
                        WRITE_TMP=open(TMP_LOG,"wb")
                        info[self.name] = [RE_FILE_PATH,FiteSize,R_tell,1]
                        WRITE_TMP.write(pickle.dumps(info))
                        WRITE_TMP.flush()
                        print("写入记录指针的文件")
                        WRITE_TMP.close()
                        print(info)
                    if info[self.name][1]==FiteSize:
                        info[self.name][-1]=0
                        WRITE_TMP=open(TMP_LOG,"wb")
                        WRITE_TMP.write(pickle.dumps(info))
                        WRITE_TMP.flush()
                        print("文件大小相等，写入完成")
                        WRITE_TMP.close()
                        f = open(TMP_LOG,"rb")
                        a=pickle.loads(f.read())
                        print(a)
                    else:
                        pass
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
                        # print(CUR_PATH)
                        config["HOME"][S_USER]=''.join("%s/%s"%(CUR_PATH,S_USER))
                        config.write(open("ftp.config","w"))
                        os.chdir(config["HOME"][S_USER])
                        # print("diaoyong hanshu")
                        break
                    else:U_P_AUTH2 = conn.sendall(bytes("ACK_ERROR",'utf8'))
                else:
                    U_P_AUTH2 = conn.sendall(bytes("ACK_ERROR",'utf8'))
                    LOGIN_AUTH=False
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
                MES_ACK = conn.sendall(bytes("ack","utf8")) # 发送ack回执
                MES_INFO_SPLIT=MES_INFO.decode().split(" ")
                FUNC=S_FUNC(conn,U_P_SPLIT[0]) # 实例化Server的类，反射调用方法
                if hasattr(FUNC,MES_INFO_SPLIT[0]):
                    func = getattr(FUNC,MES_INFO_SPLIT[0])
                    # print("diaoyong func")
                    func(MES_INFO.decode())
                else:print('error......!')
            except Exception:
                AUTH=False
                break

