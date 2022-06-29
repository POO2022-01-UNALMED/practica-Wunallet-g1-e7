import tkinter as tk
import os
from tkinter import Label, Entry, Button, Text, PhotoImage, Frame, INSERT, scrolledtext
from PIL import Image,ImageTk
import pathlib
from Wunallet.UI_Wunalet import V_P
from Wunallet.capaGrafica.fieldFrame import FieldFrame
from tkinter import ttk

path = os.path.join(pathlib.Path(__file__).parent.absolute())

class Inicio(tk.Tk):
    def __init__(self):
        self._c = 1
        super().__init__()
        self.title('WUNALLET')
        self.geometry("910x592")
        self.option_add('*tearOff',False)
        
        # ---- #
        # Menu #
        # ---- #
        self._barraMenu = tk.Menu(self)
        inicio = tk.Menu(self._barraMenu)
        inicio.add_command(label = "Descripcion", command = lambda: self.desplegarDescripcion())
        inicio.add_command(label = "Salir", command = lambda: self.destroy())
        self._barraMenu.add_cascade(label = "Inicio", menu = inicio)
        self.config(menu = self._barraMenu)
        
        # -------- #
        # Frame P1 #
        # -------- #
        self.frP1 = FramefrP1(self)
        self.frP1.pack(side='left',fill='both',expand='true')

        # -------- #
        # Frame P2 #
        # -------- #
        self.frP2 = FramefrP2(self)
        self.frP2.pack(side='right', fill='both', expand='true')

        # -------- #
        # Frame PD #
        # -------- #
        self.frPD = FramefrPD(self)



    # ----------------------------------------------------------------------------- #
    # función para mostrar la descripcion                                           #
    # Funcionamiento: cada vez que se presiona en el menú "Descripción" se          #
    # incremeta el valor de c, cuando c es par, se mostrará el frame PD, que        #
    # corresponde al desplegable de la información de la aplicación y cuando es     #
    # impar se muestran los frames P5 y P6, con la hoja de vida y las cuatro        #
    # imagenes                                                                      #
    # ----------------------------------------------------------------------------- #
    def desplegarDescripcion(self):
        self._c = self._c + 1
            
        if(self._c%2==0):
            self.frP2.pack_forget()
            self.frPD.pack(side='left',fill='both',expand='true')
        else:
            self.frPD.pack_forget()
            self.frP2.pack(side='right', fill='both', expand='true')

class FramefrPD(Frame):
    def __init__(self, ventana):
        super().__init__(ventana)
        self._ventana = ventana

        # -------- #
        # - frP7 - #
        # -------- #
        self._frP7 = Frame(self)
        self._frP7 = tk.Frame(self)
        self._frP7.pack(side="top", fill="both",padx=10,pady=10)
        
        self._textDescrip = tk.Text(self._frP7, height=50,font=('Times New Roman',12))
        texto = "¡Bienvenido a Wunallet! Si deseas acceder a las funcionalidades por favor da click en ir a ventana principal. A la derecha puede encontrar información sobre los desarrolladores, y para ver una breve descripción del software puedes ir a la ruta Inicio -> Descripción."
        self._textDescrip.insert(tk.END, texto)
        self._textDescrip.config(state="disabled")
        self._frP7.pack(side="top")
        self._textDescrip.pack(side="top")

        self._frP7.pack(side='right', fill='both', expand='true')

   

# -------- #
# Frame P1 #
# -------- #
class FramefrP1(Frame):
    contador = 0
    def __init__(self, ventana):
        super().__init__(ventana)
        self._ventana = ventana

        # ---- #
        # frP3 #
        # ---- #
        
        self._frP3 = Frame(self, height="420")
        
        textoNombreSaludo = "¡Bienvenido a Wunallet!"
        self._labelSaludo = Label(self._frP3, text = textoNombreSaludo, font = ("Verdana", 16), fg = "#AD3DE1")
        self._labelSaludo.pack(side="top",padx=10,pady=10)

        self._frP3.pack(side="top", fill="x",padx=10,pady=10)

        # ------ #
        # frP4_1 #
        # ------ #


        self._frP4 = tk.Frame(self)
        self._frP4.pack(side="bottom", fill="both",expand="true",padx=10,pady=10)

        # ---------- #
        # - frP4_1 - #
        # ---------- #
        
        self._frImgSistema = Frame(self._frP4)
        # Imagen inicial 
        imagenIterante = ImageTk.PhotoImage(Image.open(path+"/capaGrafica/img/sistema1.jpg"))
        labelImagenSistema = tk.Label(self._frImgSistema, image = imagenIterante)
        labelImagenSistema.image = imagenIterante
        labelImagenSistema.bind("<Leave>",self.siguienteImagen)
        labelImagenSistema.pack()
        self.labelImagenSistema = labelImagenSistema

        self._frImgSistema.pack(side="top", fill="both",expand="true")

        # ---------- #
        # - frP4_2 - #
        # ---------- #  

        
        self._frBtVentanaPrincipal = Frame(self._frP4)

        style = ttk.Style()
        style.map("C.TButton",
            foreground=[('pressed', 'red'), ('active', 'blue')],
            background=[('pressed', '!disabled', 'black'), ('active', 'white')]
            )

        self._boton = ttk.Button(self._frBtVentanaPrincipal, text = "Ingresar",style="C.TButton", command = self.abrir_ventana_principal)
        self._boton.pack()
        self._frBtVentanaPrincipal.pack(side="bottom", fill="both",expand="true")

    # ----------------------------------------------------------------------------- #
    # Función para abrir la ventana PP                                              #
    # Funcionamiento: cuando se ejecuta el boton ingresar se ejecuta esta función   #
    # haciendo que esta ventana se destruya y se invoque la ventana que contiene    #
    # las funcionalidades                                                           #
    # ----------------------------------------------------------------------------- #
    def abrir_ventana_principal(self):
        self._ventana.destroy()
        v_p = V_P()
        # v_p.mainloop()

    # ----------------------------------------------------------------------------- #
    # Función para cambiar la foto del sistema                                      #
    # Funcionamiento: cuenta cada vez que el cursor pasa por encima del frame en    #
    # el que se encuentra la imagen, este conteo se escala en un rango de 0-4       #
    # imprimiendo la imagen que tiene el nombre "sistema"+(valorEscalado +1)+".jpg" #
    # ----------------------------------------------------------------------------- #
    def siguienteImagen(self,event):
        FramefrP1.contador = (FramefrP1.contador+1)%5
        new = ImageTk.PhotoImage(Image.open(path+"/capaGrafica/img/sistema"+str(FramefrP1.contador+1)+".jpg"))
        self.labelImagenSistema.config(image=new)
        self.labelImagenSistema.image = new    


# ---- #
# frP2 #
# ---- #

