import random

class Server:

    def __init__(self, ip, port):

        self.cpu = random.randint(1, 10) * 100
        self.memoria = random.randint(1, 10) * 100
        self.cpuDisp = self.cpu
        self.memoriaDisp = self.memoria

        self.ip = ip
        self.port = port


    def validarSolicitud(self, solicitud):

        cpu,memory = solicitud.split()
        cpu = int(cpu)
        memory = int(memory)
        if memory > self.memoriaDisp or cpu > self.cpuDisp:

            return 0:
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
