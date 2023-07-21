import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from tkinter.font import BOLD

class LoginDesign:
    def __init__(self, servidor):
        self.servidor = servidor
        self.ventana = tk.Tk()
        self.ventana.title("Login")
        self.ventana.geometry("800x500")
        self.ventana.config(bg = "lightblue")
        self.ventana.resizable(width = 0, height = 0)

        #En caso de poner logo
        #logo= PhotoImage(file="nombre.gif")
        #logo=image.subsample(2,2)
        #logo=label(image=image)
        #label.pack()

        #FRAME derecha
        frame_logo = tk.Frame(self.ventana, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10, bg="lightblue")
        frame_logo.pack(side = "left", expand=tk.NO, fill=tk.BOTH)

        #frame "formulario"
        frame_form = tk.Frame(self.ventana, bd=0, width=400, relief=tk.SOLID, bg="white")
        frame_form.pack(side= "right", expand=tk.YES, fill=tk.BOTH)

        #frame de la parte de arriba, para que no entendi XD
        frame_form_top = tk.Frame(frame_form, height = 50, bd=0, relief=tk.SOLID, bg="white")
        frame_form_top.pack(side = "top", fill =tk.X)
        title = tk.Label(frame_form_top, text = "Bienvenido al sistema", font = ("times", 30), fg="black", bg ="white",pady=50)
        title.pack(expand=tk.YES, fill=tk.BOTH)

        #frame de abajo que sirve de relleno
        frame_form_fill = tk.Frame(frame_form, height = 50, bd=0, relief=tk.SOLID, bg="white")
        frame_form_fill.pack(side="bottom", expand = tk.YES, fill=tk.BOTH)

        etiqueta_usuario = tk.Label(frame_form_fill, text = "Usuario",
                            font=("Calibri", 14), fg = "black", bg ="white", anchor="w")
        etiqueta_usuario.pack(fill=tk.X, padx=20, pady=5)
        self.usuario = ttk.Entry(frame_form_fill, font=("Arial, 14"))
        self.usuario.pack(fill=tk.X, padx=20, pady=10)

        etiqueta_password = tk.Label(frame_form_fill, text = "Contraseña",
                                font=("Calibri", 14), fg = "black", bg ="white", anchor="w")
        etiqueta_password.pack(fill=tk.X, padx=20, pady=5)
        self.password = ttk.Entry(frame_form_fill, font=("Times, 14"))
        self.password.pack(fill=tk.X, padx=20, pady=10)
        self.password.config(show="*")

        inicio = tk.Button(frame_form_fill, text="Iniciar sesión",
                            font=("Calibri", 15, BOLD), bg="lightblue", fg="black", command=self.verificar)
        inicio.pack(fill = tk.X, padx=20, pady=20)
        inicio.bind("<Return>", (lambda event : self.verificar()))

        registro = tk.Button(frame_form_fill, text="Crear cuenta nueva",
                            font=("Calibri", 15, BOLD), bg="greenyellow", fg="black", command=self.RegistrarUsuario)
        registro.pack(fill = tk.X, padx=20, pady=20)
        registro.bind("<Return>", (lambda event : self.RegistrarUsuario()))

        self.ventana.mainloop()

    def verificar(self):
        pass

    def RegistrarUsuario(self):
        pass
