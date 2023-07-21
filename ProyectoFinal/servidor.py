from BD.datos import *
import socket
import threading

host = "localhost"
puerto = 8001

#IF_INET protocolo IPv4, SOCK_STREAM protocolo de transporte TCP
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((host,puerto))

servidor.listen()
print("El servidor esta activo escuchando peticiones")

clientes = []

class Salas(threading.Thread):
    def __init__(self):
        pass

class Cliente(threading.Thread):
    def __init__(self, cliente, addr, name):
        super(Cliente, self).__init__()
        self.cli = cliente
        self.addr = addr
        self.name = name

    def run(self):
        while True:
            try:
                mensaje = self.cli.recv(2048)
                recibido = mensaje.decode("utf-8")
                recibido = eval(recibido)

                if recibido[0] == 'enviarMensaje':
                    mensaje_a_enviar = f"{self.name}: " + str(recibido[1])
                    broadcast(mensaje_a_enviar)

                elif recibido is str:
                    mensaje_a_enviar = f"{self.name}: " + str(recibido[1])
                    broadcast(mensaje_a_enviar)

                elif recibido[0] == 'exit':
                    print(clientes)
                    clientes.remove(self.cli)
                    print(clientes)
                    mensaje_a_enviar = f"{self.name} se ha desconectado"
                    broadcast(mensaje_a_enviar)
                    print(f"{self.addr[0]} se ha desconectado")
                    break

            except:
                continue
                #clientes.remove(self)
                #self.cli.close()


"""
Broadcast/difusion (El que envia los mensajes a todos los conectados en el chat)
    Para las multiples salas se tendra que enviar la lista de integrantes por sala
"""

def broadcast(mensaje):
    for cliente in clientes:
        cliente.send(mensaje.encode("utf-8"))

#Funcion que ACEPTARCONEXION (las escucha pues)
def aceptarConexion():
    while True:
        cli, addr = servidor.accept()
        print (f"{addr[0]} se ha conectado")

        salir=1

        while salir:
            recibido = cli.recv(1024)
            recibido = recibido.decode("utf-8")
            recibido = eval(recibido)

            """
            Al iniciar solo hay dos posibles mensajes que se pueden recibir:
                1. El registro en la base de datos
                2. El login para entrar en la sala de chat
            """
            if recibido[0]=="registrarUser":
                mensaje, bandera = insertar_datos(recibido[1],recibido[2],recibido[3],recibido[4],recibido[5],recibido[6])
                respuesta=[mensaje, bandera]
                cli.send(str(respuesta).encode())

            elif recibido[0]=="verificarUser":
                mensaje, bandera = validar_datos(recibido[1], recibido[2])
                #recibido[1] = username, recibido[2] = password
                respuesta=[mensaje, bandera]
                cli.send(str(respuesta).encode())
                if bandera == 1:
                    c = Cliente(cli, addr, recibido[1])
                    c.start()
                    clientes.append(cli)
                    broadcast(f"{recibido[1]} se ha unido a la sala\n")
                    salir=0



aceptarConexion()
