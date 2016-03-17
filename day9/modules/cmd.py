#/usr/bin/env python3
#-*-encoding:utf8-*-
import sys,os,paramiko,multiprocessing
import logging
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE)
import yaml

class cmd(object):
    def __init__(self,*args):
        self.group=args[0]
        self.command=args[2]
        file="%s/conf/conf.yaml"%(BASE)
        f=open(file)
        info=yaml.load(f)
        self.info = info
    @property
    def help(self):
        print('''
        CMD.run  -运行命令
        CMD.put -上传文件
        ''')
    @property
    def run(self):
        info = self.info
        try:
            if self.group in info.keys():
                for i in info[self.group]:
                    user=info[self.group][i]["user"]
                    passwd=info[self.group][i]["passwd"]
                    port=info[self.group][i]["port"]
                    SSH=multiprocessing.Process(target=self.SSH,args=(i,user,passwd,port))
                    SSH.start()
            elif self.group == "*":
                for i in info:
                    for ii in info[i]:
                        user=info[i][ii]["user"]
                        passwd=info[i][ii]["passwd"]
                        port=info[i][ii]["port"]
                        SSH=multiprocessing.Process(target=self.SSH,args=(ii,user,passwd,port))
                        SSH.start()

            else:
                print("Group no exit")
        except Exception as e:
            print("run异常错误")
            print(e)

    @property
    def put(self):
        info = self.info
        try:
            if self.group in info.keys():
                for i in info[self.group]:
                    user=info[self.group][i]["user"]
                    passwd=info[self.group][i]["passwd"]
                    port=info[self.group][i]["port"]
                    GET_FILE=multiprocessing.Process(target=self.PUT,args=(i,user,passwd,port))
                    GET_FILE.start()
            elif self.group == "*":
                for i in info:
                    for ii in info[i]:
                        user=info[i][ii]["user"]
                        passwd=info[i][ii]["passwd"]
                        port=info[i][ii]["port"]
                        GET_FILE=multiprocessing.Process(target=self.PUT,args=(ii,user,passwd,port))
                        GET_FILE.start()
        except Exception:
            print("get faild")

    @property
    def get(self):
        print("get")
    def SSH(self,host,user,passwd,port):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=host, port=port, username=user, password=passwd)
            stdin,stdout,stderr=ssh.exec_command(self.command)
            result = stdout.read()
            print("-------%s,OK!"%host)
            log_stdin="[%s] - {run}: [%s] {状态 %s} "%(host,self.command,"True")
            LOG_FILE="%s/var/sys.log"%BASE
            self.LOG(log_stdin,LOG_FILE)
            print(result.decode())
            ssh.close()
        except Exception as e:
            print("ssh Auth Faild，please check config file...")
            print(e)
            log_stdin="[%s] - {run}: [%s] {error info: %s} "%(host,self.command,e)
            LOG_FILE="%s/var/err.log"%BASE
            self.LOG(log_stdin,LOG_FILE)
    def PUT(self,host,user,passwd,port):
        try:
            path=self.command.split(",")
            remote_path=path[1]
            local_path=path[0]
            transport = paramiko.Transport((host,port))
            transport.connect(username=user,password=passwd)
            sftp = paramiko.SFTPClient.from_transport(transport)
            sftp.put(local_path, remote_path)
            print("-------%s,OK!"%host)
            log_stdin="[%s] - {put} - local_path [%s] remote_path:[%s] {状态 %s}"%(host,local_path,remote_path,"True")
            LOG_FILE="%s/var/sys.log"%BASE
            self.LOG(log_stdin,LOG_FILE)
            transport.close()
        except Exception as e:
            print("-------%s,Faild!"%host)
            print(e)
            log_stdin="[%s] - {run}: [%s] {error info: %s} "%(host,self.command,e)
            LOG_FILE="%s/var/err.log"%BASE
            self.LOG(log_stdin,LOG_FILE)
    def LOG(self,log,log_file):
        logger = logging.getLogger("sys-log")
        logger.setLevel(logging.DEBUG)
        # LOG_FILE="%s/var/sys.log"%BASE
        SSH_LOG=logging.FileHandler(log_file)
        SSH_LOG.setLevel(logging.INFO)
        formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        SSH_LOG.setFormatter(formatter)
        logger.addHandler(SSH_LOG)
        logger.info(log)

