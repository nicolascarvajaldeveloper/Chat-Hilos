import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
from tkinter import messagebox
from login_design import *
from registro import *
from salachat import *

class PantallaMenu(LoginDesign):
    def __init__(self, servidor):
        super().__init__(servidor)

    def verificar(self):
        datos=["verificarUser", self.usuario.get(), self.password.get()]
        self.servidor.send(str(datos).encode())

        respuesta = self.servidor.recv(1024).decode("utf-8")
        recibido = eval(respuesta)
        if recibido[1]:
            messagebox.showinfo(message=str(recibido[0]), title="Inicio de sesión")
            user = self.usuario.get()
            self.ventana.destroy()
            return user
            #Abre la ventana de los chats (chat predeterminado)
        else:
            messagebox.showerror(message=str(recibido[0]), title="Mensaje")

    def RegistrarUsuario(self):
        pantalla2 = PantallaRegistro(self.servidor).ventana.mainloop()
