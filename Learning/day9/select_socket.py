import select
import socket
import sys
import queue

# Create a TCP/IP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)

# Bind the socket to the port
server_address = ('localhost', 10000)
# print (sys.stderr, 'starting up on %s port %s' % server_address)
server.bind(server_address)
# print(server_address)
# Listen for incoming connections
server.listen(5)
INPUT = [server,]
# print(INPUT)
OUTPUT=[]
while INPUT:
    r,w,e=select.select(INPUT,OUTPUT,INPUT)
    if INPUT:
        print(r)
    else:
        print("bbb")