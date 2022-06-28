from asyncio.windows_events import NULL
import tkinter as tk
from tkinter import messagebox
import gc

from setuptools import Command
from fieldFrame import FieldFrame
# Importamos las clases de la aplicación
# Se imoprtan las clases con información de los clientes
""" from gestorAplicacion.infoClientes.Banco import Banco
from gestorAplicacion.infoClientes import PerfilCrediticio
from gestorAplicacion.infoClientes import Usuario
from gestorAplicacion.infoClientes import comportamientoDePago """

# Se imoprtan las clases con información de los productos financieros
""" from gestorAplicacion.productosFinancieros import Ahorro
from gestorAplicacion.productosFinancieros import BajoMonto
from gestorAplicacion.productosFinancieros import Corriente
from gestorAplicacion.productosFinancieros import Credito
from gestorAplicacion.productosFinancieros import Cuenta """

#-------------------#
# OBJETOS DE PRUEBA #
#-------------------#

# USUARIOS
""" juanPerez = Usuario(NULL,1000000,10,NULL)
hernestoPerez = Usuario(NULL,2000000,98,NULL) """

# BANCOS
""" Unalombia = Banco("Unalombia",1.6)
PooBanco = Banco("PooBanco",2.5)
QuitaVivienda = Banco("QuitaVivienda",36.0) """

# CUENTAS
""" cuenta1 = Ahorro(89,juanPerez, 10000.0 ,QuitaVivienda,"ahorro",2.5)
cuenta3 = Corriente(23,juanPerez,50000000.0,Unalombia,"corriente",1.2)
cuenta2 = BajoMonto(69,hernestoPerez, 1000000.0,PooBanco, "bajoMonto", 2.2,3000000.0,3000000.0)
cuenta4 = BajoMonto(26,hernestoPerez, 6000000.0,Unalombia, "bajoMonto", 1.3,200000.0,200000.0) """
#-----------------------------
#-----------------------------
#-----------------------------
ventana = tk.Tk()
ventana.title("WUNALLET")
ventana.geometry("800x500")
ventana.option_add('*tearOff',False)

#------#
# MENU #
#------#

# Se define la barra de menu
menuPrincipal = tk.Menu(ventana)
ventana.config(menu=menuPrincipal)

# Agregamos los diferentes menus disponibles
archivo = tk.Menu(menuPrincipal)
procesosYconsultas = tk.Menu(menuPrincipal)
ayuda = tk.Menu(menuPrincipal)

menuPrincipal.add_cascade(label="Archivo",menu=archivo)
menuPrincipal.add_cascade(label="Procesos y Consultas",menu=procesosYconsultas)
menuPrincipal.add_cascade(label="Ayuda",menu=ayuda)

# Estructura menu Archivo

def archivoAplicacion():
    messagebox.showinfo("Aplicación","Explicación de lo que hace WUNALLET")

archivo.add_command(label="Aplicación",command=archivoAplicacion)

# Estructura menu Procesos y Consultas

menuFuncionalidades = tk.Menu(menuPrincipal)
procesosYconsultas.add_cascade(label="Funcionalidades",menu=menuFuncionalidades)

# Selección De Usuario
frameF0 =  tk.Frame(ventana,width=800,height=500) # Frame para el ingreso del ususario
frameF00 =  tk.Frame(ventana,width=800,height=500) # Frame para el mensaje de usuario seleccionado

FieldFrame (frame=frameF0,
                tituloF="Selección de usuario",
                descrip="A continuación seleccione el usuario con el que desea ingresar. Una vez ingrese\n dirijace al menu de Procesos y Consultas, alli podra encontrar un listado de\n funcionalidades de la cuales podra hacer uso con su usuario.",
                tituloCriterios="Criterio",
                criterios= "Usuario",
                tituloValores= "Valor",
                valores= NULL,
                tituloBoton="Ingresar")
frameF0.pack(expand=True)

# Frames para el menu Procesos y Consultas
resultado = tk.Frame(ventana,width=400,height=250)

frameF1 =  tk.Frame(ventana,width=800,height=500)
frameF2 = tk.Frame(ventana,width=400,height=250)
frameF3 = tk.Frame(ventana,width=800,height=500)
frameF4 = tk.Frame(ventana,width=800,height=500)
frameF5 = tk.Frame(ventana,width=800,height=500)



# Se debe definir una función para eliminar los labels abiertos del frame resultado cuando se vuelva a abrir el menu
def delete(): 
    for label in resultado.winfo_children():
        if isinstance(label,tk.Label) : # just Label since you used a wildcard import to import tkinter
            print(label.cget("text"))
            label.destroy()
            try:
                print(label.cget("text"))
            except:
                print("Hola")
            

    for boton in frameF2.winfo_children():
        if isinstance(boton,tk.Button) : # just Label since you used a wildcard import to import tkinter
            boton.destroy()
            
