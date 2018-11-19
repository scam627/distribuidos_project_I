import socket
import sys

### //crear coneccion
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect(('localhost', 9999))
### Envia un mensaje solicitando las Ip en un string por parte del servidor de distribucion
def pedirIP(self):
	client_socket . send ("get ips")


#direccion = client_socket.recv(1024)
def recibeDirecciones(self,cadena):
	direcciones = cadena
	direcciones.split(",")
	return direcciones


def pedirDatos(self):
	cpu=raw_input("\ningrese el porcentaje de cpu a utilizar: ")
	memoria=raw_input("\ningrese el porcentaje de memoria a utilizar: ")
	mensaje=cpu+" "+memoria
	return mensaje

def recorrerDirecciones(self,listaDireccion):
	direcciones = []
	direcciones = listaDireccion
	mensaje = pedirDatos()
	respuesta = 0
	cont = 0
	while (respuesta == 0):
		#hacer split por espacio de Ip y puerto
		ip,port = direcciones[cont].split(" ")
		s1 = socket.socket()
		s1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		s1.connect((ip, port))
		client_socket . send (mensaje)
		#hacer coneccion al servidor y esperar respuesta



client_socket . close ()

if __name__ == '__main__':
	pedirIP() # envia peticion de ip a servidor de distribucion
	direccion = client_socket.recv(1024) # recibe un string con todas las direcciones por parte del servidor de distribucion
	lista = recibeDirecciones(direccion) #realiza la separacion de todas las direcciones y las devuelve en una lista
	recorrerDirecciones(lista)

