'''
    Servidor de dominio (Socket server using threads)
'''

# Imports
# ______________________________________________

import json
import socket
import sys
import thread

# ______________________________________________

HOST = '192.168.0.30'   # Server nickname
PORT_SERVER = 1024   # Arbitrary non-privileged port

# ______________________________________________

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

# Bind socket to local host and port
# ______________________________________________

try:
    serverSocket.bind((HOST, PORT_SERVER))
except socket.error as msg:
    print 'Bind failed. Error Code: ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

print 'Socket bind complete'

# Start listening on socket
# ______________________________________________
serverSocket.listen(10)
print 'Socket now listening'

# Recieve new connections
# ______________________________________________

list_connections = {}


def rec_ip(conn, addr):
    data = conn.recv(1025)
    reply = 'OK...' + data + ';'
    ip, port = data.split(' ')
    text = ''
    if ip != "get":
        list_connections[port] = ip
        print ip + ' ' + port + ' add :)'
    else:
        for item in list_connections:
            text += list_connections[item] + ' ' + item + ' , '
        conn.send(text)
        print text


while True:
    connServer, addrServer = serverSocket.accept()
    print 'Connected with ' + addrServer[0] + ':' + str(addrServer[1])
    thread.start_new_thread(rec_ip, (connServer, addrServer))

serverSocket.close()
