import tkinter as tk
import pathlib
import os
from tkinter import Label, Entry, Button, Text, PhotoImage, Frame, INSERT, scrolledtext
from PIL import Image,ImageTk
import os 
import pathlib
import codecs
import io
import sys
from Wunallet.UI_Wunalet import V_P
from Wunallet.capaGrafica.fieldFrame import FieldFrame

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



    # ----------------------------------- #
    # función para mostrar la descripcion #
    # ----------------------------------- #
    def desplegarDescripcion(self):
        self._c = self._c + 1
        print(self._c)
            
        if(self._c%2==0):
            self.frP2.pack_forget()
            self.frPD.pack(side='left',fill='both',expand='true')
            # .pack_forget()
        else:
            # self._frP7.pack(side='right', fill='both', expand='true')
            self.frPD.pack_forget()
            self.frP2.pack(side='right', fill='both', expand='true')

        # self.frP1._labelSaludoC3.pack(side="bottom",anchor="w")
        # self.frP1._labelSaludoC2.pack(side="bottom",anchor="w")
        # self.frP1._labelSaludoC1.pack(side="bottom",anchor="w")
        # self.frP1._textWel.pack(side="bottom",anchor="w")


class FramefrPD(Frame):
    def __init__(self, ventana):
        super().__init__(ventana)
        
        # -------- #
        # - frP7 - #
        # -------- #

        self._frP7 = Frame(self)

        n_inicial = 0
        self._frP7 = tk.Frame(self)
        self._frP7.pack(side="top", fill="both",padx=10,pady=10)
        self._lblHV = tk.Text(self._frP7, height=50,font=('Times New Roman',12))

        texto = "¡Bienvenido a Wunallet! Si deseas acceder a las funcionalidades por favor da click en ir a ventana principal. A la derecha puede encontrar información sobre los desarrolladores, y para ver una breve descripción del software puedes ir a la ruta Inicio -> Descripción."

        self._lblHV.insert(tk.END, texto)
        # self._lblHV.bind("<Button-1>", self.siguienteIntegrante)

        self._lblHV.config(state="disabled")
        self._frP7.pack(side="top")
        self._lblHV.pack(side="top")

        self._frP7.pack(side='right', fill='both', expand='true')

   