# Se debe definir una función para esconder los frames abiertos cuando se abre otro
def hide_all_frames():
    frameF00.pack_forget()
    frameF0.pack_forget()
    frameF1.pack_forget()
    frameF2.pack_forget()
    frameF3.pack_forget()
    frameF4.pack_forget()
    frameF5.pack_forget()
    resultado.pack_forget()
    

def F1():
    hide_all_frames()
    criterios = ["Banco", "Tipo Cuenta", "Numero Cuenta", "Numero Cedula"]
    FieldFrame (frame=frameF1,
                tituloF="Inscribir Cuenta",
                descrip="Esta funcionalidad consiste en vincular a un usuario con una o mas cuentas",
                tituloCriterios="Criterio",
                criterios= criterios,
                tituloValores= "Valor",
                valores= NULL,
                tituloBoton="Inscribir")
    frameF1.pack(expand=True)
    
# Funcionalidad Inscribir Cuentas
menuFuncionalidades.add_command(label="F1",command=F1)

def F2():
    hide_all_frames()  
    delete()
    global textResultF2
    textResultF2 = tk.Label(resultado)
    textResultF2.grid(row=0,column=0,columnspan=6,pady=10)  
    criterios = ["Numero Cuenta"]
    p=FieldFrame (frame=frameF2,
                tituloF="Ver Historial",
                descrip="Esta funcionalidad consiste en mostrar el hisotorial de transferencias de una cuenta.",
                tituloCriterios="Criterio",
                criterios= criterios,
                tituloValores= "Valor",
                valores= NULL,
                tituloBoton="Ver Historial") 
    
    def values_frameF2():
        inputsF2 = {} 
        for widget in frameF2.winfo_children():
            if isinstance(widget, tk.Entry):
                inputsF2[criterios[0]] = widget.get()
                try:
                    int(inputsF2[criterios[0]])
                    if int(inputsF2[criterios[0]])<0:
                        textResultF2.config(text="")
                        messagebox.showerror("Error","El numero de cuenta debe ser entero")
                    else:
                        textResultF2.config(text=widget.get())
                        widget.configure(state="disable")
                except:
                    if inputsF2[criterios[0]]=="":
                        textResultF2.config(text="")
                        messagebox.showerror("Error","Se deben llenar todos los campos")
                    else:
                        textResultF2.config(text="")
                        messagebox.showerror("Error","El numero de cuenta debe ser entero")
                    
             
    getattr(p,'botonIzq').config(command=values_frameF2)      
    frameF2.pack(expand=True)
    resultado.pack(expand=True)    



menuFuncionalidades.add_command(label="F2",command=F2)

def F3():
    hide_all_frames()
    criterios = ["Banco","Cuenta","Monto","Plazo"]
    FieldFrame (frame=frameF3,
                tituloF="Solicitar Credito",
                descrip="Esta funcionalidad genera un credito al usuario",
                tituloCriterios="Criterio",
                criterios= criterios,
                tituloValores= "Valor",
                valores= NULL,
                tituloBoton="Solicitar") 
    frameF3.pack(expand=True) 

menuFuncionalidades.add_command(label="F3",command=F3)

def F4():
    hide_all_frames()
    criterios = "Cuenta"
    FieldFrame (frame=frameF4,
                tituloF="Romper Topes",
                descrip="Esta funcionalidad consiste en cmabiar una cuenta de bajo monto en una de ahorros",
                tituloCriterios="Criterio",
                criterios= criterios,
                tituloValores= "Valor",
                valores= NULL,
                tituloBoton="Romper Topes") 
    frameF4.pack(expand=True) 
menuFuncionalidades.add_command(label="F4",command=F4)

def F5():
    hide_all_frames()
    criterios = ["Cuenta Origen","Tipo Transferencia","Cuenta Destino","Banco Destino","Numero Cuenta","Valor"]
    FieldFrame (frame=frameF5,
                tituloF="Transferir",
                descrip="Esta funcionalidad consiste en transferir dinero a otra cuenta o pagar un credito al banco",
                tituloCriterios="Criterio",
                criterios= criterios,
                tituloValores= "Valor",
                valores= NULL,
                tituloBoton="Transferir") 
    frameF5.pack(expand=True) 
menuFuncionalidades.add_command(label="F5",command=F5)

# Estructura menu AYUDA

def acercaDe():
    messagebox.showinfo("Acerca de:","Daniel \n Diego \n David \n Cesar")

ayuda.add_command(label="Autores:",command=acercaDe)








ventana.mainloop()