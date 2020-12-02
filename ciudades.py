from tkinter import StringVar
from tkinter import IntVar

class Ciudades:

    def __init__(self):
        self.idciudad = StringVar()
        self.estadoCiudad = IntVar()
        self.nombreCiudad = StringVar()
        self.descripcion = StringVar()
    
    def limpiar(self):
        self.idciudad.set("")
        self.estadoCiudad.set(0)
        self.nombreCiudad.set("")
        self.descripcion.set("")

    def printInfo(self):
        print(f"ID de Ciudad: {self.idciudad.get()}")
        print(f"Estado de Ciudad: {self.estadoCiudad.get()}")
        print(f"Nombre de Ciudad: {self.nombreCiudad.get()}")
        print(f"Descripción: {self.descripcion.get()}")