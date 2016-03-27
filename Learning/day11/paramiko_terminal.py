import paramiko
ssh = paramiko.SSHClient() # 创建一个ssh会话

transport = paramiko.Transport(('localhost',22)) # 绑定链接主机
transport.start_client()
transport.auth_password("chen","chen27")

chan = transport.open_session() # 打开一个通道
chan.get_pty() # 获取一个终端
chan.invoke_shell() # 激活终端

while True:





