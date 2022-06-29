from ast import Import
import tkinter as tk
from tkinter import Frame
from tkinter  import ttk
from tkinter import messagebox

class PairButton(Frame):

    def __init__(self, frame, LBotonTitulo,RBotonTitulo='Borrar'):
        self._LBoton = tk.Button(frame, text=LBotonTitulo)
        self._RBoton = tk.Button(frame, text=RBotonTitulo)
        self._LBoton.grid(row=0, column=0, padx=50, pady=10)
        self._RBoton.grid(row=0, column=2, columnspan=3, padx=150, pady=10)


    def borrarCampos(frame):
        for widget in frame.winfo_children():
            if isinstance(widget, tk.Entry):
                widget.delete(0,last="end")
            if isinstance(widget, ttk.Combobox):
                widget.set('')
                

                
