import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox, scrolledtext
from tkinter.font import BOLD
import threading


class SalaChatDesign:
    def __init__(self): #, servidor, nombre):
        #self.servidor = servidor
        self.gui_done = False
        self.running = True

        self.hilo_recibe = threading.Thread(target = self.recibirMensaje)
        self.hilo_interfaz = threading.Thread(target = self.run)

        self.hilo_recibe.start()
        self.hilo_interfaz.start()

    def run(self):
        self.ventana = tk.Tk()
        self.ventana.title("sala chat")
        self.ventana.geometry("800x600")
        self.ventana.config(bg = "LightSkyBlue1")
        self.ventana.resizable(width = 0, height = 0)
        self.ventana.protocol("WM_DELETE_WINDOW", self.disabledEvent)

        #---------------------------------------------------
        BarraMenu = Menu(self.ventana, background="WhiteSmoke")
        #---------------------------------------------------
        menuOpciones = Menu(BarraMenu)
        menuOpciones.add_command(label = "Crear sala", command=self.crearSala)
        menuOpciones.add_command(label = "Entrar sala")
        menuOpciones.add_command(label = "Salir sala")
        menuOpciones.add_command(label = "Eliminar sala")
        #---------------------------------------------------
        menuSalir = Menu(BarraMenu)
        menuSalir.add_command(label = "Salir", command=self.exit)
        #---------------------------------------------------
        menuPrivado = Menu(BarraMenu)
        menuPrivado.add_command(label = "Enviar mensaje privado")
        #---------------------------------------------------
        menuVer = Menu(BarraMenu)
        menuVer.add_command(label = "Lista salas y participantes")
        menuVer.add_command(label = "Mostrar usuarios registrados")
        #---------------------------------------------------
        BarraMenu.add_cascade(label = "Opciones de sala", menu = menuOpciones)
        BarraMenu.add_cascade(label = "Ver", menu = menuVer)
        BarraMenu.add_cascade(label = "Privado", menu = menuPrivado)
        BarraMenu.add_cascade(label = "Exit", menu = menuSalir)

        self.ventana.config(menu=BarraMenu)

        #frame "formulario"
        frame_form = tk.Frame(self.ventana, bd=0, width=400, relief=tk.SOLID, bg="white")
        frame_form.pack(side= "right", expand=1, fill=tk.BOTH, padx=40, pady=15)

        #frame de la parte de arriba, para que no entendi XD
        frame_form_top = tk.Frame(frame_form, height = 30, bd=0, relief=tk.SOLID, bg="black")
        frame_form_top.pack(side = "top", fill =tk.BOTH)
        title = tk.Label(frame_form_top, text = "Chat Grupal", font = ("times", 14), fg="black", bg ="white")
        title.pack(expand=tk.YES, fill=tk.X)

        frame_form_fill = tk.Frame(frame_form, height = 50, bd=0, relief=tk.SOLID, bg="WhiteSmoke")
        frame_form_fill.pack(side="bottom", expand = tk.YES, fill=tk.BOTH)
        # Zona donde se mostraran los mensajes

        self.areaTexto = tk.scrolledtext.ScrolledText(frame_form_fill)
        self.areaTexto.pack( padx=5, pady=5, expand = tk.YES, fill=tk.BOTH)
        self.areaTexto.config(state = "disabled")

        #frame de abajo que sirve como zona donde se escriben los mensajes y se envian

        frame_form_bottom = tk.Frame(frame_form_fill, height = 80, bd=0, relief=tk.SOLID, bg="WhiteSmoke")
        frame_form_bottom.pack(side = "bottom", fill =tk.BOTH)

        etiqueta_nombres = tk.Label(frame_form_bottom, text = "Mensaje:",
                            font=("Calibri", 11), fg = "black", bg ="WhiteSmoke", anchor="center")
        etiqueta_nombres.pack(fill=tk.X, padx=20)
        self.mensaje = tk.Text(frame_form_bottom, font=("Arial, 11"), height=1)
        self.mensaje.pack(fill=tk.X, padx=20)

        enviar = tk.Button(frame_form_bottom, text="Enviar", font=("Calibri", 13, BOLD),
                            bg="SteelBlue1", fg="black",command=self.enviarMensaje)
        enviar.pack(anchor="se", padx=10, pady=10)

        self.gui_done = True

        self.ventana.mainloop()

    def disabledEvent(self):
        pass

    def borrarEntradaTexto(self):
        pass

    def enviarMensaje(self):
        pass

    def recibirMensaje(self):
        pass

    def exit(self):
        pass

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
