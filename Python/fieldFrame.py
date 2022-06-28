from ast import Import
import tkinter as tk
from tkinter import Frame
from tkinter  import ttk
from tkinter import messagebox

class FieldFrame(Frame):
 
    def __init__(self,frame,tituloF,descrip,tituloCriterios, criterios, tituloValores, valores,tituloBoton, habilitado=False):
        self._tituloC = tituloCriterios
        self._criterios = criterios
        self._tituloV = tituloValores
        self._vals = valores
        self._habilitar = habilitado
        self._tituloF = tituloF # titulo funcionalidad
        self._descrip = descrip # descripcion de la funcionalidad
        self._tituloBoton = tituloBoton

        labelsC = {}
        entrysC = {}

        # Titulo y descripcion de la funcionalidad
        nombreFuncionalidad = tk.Label(frame,text=self._tituloF,font = ("Arial",15,"bold"))
        descripcionFuncionalidad = tk.Label(frame,text=self._descrip,font = ("Arial",10))
        
        nombreFuncionalidad.grid(row=0,column=0,columnspan=6,pady=10)
        descripcionFuncionalidad.grid(row=1,column=0,columnspan=6,padx=10,pady=10)

        # Se ubican posteriormente los titulos de criteios y valores
        labelsC["label00"]=tk.Label(frame,text=self._tituloC.upper(),font = ("Arial",10,'bold'))
        labelsC["label11"]=tk.Label(frame,text=self._tituloV.upper(),font = ("Arial",10,'bold'))

        labelsC["label00"].grid(row=3,column=0,padx=10,pady=10)
        labelsC["label11"].grid(row=3,column=2,columnspan=3,padx=10,pady=10)

        # Se ubican posteriormente los labels de los criterios y los entrys
        if isinstance(self._criterios,list):
            for i in range(0,len(self._criterios)):
                # Defino los labels y los entry
                
                labelsC["label{0}".format(i)]=tk.Label(frame,text=self._criterios[i])
                entrysC["entry{0}".format(i)]=tk.Entry(frame)

                # Obtengo los nombres clave de los labels y entrys
                keysLabels = list(labelsC)[2:]
                keysEntrys = list(entrysC)

                labelsC[keysLabels[i]].grid(row=i+4,column=0,padx=10,pady=10)
                entrysC[keysEntrys[i]].grid(row=i+4,column=2,columnspan=3,padx=10,pady=10)

        else:
            # Defino el label y el entry
            labelsC["label{0}".format(1)]=tk.Label(frame,text=self._criterios)
            entrysC["entry{0}".format(1)]=tk.Entry(frame)
                
            # Obtengo los nombres clave de los labels y entrys
            keysLabels = list(labelsC)[2:]
            keysEntrys = list(entrysC)

            labelsC[keysLabels[0]].grid(row=4,column=0,padx=10,pady=10)
            entrysC[keysEntrys[0]].grid(row=4,column=2,columnspan=3,padx=10,pady=10)

        # Banco ?
        indxBanco = None
        # ¿Esta la palabra Banco en alguno de los criterios?
        bancoEsta = [char.find("Banco") for char in self._criterios] 
        if any(x !=-1 for x in bancoEsta):
            indxBanco = bancoEsta.index(0) # 0: Porque es donde se encuentra la palabra Banco en criterios
            valorDefecto = tk.StringVar(value="BancosDisponibles")
            labelsC["label{0}".format(indxBanco)]=tk.Label(frame,text=self._criterios[indxBanco])
            entrysC["entry{0}".format(indxBanco)]=ttk.Combobox(frame,state="readonly",values=["Unalombia","PooBanco","QuitaVivienda"],textvariable=valorDefecto)
            keysLabels = list(labelsC)[2:]
            keysEntrys = list(entrysC)
            labelsC[keysLabels[indxBanco]].grid(row=indxBanco+4,column=0,padx=10,pady=10)
            entrysC[keysEntrys[indxBanco]].grid(row=indxBanco+4,column=2,columnspan=3,padx=10,pady=10) 

        def values_frame():
            for widget in frame.winfo_children():
                if isinstance(widget, tk.Entry):
                    print(widget.get())

        def pantallaIngresar():
            messagebox.showinfo("Usuario Seleccionado",
                                "Usted seleccionó: "+entrysC[keysEntrys[0]].get())

        if self._tituloBoton=="Ingresar":
            self.botonIzq = tk.Button(frame, text =self._tituloBoton,command=pantallaIngresar)
            
        else:
            self.botonIzq = tk.Button(frame, text =self._tituloBoton,command=values_frame)
            

        def clear_frame():
            for widget in frame.winfo_children():
                if isinstance(widget, tk.Entry):
                    widget.delete(0,last="end")

        self.botonDer = tk.Button(frame, text = "Borrar",command=clear_frame)

        self.botonIzq.grid(row=len(self._criterios)+4,column=0,padx=10,pady=10)
        self.botonDer.grid(row=len(self._criterios)+4,column=2,columnspan=3,padx=10,pady=10)
    # @arg criterio el criterio cuyo valor se quiere obtener
    # @return el valor del criterio cuyo nombre es 'criterio'

    def getValue(self,criterio):
        if criterio in set(self._criterios):
             print("Esta")
            
        else:
            print("No esta")

        

        

    

