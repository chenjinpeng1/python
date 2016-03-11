#!/usr/bin/env python3.5
#-*- encoding:utf8 -*-
import sys,paramiko,configparser,pickle,threading
class MyServer(object):
	def __init__(self,hostname,port,username,passwd,command):
		self.hostname = hostname
		self.port = int(port)
		self.username = username
		self.passwd = passwd
		self.command = command
	def run(self):
		# 创建ssh对象
		ssh = paramiko.SSHClient()
		#允许连接不在know_hosts文件中的主机
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		# 连接服务器
		ssh.connect(hostname=self.hostname, port=self.port, username=self.username, password=self.passwd)
  
		# 执行命令
		stdin, stdout, stderr = ssh.exec_command(self.command)
		# 获取命令结果
		result = stdout.read()
		print("--------------------------%s------------------"%self.hostname)
		print (result.decode())
		# 关闭连接
		ssh.close()
if __name__ == "__main__":
	f = open("../log/hosts","rb")
	info= pickle.loads(f.read())
	f.close()
	while True:
		HOST_STR = input("添加你的主机信息:（格式为 host address,port,user,password）")
		if HOST_STR == "q":break
		HOST=HOST_STR.split(",")
		info[HOST[0]]=[HOST[1],HOST[2],HOST[3]]
		with open("../log/hosts","wb") as f:
			f.write(pickle.dumps(info))
			f.close()
	command = input("cmd>>>:")
	f = open("../log/hosts","rb")
	info= pickle.loads(f.read())
	f.close()
	for i in info.keys():
		A=MyServer(i,info[i][0],info[i][1],info[i][2],command)
		t = threading.Thread(target=A.run,args=[])
		t.start()
		#t.join(0.5)
