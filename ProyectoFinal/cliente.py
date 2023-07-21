import socket
import threading
from login import *
from registro import *

host = "localhost"
puerto = 8001

servidor= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.connect((host, puerto))

#deberia hacer una clase cliente?

principal = PantallaMenu(servidor)
sala = SalaChat(principal, servidor)
