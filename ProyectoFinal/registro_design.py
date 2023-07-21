import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from tkinter.font import BOLD

class RegisterDesign:
    def __init__(self, servidor):
        self.servidor = servidor
        self.ventana = tk.Toplevel()
        self.ventana.title("Registro nueva cuenta")
        self.ventana.geometry("800x500")
        self.ventana.config(bg = "lightblue")
        self.ventana.resizable(width = 0, height = 0)

        #En caso de poner logo
        #logo= PhotoImage(file="nombre.gif")
        #logo=image.subsample(2,2)
        #logo=label(image=image)
        #label.pack()

        #FRAME derecha
        frame_logo = tk.Frame(self.ventana, bd=0, width=200, relief=tk.SOLID, padx=10, pady=10, bg="greenyellow")
        frame_logo.pack(side = "left", expand=tk.NO, fill=tk.BOTH)

        #frame "formulario"
        frame_form = tk.Frame(self.ventana, bd=0, width=600, relief=tk.SOLID, bg="white")
        frame_form.pack(side= "right", expand=tk.YES, fill=tk.BOTH)

        #frame de la parte de arriba, para que no entendi XD
        frame_form_top = tk.Frame(frame_form, height = 50, bd=0, relief=tk.SOLID, bg="white")
        frame_form_top.pack(side = "top", fill =tk.X)
        title = tk.Label(frame_form_top, text = "Registro de usuario", font = ("times", 20), fg="black", bg ="white",pady=10)
        title.pack(expand=tk.YES, fill=tk.BOTH)

        #frame de abajo que sirve de relleno
        frame_form_fill = tk.Frame(frame_form, height = 50, bd=0, relief=tk.SOLID, bg="white")
        frame_form_fill.pack(side="bottom", expand = tk.YES, fill=tk.BOTH)

        #nombres},{apellidos},{username},{password},{int(edad)},{genero
        etiqueta_nombres = tk.Label(frame_form_fill, text = "Nombres",
                            font=("Calibri", 11), fg = "black", bg ="white", anchor="w")
        etiqueta_nombres.pack(fill=tk.X, padx=20)
        self.nombres = ttk.Entry(frame_form_fill, font=("Arial, 11"))
        self.nombres.pack(fill=tk.X, padx=20)

        etiqueta_apellidos = tk.Label(frame_form_fill, text = "Apellidos",
                                font=("Calibri", 11), fg = "black", bg ="white", anchor="w")
        etiqueta_apellidos.pack(fill=tk.X, padx=20, pady=5)
        self.apellidos = ttk.Entry(frame_form_fill, font=("Times, 11"))
        self.apellidos.pack(fill=tk.X, padx=20)

        etiqueta_usuario = tk.Label(frame_form_fill, text = "Usuario",
                            font=("Calibri", 11), fg = "black", bg ="white", anchor="w")
        etiqueta_usuario.pack(fill=tk.X, padx=20, pady=5)
        self.usuario = ttk.Entry(frame_form_fill, font=("Arial, 11"))
        self.usuario.pack(fill=tk.X, padx=20)

        etiqueta_password = tk.Label(frame_form_fill, text = "Contraseña",
                                font=("Calibri", 11), fg = "black", bg ="white", anchor="w")
        etiqueta_password.pack(fill=tk.X, padx=20, pady=5)
        self.password = ttk.Entry(frame_form_fill, font=("Times, 11"))
        self.password.pack(fill=tk.X, padx=20)
        self.password.config(show="*")

        etiqueta_edad = tk.Label(frame_form_fill, text = "Edad",
                                font=("Calibri", 11), fg = "black", bg ="white", anchor="w")
        etiqueta_edad.pack(fill=tk.X, padx=20, pady=5)
        self.edad = ttk.Entry(frame_form_fill, font=("Times, 11"))
        self.edad.pack(fill=tk.X, padx=20)

        #----------------------------------------------------------------------------------------
        #Lista de opciones de genero
        etiqueta_genero = tk.Label(frame_form_fill, text = "Genero",
                                font=("Calibri", 11), fg = "black", bg ="white", anchor="w")
        etiqueta_genero.pack(fill=tk.X, padx=20, pady=5)

        self.lista_desplegable = ttk.Combobox(frame_form_fill, state="readondly", justify="left")
        opciones= ["Femenino", "Masculino", "Prefiero no especificar"]
        self.lista_desplegable['values'] = opciones
        self.lista_desplegable.pack()

        self.genero = StringVar()
        self.lista_desplegable.bind("<<ComboboxSelected>>", self.opcionElegida)
        #----------------------------------------------------------------------------------------
        self.registro = tk.Button(frame_form_fill, text="Registrar",
                            font=("Calibri", 15, BOLD), bg="greenyellow", fg="black", command=self.registrar, state="disabled")
        self.registro.pack(fill = tk.X, padx=20, pady=20)
        self.registro.bind("<Return>", (lambda event: self.registrar()))

        self.ventana.mainloop()

    def registrar(self):
        pass

    def opcionElegida(self,event):
        self.genero = self.lista_desplegable.get()
        if self.nombres.get()!="" and self.apellidos.get()!=""  and self.usuario.get()!="" and self.password.get()!="" and self.edad.get()!="":
           self.registro["state"] = "normal"
