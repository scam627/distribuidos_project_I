import socket
import sys

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect(('localhost', 9999))

cpu=raw_input("\ningrese el porcentaje de cpu a utilizar: ")
memoria=raw_input("\ningrese el porcentaje de memoria a utilizar: ")

mensaje=cpu+" "+memoria

client_socket . send (n1 + " " + n2 + " " + n3)
direccion = client_socket.recv(1024)

