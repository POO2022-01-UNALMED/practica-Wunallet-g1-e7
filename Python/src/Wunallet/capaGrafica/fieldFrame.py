from ast import Import
import tkinter as tk
from tkinter import Frame
from tkinter  import ttk
from tkinter import messagebox



class FieldFrame(Frame):
 
    def __init__(self, frame, tituloFuncion, descripcion, tituloCriterios, criterios, tituloValores, valores,val=None, habilitados=None):
        self._tituloFuncion = tituloFuncion # titulo funcionalidad
        self._descripcion = descripcion # descripcion de la funcionalidad
        self._tituloCriterios = tituloCriterios
        self._criterios = criterios
        self._tituloValores = tituloValores
        self._valores = valores

        # Se crean y posicionan los label del titulo y la descripción de la funcionalidad
        labelNombreF = tk.Label(frame,text=tituloFuncion,font = ("Arial",15,"bold"))
        labelNombreF.grid(row=0,column=0,columnspan=6,pady=10)
        labelDescripcionF = tk.Label(frame,text=descripcion,font = ("Arial",10))
        labelDescripcionF.grid(row=1,column=0,columnspan=6,padx=10,pady=10)

        # Se crean y posicionan los label de los titulos de criterios y valores
        labelTituloCriterios=tk.Label(frame,text=self._tituloCriterios.upper(),font = ("Arial",10,'bold'))
        labelTituloCriterios.grid(row=3,column=0,padx=10,pady=10)
        labelTituloValores=tk.Label(frame,text=self._tituloValores.upper(),font = ("Arial",10,'bold'))
        labelTituloValores.grid(row=3,column=2,columnspan=3,padx=10,pady=10)

        # Si no se introduce explícitamente la lista de criterios habilitados, entonces habilitados será una lista de Trues con
        #la misma longitud que la lista de criterios-valores
        if habilitados == None:
            habilitados = [True for i in range(len(criterios))] 

        formulario_dict = {}
        # Creación y ubicación de cada label por criterio y entry por valor. En caso de que el criterio sea banco, el entry será
        # un combobox
        for criterio, valor, habilitado, indice in zip(criterios, valores, habilitados, range(len(criterios))):
            if "Banco" in criterio:
                labelCriterio = tk.Label(frame, text = criterio, font = ("Arial", 10))
                valorDefecto = tk.StringVar(value="Bancos disponibles")
                entryValue = ttk.Combobox(frame, state="readonly", values=["Unalombia","PooBanco","QuitaVivienda"],
                        textvariable=valorDefecto)
                formulario_dict[labelCriterio] = entryValue
                labelCriterio.grid(row=indice+4, column=0, padx=10, pady=10)
                entryValue.grid(row=indice+4, column=2, columnspan=3, padx=10, pady=10)

            else:
                
                if "Tipo Cuenta" in criterio:
                    
                    labelCriterio = tk.Label(frame, text = criterio, font = ("Arial", 10))
                    valorDefecto = tk.StringVar(value="Tipos disponibles")
                    entryValue = ttk.Combobox(frame, state="readonly", values=["bajoMonto","ahorros","corriente"],
                            textvariable=valorDefecto)
                    formulario_dict[labelCriterio] = entryValue
                    labelCriterio.grid(row=indice+4, column=0, padx=10, pady=10)
                    entryValue.grid(row=indice+4, column=2, columnspan=3, padx=10, pady=10)
                    labelCriterio = tk.Label(frame, text = criterio, font = ("Arial", 10))
                else:
                    if "Cuentas Disponibles" in criterio:
                        labelCriterio = tk.Label(frame, text = criterio, font = ("Arial", 10))
                        valorDefecto = tk.StringVar(value="Cuentas disponibles")
                        entryValue = ttk.Combobox(frame, state="readonly", values=val,
                                textvariable=valorDefecto)
                        formulario_dict[labelCriterio] = entryValue
                        labelCriterio.grid(row=indice+4, column=0, padx=10, pady=10)
                        entryValue.grid(row=indice+4, column=2, columnspan=3, padx=10, pady=10)
                        labelCriterio = tk.Label(frame, text = criterio, font = ("Arial", 10))
                    
                    else:
                        if "Tipo Transferencia" in criterio:
                            labelCriterio = tk.Label(frame, text = criterio, font = ("Arial", 10))
                            valorDefecto = tk.StringVar(value="Tipos disponibles")
                            entryValue = ttk.Combobox(frame, state="readonly", values=["Pagar credito","A otra cuenta - Inscrita","A otra cuenta - No inscrita"],
                                    textvariable=valorDefecto)
                            formulario_dict[labelCriterio] = entryValue
                            labelCriterio.grid(row=indice+4, column=0, padx=10, pady=10)
                            entryValue.grid(row=indice+4, column=2, columnspan=3, padx=10, pady=10)
                            labelCriterio = tk.Label(frame, text = criterio, font = ("Arial", 10))
                        
                        else:
                            labelCriterio = tk.Label(frame, text = criterio, font = ("Arial", 10))
                            if habilitado is False:
                                entryValue = tk.Entry(frame, textvariable = tk.StringVar(frame, value = valor), state='disabled')
                            else:
                                entryValue = tk.Entry(frame, text = tk.StringVar(frame, value = valor), state='normal')
                                formulario_dict[labelCriterio] = entryValue
                                labelCriterio.grid(row=indice+4, column=0, padx=10, pady=10)
                                entryValue.grid(row=indice+4, column=2, columnspan=3, padx=10, pady=10)
            
            

        # Método para obtener el valor de un criterio en específico
        def getValue(self,criterio):
            if criterio in set(self._criterios):
                print("Esta")
                for (labelCriterio, entryValue) in formulario_dict.items():
                    if labelCriterio.cget("text") == criterio:
                        return entryValue.get()
            else:
                print("No esta")

        # def values_frame():
            # for widget in frame.winfo_children():
                # if isinstance(widget, tk.Entry):
                    # print(widget.get())

        # def pantallaIngresar():
            # messagebox.showinfo("Usuario Seleccionado",
                                # "Usted seleccionó: "+entrysC[keysEntrys[0]].get())

## Funcion boton de la derecha
    # def clear_frame():
        # for widget in frame.winfo_children():
            # if isinstance(widget, tk.Entry):
                # widget.delete(0,last="end")

        # self.botonDer = tk.Button(frame, text = "Borrar",command=clear_frame)
        # self.botonDer.grid(row=len(self._criterios)+4,column=2,columnspan=3,padx=10,pady=10)

    # @arg criterio el criterio cuyo valor se quiere obtener
    # @return el valor del criterio cuyo nombre es 'criterio'


