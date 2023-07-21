import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from tkinter.font import BOLD
from registro_design import *

class PantallaRegistro(RegisterDesign):
    def __init__(self, servidor):
        super().__init__(servidor)

    def registrar(self):
        datos = ["registrarUser", self.nombres.get(), self.apellidos.get(), self.usuario.get(),
              self.password.get(), self.edad.get(), self.genero]
        self.servidor.send(str(datos).encode())

        respuesta = self.servidor.recv(1024).decode("utf-8")
        recibido = eval(respuesta)
        if recibido[1]:
            messagebox.showinfo(message=str(recibido[0]), title="Registro")
            self.ventana.destroy()
            #Abre la ventana de los chats (chat predeterminado)
        else:
            messagebox.showerror(message=str(recibido[0]), title="Mensaje")
