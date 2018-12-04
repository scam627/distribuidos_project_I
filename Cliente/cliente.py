import socket
import sys

### //crear coneccion
sDist = socket.socket()
sDist.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sDist.connect(('localhost', 9989))
### Envia un mensaje solicitando las Ip en un string por parte del servidor de distribucion
def pedirIP():
	sDist . send ("get ips")


#direccion = client_socket.recv(1024)
def recibeDirecciones(cadena):
	#direcciones = cadena
	direcciones = cadena.split(",")
	return direcciones


def pedirDatos():
	cpu=raw_input("\ningrese el porcentaje de cpu a utilizar: ")
	memoria=raw_input("\ningrese el porcentaje de memoria a utilizar: ")
	mensaje=cpu+" "+memoria
	return mensaje

def recorrerDirecciones(listaDireccion):#retorna si se ejecuta el proceso o no, en caso de si, muestra donde.
	direcciones = []
	direcciones = listaDireccion
	#print type(direcciones[0])
	mensaje = pedirDatos()
	respuesta = '0'
	estado = "no se cumplio"
	#cont = 0
	for l in direcciones:
	#while (respuesta == '0'):
		#hacer split por espacio de Ip y puerto
		ip,port = l.split()
		print ip, port
		s1 = socket.socket()
		s1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		s1.connect((ip, int(port)))
		s1 . send (mensaje)
		respuesta = s1.recv(1024) # respuesta???
		#hacer coneccion al servidor y esperar respuesta
		if (respuesta == '1'):
			estado = "se cumplio"
			print "servicio ejecutado en: ",ip,port
			return estado
		#cont += 1
		s1.close()
	return estado





if __name__ == '__main__':
	pedirIP() # envia peticion de ip a servidor de distribucion
	direccion = sDist.recv(1024) # recibe un string con todas las direcciones por parte del servidor de distribucion
	sDist . close ()#funciona
	
	lista = recibeDirecciones(direccion) #realiza la separacion de todas las direcciones y las devuelve en una lista
	#print lista[1]
	
	mostrar = recorrerDirecciones(lista)
	if (mostrar == '0'):
		pass
		pass
		mostrar = recorrerDirecciones(lista)
	print mostrar
	