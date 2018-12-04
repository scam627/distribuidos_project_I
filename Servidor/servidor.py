from Ip import *
import thread
import socket
import sys
import threading

def imprimir():
    print("hola")

if __name__ == "__main__":

    actualizadorIp = Ip("localhost 8888", ['localhost','localhost'], [9997,9995])
    #actualizadorIp.sendIP()
    actualizadorIp.start()
    #thread.start_new_thread(actualizadorIp.sendIP,())
    #thread.start_new_thread(imprimir,())
