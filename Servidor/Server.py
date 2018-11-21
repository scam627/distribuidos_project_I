import random
import socket
#import sys
import thread
#import socket
import sys
import math
#import threading
import time

class Server:#(threading.Thread):

    def __init__(self, ip, port):

        #ing.Thread.__init__(self)

        self.ip = ip
        self.port = port

        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print 'Socket created'
        self.abrirConexion()

        self.cpu = random.randint(1, 10) * 100
        self.memoria = random.randint(1, 10) * 100

        print("cpu",str(self.cpu))
        print("memoria",str(self.memoria))

        self.cpuDisp = self.cpu
        self.memoriaDisp = self.memoria




    def abrirConexion(self):

        try:
            self.serversocket.bind((self.ip, self.port))
        except socket.error as msg:
            print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
            sys.exit()

        self.serversocket.listen(10)
        
    def validarSolicitud(self, solicitud):

        cpu,memory = solicitud.split()
        cpu = int(cpu)
        memory = int(memory)
        if memory > self.memoriaDisp or cpu > self.cpuDisp:

            return 0
        else:

            self.cpuDisp -= cpu
            self.memoriaDisp -= memory
            return 1

    def RecuperarRecursos(self, solicitud):

        cpu,memory = solicitud.split()
        cpu = int(cpu)
        memory = int(memory)

        self.cpuDisp += cpu
        self.memoriaDisp += memory

    def operar(conn, addr):

        data = conn.recv (1025)
        resp = self.validarSolicitud(data)
        #esperar un tiempo
        time.sleep(15)
        print("operado: " + str(resp))


        #envio la respuesta
        conn.sendall(str(resp))


    def run(self):

        while 1:
            print("wait to accept a connection - blocking call")
            conn, addr = self.serversocket.accept()
            print 'Connected with ' + addr[0] + ':' + str(addr[1])
            thread.start_new_thread (self.operar, (conn, addr))



server = Server("localhost", 9999)
server.run()
