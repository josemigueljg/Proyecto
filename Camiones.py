from tkinder import StringVar
from tkinder import IntVar

class Camiones:
    def __init__(self):
        self.placa = StringVar()
        self.conductor = StringVar()
        self.estado = IntVar()
        self.RutCamion = StringVar()
        self.UbiActual = StringVar()


    def limpiar(self):
        self.placa.set("")
        self.conductor.set("")
        self.estado.set(0)
        self.RutCamion.set("")
        self.UbiActual.set("")

    def printInfo(self):
        print(f"placa:{self.placa.get()}")
        print(f"conductor:{self.conductor.get()}")
        print(f"estado:{self.estado.get()}")
        print(f"RutCamion:{self.RutCamion.get()}")
        print(f"UbiActual:{UbiActual.get()}")
        