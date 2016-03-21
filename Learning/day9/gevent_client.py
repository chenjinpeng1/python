import socket
import threading
def run(mes):
	HOST = 'localhost'    # The remote host
	PORT = 10000           # The same port as used by the server
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((HOST, PORT))
	msg = bytes("aaaaa",encoding="utf8")
	s.sendall(msg)
	data = s.recv(1024)
	print("threading [%s],msg[%s]"%(mes,msg))
	s.close()

for i in range(2000):
	t = threading.Thread(target=run,args=[i,])
	t.start()
