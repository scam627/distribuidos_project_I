import socket
#import sys
#import thread
import math
import threading

class Ip(threading.Thread):

    def __init__(self, ipPort, serverDistIP,serverDistPort):

        threading.Thread.__init__(self)
        self.ipPort = ipPort
        self.serverDistIP = serverDistIP#[ip1, ip2]
        self.serverDistPort  = serverDistPort#[port1, port2]
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def run(self):
        contador = 100000000
        while(True):
            if contador:
                contador -= 1
            else:
                contador = 100000000
                for i in range(len(self.serverDistPort)):
                    try:
                        self.client_socket.connect((self.serverDistIP[i], self.serverDistPort[i]))
                        self.client_socket.send(self.ipPort)
                        data = client_socket.recv(1024)
                        print(data)
                        self.client_socket.close()
                    except Exception as e:
                        print("no se puede realizar la conexion con: " +self.serverDistIP[i]+" "+str(self.serverDistPort[i]))
