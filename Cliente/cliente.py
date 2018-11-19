import socket
import sys

### //crear coneccion
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect(('localhost', 9999))
###
def pedirIP(self):
	client_socket . send ("get ips")


#direccion = client_socket.recv(1024)
def recibeDirecciones(self,cadena):
	direcciones = cadena
	direcciones.split(",")
	return direcciones

def recorrerDirecciones(self,listaDireccion):
	direcciones = []
	direcciones = listaDireccion
	while ("respuesta sea 0"):
		#hacer split por espacio de Ip y puerto
		#hacer coneccion al servidor y esperar respuesta

def pedirDatos(self):
	cpu=raw_input("\ningrese el porcentaje de cpu a utilizar: ")
	memoria=raw_input("\ningrese el porcentaje de memoria a utilizar: ")
	mensaje=cpu+" "+memoria
	return mensaje

client_socket . send (mensaje)

