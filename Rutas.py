# Origen
# Destino
# Nombre de la ruta
# Distancia en kilometros 
from tkinter import StringVar 
from tkinter import IntVar

class Rutas: 

    def __init__(self):
        self.origen = StringVar()
        self.destino = StringVar()
        self.nombre_rutas = StringVar()
        self.distanciaKm= IntVar()
        

    def limpiar(self):
        self.origen.set("")
        self.nombre_rutas.set("")
        self.destino.set("")
        self.distanciaKm.set(0)
   

    def printInfo(self):
        print(f"Origen:{self.origen.get()}")
        print(f"Destino:{self.destino.get()}")
        print(f"Nombre de la Ruta:{self.nombre_rutas.get()}")
        print(f"Distancia en Kilometros:{self.distanciaKm.get()}")
     