class FramefrP2(Frame):
    _contadorIntegrante = 0

    def __init__(self, ventana):
        super().__init__(ventana)
        
        # -------- #
        # - frP5 - #
        # -------- #
        self._frP5 = Frame(self)

        n_inicial = 0
        self._frP5 = tk.Frame(self)
        self._lblHV = tk.Text(self._frP5, height=5,font=('Times New Roman',12))

        # Despliegue del primer documento de texto 

        with open(path+"/capaGrafica/textos/"+str(n_inicial)+".txt",encoding="utf-8") as f:
            texto = f.read()
        self._lblHV.insert(tk.END, texto)
        self._lblHV.bind("<Button-1>", self.siguienteIntegrante)
        self._lblHV.config(state="disabled")
        self._frP5.pack(side="top")
        self._lblHV.pack(side="top")
      
        self._frP5.pack(side="top", fill="x",padx=10,pady=10)

        # -------- #
        # - frP6 - #
        # -------- #
        
        self._frP6 = Frame(self)

        imgHV1 = ImageTk.PhotoImage(Image.open(path+"/capaGrafica/img/"+str(n_inicial)+"HV1.jpg"))
        imgHV2 = ImageTk.PhotoImage(Image.open(path+"/capaGrafica/img/"+str(n_inicial)+"HV2.jpg"))
        imgHV3 = ImageTk.PhotoImage(Image.open(path+"/capaGrafica/img/"+str(n_inicial)+"HV3.jpg"))
        imgHV4 = ImageTk.PhotoImage(Image.open(path+"/capaGrafica/img/"+str(n_inicial)+"HV4.jpg"))


        iHV1 = tk.Label(self._frP6, image = imgHV1)
        iHV1.image = imgHV1
        iHV1.grid(row=0, column=0)
        self.iHV1 = iHV1
    
        iHV2 = tk.Label(self._frP6, image = imgHV2)
        iHV2.ima1e = imgHV2
        iHV2.grid(row=0, column=1)
        self.iHV2 = iHV2
 
        iHV3 = tk.Label(self._frP6, image = imgHV3)
        iHV3.ima1e=imgHV3
        iHV3.grid(row=1, column=0)
        self.iHV3 = iHV3

        iHV4 = tk.Label(self._frP6, image = imgHV4)
        iHV4.ima1e = imgHV4
        iHV4.grid(row=1, column=1)
        self.iHV4 = iHV4

        self._frP6 = self._frP6



        self._frP6.pack(side="bottom", fill="both",expand="true",padx=10,pady=10)


    # ------------------------------------------------------------------------- #
    # función para cambiar el integrante en el documento de texto y en las fotos #
    # Funcionamiento: cada vez que se ejecuta el click sobre el frame P5, se    #
    # lleva un conteo, este conteo se coloca en una escala de 0-4, de tal forma #
    # que siempre se tenga un número entre 0-3, y con este número se llama a la #
    # imagen y texto asociado a un integrante                                   #
    # ------------------------------------------------------------------------- #

    def siguienteIntegrante(self, event):
        self._contadorIntegrante = (self._contadorIntegrante+1)%4

        with open(path+"/capaGrafica/textos/"+str(self._contadorIntegrante)+".txt",encoding="utf-8") as f:
            textoHV = f.read()
        self._lblHV.config(state="normal")
        self._lblHV.delete("1.0", "end-1c")
        self._lblHV.insert(tk.END, textoHV)
        self._lblHV.config(state="disabled")


        imgHV1 = ImageTk.PhotoImage(Image.open(path+"/capaGrafica/img/"+str(self._contadorIntegrante)+"HV1.jpg"))
        imgHV2 = ImageTk.PhotoImage(Image.open(path+"/capaGrafica/img/"+str(self._contadorIntegrante)+"HV2.jpg"))
        imgHV3 = ImageTk.PhotoImage(Image.open(path+"/capaGrafica/img/"+str(self._contadorIntegrante)+"HV3.jpg"))
        imgHV4 = ImageTk.PhotoImage(Image.open(path+"/capaGrafica/img/"+str(self._contadorIntegrante)+"HV4.jpg"))

        #Create a Label Widget to display the text or Image
        self.label1 = tk.Label(self._frP6, image = imgHV1)
        self.label1.image = imgHV1
        self.label1.grid(row=0, column=0)
    
        self.label2 = tk.Label(self._frP6, image = imgHV2)
        self.label2.ima1e = imgHV2
        self.label2.grid(row=0, column=1)
 
        self.label3 = tk.Label(self._frP6, image = imgHV3)
        self.label3.ima1e=imgHV3
        self.label3.grid(row=1, column=0)

        self.label4 = tk.Label(self._frP6, image = imgHV4)
        self.label4.ima1e = imgHV4
        self.label4.grid(row=1, column=1)