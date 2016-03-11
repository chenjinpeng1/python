#!/usr/bin/env python3.5
#-*- encoding:utf8 -*-
import sys,paramiko,configparser,pickle,os
from multiprocessing import Process
class MyServer(object):
	def __init__(self,hostname,port,username,passwd,command):
		self.hostname = hostname
		self.port = int(port)
		self.username = username
		self.passwd = passwd
		self.command = command
	def s(self):
		self.run()
	def run(self):
		# 创建ssh对象
		ssh = paramiko.SSHClient()
		#允许连接不在know_hosts文件中的主机
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		# 连接服务器
		ssh.connect(hostname=self.hostname, port=self.port, username=self.username, password=self.passwd)
		print('conection')
		# 执行命令
		stdin, stdout, stderr = ssh.exec_command(self.command)
		# 获取命令结果
		result = stdout.read()
		print("--------------------------%s------------------"%self.hostname)
		print (os.getpid())
		print (result.decode())
		# 关闭连接
		ssh.close()
if __name__ == "__main__":
	try:
		options=["添加主机群组",""]
		f = open("../log/hosts","rb")
		info= pickle.loads(f.read())
		f.close()
		ADD_HOST=True
		GROUP_HOST=input("设定你的主机组名称：")
		if GROUP_HOST == "q":ADD_HOST=False
		while ADD_HOST:
			HOST_STR = input("添加你的主机信息:（格式为 host address,port,user,password）")
			if HOST_STR == "q":break
			HOST=HOST_STR.split(",")
			info[GROUP_HOST][HOST[0]]=[HOST[1],HOST[2],HOST[3]]
			with open("../log/hosts","wb") as f:
				f.write(pickle.dumps(info))
				f.flush()
				f.close()
		#command = input("cmd>>>:")
		f = open("../log/hosts","rb") # 重新读取主机信息
		info= pickle.loads(f.read())
		f.close()
		Grep_input=sys.argv[1:]
		INPUT = []
		for i in Grep_input:
			INPUT.append(i.replace("-",""))
		print(INPUT)
		if "-g" in Grep_input:
			Group=Grep_input[Grep_input.index("-g")+1]
			print ("group:",list(info[Group].keys()))
			for i in list(info[Group].keys()):
				print("实例化信息:",i,info[Group][i][0],info[Group][i][1],"密码",sys.argv[4])
				A=MyServer(i,info[Group][i][0],info[Group][i][1],info[Group][i][2],Grep_input[3])
				print ("实例化完成",A)
				t = Process(target=A.run,args=[])
				print ("线程启动OK！")
				t.start()
			t.join(0.5)
		else:
			print ("格式错误")
	except Exception as e:
		print ("""
 -g 指定主机组 -s shell"""
)
		print(e)
