import paramiko
import uuid
class haoroxy(object):
    def __init__(self):
        #初始化绑定账号密码主机端口信息
        self.host = "localhost"
        self.port = 22
        self.username = "chen"
        self.passwd = "chen27"
    def create_file(self):
        filename = str(uuid.uuid4())
        f = open(filename,"w")
        f.write("hello python!")
        f.close()
        return filename
    def update(self):
        # 上传文件时调用创建文件函数返回文件名
        filename = self.create_file()
        # 实例化sftp类
        Up = paramiko.SFTPClient.from_transport(self._transport)
        #上传文件
        Up.put(filename,'/home/chen/aabb.txt')
    def connect(self):
        #链接函数，启动后链接主机，定义一个公共的变量存储链接的通道
        transport = paramiko.Transport((self.host,self.port))
        transport.connect(username=self.username,password=self.passwd)
        self._transport = transport
    def close(self):
        #关闭链接
        self._transport.close()
    def rename(self):
        #更改名称函数
        #创立一个ssh链接
        ssh = paramiko.SSHClient()
        #绑定链接通道
        ssh._transport=self._transport
        #发送命令
        stdin,stdout,stderr = ssh.exec_command('mv /home/chen/aabb.txt /home/chen/11111.txt')
        ssh.close()
    def run(self):
        self.connect()
        self.update()
        self.rename()
        self.close()
aa = haoroxy()
aa.run()
'''
案例代码
'''
