import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
from tkinter import messagebox
from salachat_design import *
import threading

class SalaChat(SalaChatDesign):
    def __init__(self, user, servidor):
        self.username = user
        self.servidor = servidor
        super().__init__()

    def enviarMensaje(self):
        mensaje_a_enviar = ["enviarMensaje", f"{self.mensaje.get('1.0','end')}"]
        self.servidor.send(str(mensaje_a_enviar).encode("utf-8"))
        self.mensaje.delete("1.0","end")

    def recibirMensaje(self):
        while self.running:
            try:
                respuesta = self.servidor.recv(1024).decode("utf-8")
                if self.gui_done:
                    print("mensaje recibido", respuesta)
                    self.areaTexto.config(state="normal")
                    self.areaTexto.insert("end",respuesta)
                    self.areaTexto.yview("end")
                    self.areaTexto.config(state="disabled")

            except ConnectionAbortedError:
                break
            except:
                print("error")
                self.servidor.close()

    def exit(self):
        mensaje= ["exit"]
        self.servidor.send(str(mensaje).encode("utf-8"))
        self.running = False
        self.ventana.destroy()
        self.servidor.close()
        exit(0)

    def crearSala(self):
        pass

    def entrarSala(self):
        pass

    def salirSala(self):
        pass

    def mostrarLista(self):
        pass

    def deleteSala(self):
        pass

    def showUsers(self):
        pass

    def privateMessage(self):
        pass