class FramefrP1(Frame):
    contador = 0
    def __init__(self, ventana):
        super().__init__(ventana)

        # Guardar la referncia a la ventana 

        self.ventana = ventana

        # Definir los Frames 

        # ---- #
        # frP3 #
        # ---- #
        
        self._frP3 = Frame(self, height="420")
        
        # Contenido del frame frP3
        
        textoNombreSaludo = "¡Bienvenido a Wunallet!"
        self._labelSaludo = Label(self._frP3, text = textoNombreSaludo, font = ("Verdana", 16), fg = "#AD3DE1")
        self._labelSaludo.pack(side="top",padx=10,pady=10)

        # textoContenido1 = "Si deseas acceder a las funcionalidades de click en ir a ventana principal. A la derecha puede encontrar información sobre los desarrolladores,"
        # self._labelSaludoC1 = Label(self._frP3,text =textoContenido1 )
        # self._labelSaludoC1.pack(side="bottom", fill="both",padx=10,pady=10)

        # textoContenido2 = "y para ver una breve descripción del software puedes ir a la ruta Inicio -> Descripción."
        # self._labelSaludoC2 = Label(self._frP3,text = textoContenido2 )
        # self._labelSaludoC2.pack(side="bottom", fill="both",padx=10,pady=10)

        textoContenido3 = ", y para ver una breve descripción del software puedes ir a la ruta Inicio -> Descripción."
        self._labelSaludoC3 = Label(self._frP3,text = textoContenido3 )
        # self._labelSaludoC3.pack(side="bottom",anchor="w")
        
        textoContenido2 = "A la derecha puede encontrar información sobre los desarrolladores"
        self._labelSaludoC2 = Label(self._frP3,text = textoContenido2 )
        # self._labelSaludoC2.pack(side="bottom",anchor="w")

        textoContenido1 = "Si deseas acceder a las funcionalidades por favor da click en ir a ventana principal."
        self._labelSaludoC1 = Label(self._frP3,text =textoContenido1 )
        # self._labelSaludoC1.pack(side="bottom",anchor="w")

        # self._textWel = tk.Text(self._frP3,height=5)
        # self._textWel.insert(tk.END,"Si deseas acceder a las funcionalidades por favor da click en ir a ventana principal. A la derecha puede encontrar información sobre los desarrolladores , y para ver una breve descripción del software puedes ir a la ruta Inicio -> Descripción.")


        
        # self._frP3.grid(row = 0, column = 0, pady=(10,10))
        # self._frP3.pack(side="top", fill="x",padx=10,pady=10)
        self._frP3.pack(side="top", fill="x",padx=10,pady=10)

        # ------ #
        # frP4_1 #
        # ------ #

        # self._frP4 = tk.Frame(self,bg="red")
        self._frP4 = tk.Frame(self)
        self._frP4.pack(side="bottom", fill="both",expand="true",padx=10,pady=10)

        # ---------- #
        # - frP4_1 - #
        # ---------- #
        
        # self._frImgSistema = Frame(self._frP4, bg="red")
        self._frImgSistema = Frame(self._frP4)
        self._frImgSistema.pack(side="top", fill="both",expand="true")
        
        # Imagen
        # self._boton = Button(frImgSistema, text = "Parte arriba", font = ("Verdana", 16), fg = "white", bg = "#198C3A", command = self.abrir_ventana_principal)
        # self._boton.pack()

        # self._imgSistema = ImageTk.PhotoImage(Image.open(path+"/img/sistema1.jpg"))
        # self._label = Label(self._frImgSistema,image= self._imgSistema)
        # self._label.pack(side="top", fill="y",padx=2,pady=2)


        
        imagenIterante = ImageTk.PhotoImage(Image.open(path+"/capaGrafica/img/sistema1.jpg"))
        #Create a Label Widget to display the text or Image
        labelImagenSistema = tk.Label(self._frImgSistema, image = imagenIterante)
        labelImagenSistema.image = imagenIterante
        labelImagenSistema.bind("<Leave>",self.siguienteImagen)
        labelImagenSistema.pack()
        self.labelImagenSistema = labelImagenSistema


        # self.image_size = (600,400)
        # carrusel = ImageTk.PhotoImage(Image.open(path+"/imagenes/carrusel1.JPG").resize(self.image_size, Image.ANTIALIAS))
        # #Create a Label Widget to display the text or Image
        # labelCarrusel = tk.Label(frameP4, image = carrusel, width=self.image_size[0]+10, height=self.image_size[1]+10)
        # labelCarrusel.image = carrusel
        # labelCarrusel.bind("<Leave>",self.cambiarCarrusel)
        # labelCarrusel.pack()
        # self.labelCarrusel = labelCarrusel
        

        # label2 = Label(self._frImgSistema,text="IMAGEN")
        # label2.pack(side="bottom", fill="both",padx=2,pady=2)

        # ---------- #
        # - frP4_2 - #
        # ---------- #  

        # self._frBtVentanaPrincipal = Frame(self._frP4, bg="green")
        self._frBtVentanaPrincipal = Frame(self._frP4)
        
         # Boton de acceso a la aplicacion abajo en P4

        self._boton = Button(self._frBtVentanaPrincipal, text = "Ingresar", command = self.abrir_ventana_principal)
        self._boton.pack()
        self._frBtVentanaPrincipal.pack(side="bottom", fill="both",expand="true")

    # ------------------------------- #
    # Método para abrir la ventana PP #
    # ------------------------------- #
    def abrir_ventana_principal(self):
        self.ventana.destroy()
        # Ventana_principal()
        # print("Lo intenté llamar")
        # print(path)
        # os.system(path+"/UI_Wunalet.py")
        v_p = V_P()
        v_p.mainloop()

    # --------------------------------------- #
    # Método para cambiar la foto del sistema #
    # --------------------------------------- #
    def siguienteImagen(self,event):
        FramefrP1.contador = (FramefrP1.contador+1)%5
        new = ImageTk.PhotoImage(Image.open(path+"/capaGrafica/img/sistema"+str(FramefrP1.contador+1)+".jpg"))
        #Create a Label Widget to display the text or Image
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

        # label5 = Label(self._frP5,text="frP5")
        # label5.pack(side="top", fill="both",padx=10,pady=10)

        n_inicial = 0
        self._frP5 = tk.Frame(self)
        self._frP5.pack(side="top", fill="x",padx=10,pady=10)
        self._lblHV = tk.Text(self._frP5, height=5,font=('Times New Roman',12))

        with open(path+"/capaGrafica/textos/"+str(n_inicial)+".txt",encoding="utf-8") as f:
            texto = f.read()
        print(str(texto))
        self._lblHV.insert(tk.END, texto)
        self._lblHV.bind("<Button-1>", self.siguienteIntegrante)

        self._lblHV.config(state="disabled")
        self._frP5.pack(side="top")
        self._lblHV.pack(side="top")

        # self.hv = hv

        
        # self._frP5 = self._frP5
        

        # -------- #
        # - frP6 - #
        # -------- #
        
        # self._frP6 = Frame(self,bg="purple")
        self._frP6 = Frame(self)

        # label6 = Label(self._frP6,text="frP5")
        # label6.pack(side="top", fill="both",padx=10,pady=10)


        #Create an object of tkinter ImageTk
        imgHV1 = ImageTk.PhotoImage(Image.open(path+"/capaGrafica/img/"+str(n_inicial)+"HV1.jpg"))
        imgHV2 = ImageTk.PhotoImage(Image.open(path+"/capaGrafica/img/"+str(n_inicial)+"HV2.jpg"))
        imgHV3 = ImageTk.PhotoImage(Image.open(path+"/capaGrafica/img/"+str(n_inicial)+"HV3.jpg"))
        imgHV4 = ImageTk.PhotoImage(Image.open(path+"/capaGrafica/img/"+str(n_inicial)+"HV4.jpg"))


        #Create a Label Widget to display the text or Image
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



        # self.cargarHVTexto(0)
        
        # for i in range(0, 4):
        #     label = Label(self._p6, width = 320, height = 240)
        #     (r, c) = FrameRight._posicion_imagen[i]
        #     label.grid(row=r, column=c)
        #     self._labels.append(label)
        #     # Se cargan las primeras imagenes
        #     self.cargarHVImagen(0, i)



    # # Se usa para mostrar la hoja de vida que sigue, aumentando el atributo next_hv
    # def proximo(self, _):
    #     if self._next_hv < 2:
    #         self._next_hv = self._next_hv + 1
    #     else:
    #         self._next_hv = 0

    #     self._photos = [None, None, None, None]
    #     self.cargarHVTexto(self._next_hv)
    #     for i in range(0, 4):
    #         self.cargarHVImagen(self._next_hv, i)


    # def cargarHVImagen(self, hv_num, numero):
    #     path = os.path.join(pathlib.Path(__file__).parent.parent.parent.absolute(),'src\\recursos\HV{0}{1}.png'.format(hv_num, numero))
    #     photo = PhotoImage(file = path)
    #     self._labels[numero].configure(image = photo)
    #     self._labels[numero].image = photo



    # # Carga el texto para la hoja de vida respecto al numero asignado

    # def cargarHVTexto(self, numero):
    #     self._text = Text(self._p5, height = 10, font = ("Verdana",10), width = 80)
    #     self._text.grid(row = 1, column = 0)
    #     self._text.bind('<Button-1>', self.proximo)

    #     path = os.path.join(pathlib.Path(__file__).parent.parent.parent.absolute(),'src\\recursos\HV{0}4.txt'.format(numero))

    #     with open(path, "r+") as hv_text:
    #         self._text.insert(INSERT, hv_text.read())

    def siguienteIntegrante(self, event):
        # print("Contadorcito en ..."+ str(self._contadorIntegrante))
        self._contadorIntegrante = (self._contadorIntegrante+1)%4
        # nombre = self._contadorIntegrante[self._contadorIntegrante]
        # with open(path+"/textos/"+str(n_inicial)+".txt",encoding="utf-8") as f:

        with open(path+"/capaGrafica/textos/"+str(self._contadorIntegrante)+".txt",encoding="utf-8") as f:
            textoHV = f.read()
        print(str(textoHV))
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