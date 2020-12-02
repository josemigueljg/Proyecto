import tkinter
import mysql
from tkinter import * 
from tkinter import font
from tkinter import messagebox as msg
from tkinter import ttk 
from tksheet import Sheet
from tkcalendar import Calendar, DateEntry 
from modelo import Persona
from modelo import PersonoBO
import mant_telefonos 

class Aplicacion:

    def __init__(self):

        self.pantalla = Tk()
        self.pantalla.geometry("300x380")
        self.pantalla.title("Usuario")


        menubar = Menu(self.pantalla)
        self.pantalla.config(menu=menubar)

        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Acerca de..")
        filemenu.add_separator()
        filemenu.add_command(label="Salir", command=self.pantalla.quit)


        menubar.add_cascade(label="Archivo", menu=filemenu)
        menubar.add_cascade(label="Mantenimiento", menu=mantmenu)


        self.fuente = font.Font(weight="bold")


        self.persona = Persona.Persona()
        self.insertando = True
        

        self.lb_tituloPantalla = Label(self.pantalla, text = "MANTENIMIENTO DE PERSONAS", font = self.fuente)
        self.lb_tituloPantalla.place(x = 320, y = 20) 
        

        self.lb_cedula = Label(self.pantalla, text = "Cedula:")
        self.lb_cedula.place(x = 240, y = 60)
        self.txt_cedula = Entry(self.pantalla, textvariable=self.persona.cedula, justify="right")
        self.txt_cedula.place(x = 370, y = 60)


        self.lb_nombre = Label(self.pantalla, text = "Nombre:")
        self.lb_nombre.place(x = 240, y = 90)
        self.txt_nombre = Entry(self.pantalla, textvariable=self.persona.nombre, justify="right", width=30)
        self.txt_nombre.place(x = 370, y = 90)


        self.lb_apellido1 = Label(self.pantalla, text = "Primer apellido:")
        self.lb_apellido1.place(x = 240, y = 120)
        self.txt_apellido1 = Entry(self.pantalla, textvariable=self.persona.apellido1, justify="right", width=30)
        self.txt_apellido1.place(x = 370, y = 120)



        self.lb_apellido2 = Label(self.pantalla, text = "Segundo apellido:")
        self.lb_apellido2.place(x = 240, y = 150)
        self.txt_apellido2 = Entry(self.pantalla, textvariable=self.persona.apellido2, justify="right", width=30)
        self.txt_apellido2.place(x = 370, y = 150)


        self.lb_fec_nacimiento = Label(self.pantalla, text = "Fecha nacimiento:")
        self.lb_fec_nacimiento.place(x = 240, y = 180)
        self.txt_fechaNacimiento = Entry(self.pantalla, textvariable=self.persona.fecNacimiento, justify="right", width=30, state="readonly")
        self.txt_fechaNacimiento.place(x = 370, y = 180)
        self.bt_mostrarCalendario = Button(self.pantalla, text="...", width=3, command = self.mostrarDatePicker)
        self.bt_mostrarCalendario.place(x = 650, y = 180)


        self.lb_sexo = Label(self.pantalla, text = "Sexo:")
        self.lb_sexo.place(x = 240, y = 210)
        self.radio_sexoM = Radiobutton(self.pantalla, text="Masculino", variable=self.persona.sexo,   value=1)
        self.radio_sexoF = Radiobutton(self.pantalla, text="Femenino", variable=self.persona.sexo,   value=2)
        self.radio_sexoM.place(x = 370, y = 210)
        self.radio_sexoF.place(x = 490, y = 210)
        self.persona.sexo.set(1)


        self.lb_observaciones = Label(self.pantalla, text = "Observaciones:")
        self.lb_observaciones.place(x = 240, y = 250)
        self.txt_observaciones = Entry(self.pantalla, textvariable=self.persona.observaciones, justify="right", width=30)
        self.txt_observaciones.place(x = 370, y = 250)


        self.bt_borrar = Button(self.pantalla, text="Limpiar", width=15, command = self.limpiarInformacion)
        self.bt_borrar.place(x = 370, y = 310)

        self.bt_enviar = Button(self.pantalla, text="Enviar", width=15, command = self.enviarInformacion)
        self.bt_enviar.place(x = 510, y = 310)

        self.bt_modificar = Button(self.pantalla, text="Modificar", width=15, command = self.enviarInformacion)
        self.bt_modificar.place(x = 650, y = 310)


        self.lb_tituloPantalla = Label(self.pantalla, text = "INFORMACIÓN INCLUIDA", font = self.fuente)
        self.lb_tituloPantalla.place(x = 350, y = 355)

  

def main():
    Aplicacion()
    return 0

if __name__ == "__main__":
    main()

