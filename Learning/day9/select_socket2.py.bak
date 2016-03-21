#_*_coding:utf-8_*_
 
import select
import socket
import sys
import queue
 
# Create a TCP/IP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(False)
 
# Bind the socket to the port
server_address = ('localhost', 10000)
print(sys.stderr, 'starting up on %s port %s' % server_address)
server.bind(server_address)
server.listen(5)
 
inputs = [ server ]
 
outputs = [ ]
 
message_queues = {}
while inputs:
 
    print( '\nwaiting for the next event')
    readable, writable, exceptional = select.select(inputs, outputs, inputs)
    for s in readable:
 
        if s is server:
            connection, client_address = s.accept()
            print('new connection from', client_address)
            connection.setblocking(False)
            inputs.append(connection)
 
            message_queues[connection] = queue.Queue()
        else:
            data = s.recv(1024)
            if data:
                print(sys.stderr, 'received "%s" from %s' % (data, s.getpeername()) )
                message_queues[s].put(data)
                if s not in outputs:
                    outputs.append(s)
            else:
                print('closing', client_address, 'after reading no data')
                if s in outputs:
                    outputs.remove(s) 
                inputs.remove(s)    
                s.close()           
 
                del message_queues[s]
    for s in writable:
        try:
            next_msg = message_queues[s].get_nowait()
        except queue.Empty:
            print('output queue for', s.getpeername(), 'is empty')
            outputs.remove(s)
        else:
            print( 'sending "%s" to %s' % (next_msg, s.getpeername()))
            s.send(next_msg)
    for s in exceptional:
        print('handling exceptional condition for', s.getpeername() )
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()
        del message_queues[s]
