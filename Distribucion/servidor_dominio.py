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

HOST = '192.68.0.30'   # Server nickname
PORT = '1024'   # Arbitrary non-privileged port

# ______________________________________________

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

# Bind socket to local host and port
# _______________________________________________

try:
    serverSocket.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code: ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

print 'Socket bind complete'

# print "leer archivos"
# leer = json.loads(open('./src/data.json').read())
# print leer
# print leer[0]['ip']
