from email import header
import tkinter as tk
from tkinter import messagebox,ttk
from tokenize import Double

from setuptools import Command
from Wunallet.capaGrafica.fieldFrame import FieldFrame
from Wunallet.capaGrafica.pairButton import PairButton

# Importación clases manejo de excepciones

from Wunallet.capaLogica.exceptions.ErrorCamposVacios import ErrorCamposVacios
from Wunallet.capaLogica.exceptions.ErrorDeTipo import ErrorDeTipo
from Wunallet.capaLogica.exceptions.ErrorExtraccion import ErrorExtraccion
from Wunallet.capaLogica.exceptions.ErrorCuentaCC import ErrorCuentaCC
from Wunallet.capaLogica.exceptions.ErrorNoSaldo import ErrorNoSaldo
from Wunallet.capaLogica.exceptions.ErrorMaximoNoInscrito import ErrorMaximoNoInscrito

# Importamos las clases de la aplicación
# Se imoprtan las clases con información de los clientes

from Wunallet.capaLogica.gestorAplicacion.infoClientes.banco import Banco
from Wunallet.capaLogica.gestorAplicacion.infoClientes.perfilCrediticio import PerfilCrediticio
from Wunallet.capaLogica.gestorAplicacion.infoClientes.usuario import Usuario
from Wunallet.capaLogica.gestorAplicacion.infoClientes.comportamientoDePago import comportamientoDePago

# Se imoprtan las clases con información de los productos financieros
from Wunallet.capaLogica.gestorAplicacion.productosFinancieros.ahorro import Ahorro
from Wunallet.capaLogica.gestorAplicacion.productosFinancieros.bajoMonto import BajoMonto
from Wunallet.capaLogica.gestorAplicacion.productosFinancieros.corriente import Corriente
from Wunallet.capaLogica.gestorAplicacion.productosFinancieros.credito import Credito
from Wunallet.capaLogica.gestorAplicacion.productosFinancieros.cuenta import Cuenta
from Wunallet.capaLogica.gestorAplicacion.infoClientes.usuario import Usuario

class V_P(tk.Tk):

    def __init__(self):

        #-----------------------#
        # FUNCIONES AUXILIDARES #
        #-----------------------#

        # Función para chequear si un elemento puede castearse a entero
        def canBeInt(candidato):
            try:
                int(candidato)
                return True
            except:
                return False

        # Función para eliminar los widget asociados a un frame
        def clearFrame(frame):
            for widget in frame.winfo_children():
                widget.destroy()

        #-------------------#
        # OBJETOS DE PRUEBA #
        #-------------------#

        # USUARIOS
        juanPerez = Usuario(None,1000000,int(10),None)
        hernestoPerez = Usuario(None,2000000,int(98),None)

        # BANCOS
        Unalombia = Banco("Unalombia",1.6)
        PooBanco = Banco("PooBanco",2.5)
        QuitaVivienda = Banco("QuitaVivienda",36.0)

        # CUENTAS
        cuenta1 = Ahorro(nroCuenta=89,titular=juanPerez, saldo=10000.0 ,banco=QuitaVivienda,tipoDeCuenta="ahorro",tasaDeInteres=2.5)
        cuenta3 = Corriente(23,juanPerez,50000000.0,Unalombia,"corriente",1.2)
        cuenta2 = BajoMonto(69,hernestoPerez, 1000000.0,PooBanco, "bajoMonto", 2.2,3000000.0,3000000.0)
        cuenta4 = BajoMonto(26,hernestoPerez, 14000.0,Unalombia, "bajoMonto", 1.3,200000.0,200000.0)

        listaUsuarios = [juanPerez, hernestoPerez]
        variables = vars()
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

        def archivoSalir():
            # Importación de la aplicacion de inicio

            from Wunallet.inicio import Inicio
            ventana.destroy()
            ini = Inicio()
            ini.mainloop()

        archivo.add_command(label="Aplicación",command=archivoAplicacion)
        archivo.add_command(label="Salir",command=archivoSalir)


        # Estructura menu Procesos y Consultas

        menuFuncionalidades = tk.Menu(menuPrincipal)
        procesosYconsultas.add_cascade(label="Funcionalidades",menu=menuFuncionalidades)

        # Frame para mostrar los resultados
        resultado = tk.Frame(ventana,width=400,height=250)
        # Selección De Usuario
        frameF1 =  tk.Frame(ventana,width=800,height=250) # Frame para el formulario de login
        frameF2 =  tk.Frame(ventana,width=800,height=250) # Frame para los botones

        FieldFrame(frame=frameF1,
                        tituloFuncion="Selección de usuario",
                        descripcion="A continuación seleccione el usuario con el que desea ingresar. Una vez ingrese\n dirijace al menu de Procesos y Consultas, alli podra encontrar un listado de\n funcionalidades de la cuales podra hacer uso con su usuario.",
                        tituloCriterios="Criterio",
                        criterios= ["Usuario"],
                        tituloValores= "Valor",
                        valores= [""])

        botonesUsuario=PairButton(frame=frameF2,
                LBotonTitulo="Aceptar")
        
        # Frame de login al sistema
        def values_frameF0():
            global usuarioActivo
            criterio = ["Usuario"]
            inputsF0 = {} 
            for widget in frameF1.winfo_children():
                if isinstance(widget, tk.Entry):
                    inputsF0[criterio[0]] = widget.get()

                    # Chequeo de campos vacíos
                    if any(inputsF0.get(entry)=="" for entry in inputsF0):
                        try:
                            raise ErrorCamposVacios()
                        except:
                            messagebox.showerror(ErrorCamposVacios.mensajeGeneral, ErrorCamposVacios().getMensajeEspecifico())
                            return


                    # Chequeo de tipo en el input
                    if (not canBeInt(inputsF0[criterio[0]])) or (int(inputsF0[criterio[0]])<0):
                        try:
                            raise ErrorDeTipo("El número de cédula debe ser un entero positivo")
                        except:
                            messagebox.showerror(ErrorDeTipo.mensajeGeneral,
                                    ErrorDeTipo("El número de cédula debe ser un entero positivo").getMensajeEspecifico())
                            return

                    # Si el input es correcto se itera sobre todas las variables y si alguna es instancia de Usuario y su atributo 
                    # cédula coincide con el valor ingresado, se fija como usuario activo durante el resto del programa y 
                    # se le indica qué hacer al usuario mediante la GUI.
                    for usuario in listaUsuarios:
                        if getattr(usuario,"_cc") == int(inputsF0[criterio[0]]):
                            messagebox.showinfo("Usuario",
                                    f"Usted selecciono {int(inputsF0[criterio[0]])}.\n Ahora diríjase al menu de Procesos y Consultas")
                            widget.configure(state="disable")
                            usuarioActivo = usuario
                            return
                    widget.delete(0,last="end") 
                    try:
                        raise ErrorExtraccion("El", "usuario")
                    except:
                        messagebox.showerror(ErrorExtraccion.mensajeGeneral, 
                                ErrorExtraccion("El", "usuario").getMensajeEspecifico())

                
        getattr(botonesUsuario,'_LBoton').config(command=values_frameF0)
        getattr(botonesUsuario,'_RBoton').config(command=lambda :PairButton.borrarCampos(frameVer))
        frameF1.pack(expand=True,anchor='s')
        frameF2.pack(expand=True,anchor='n')

        # Frames para el menu Procesos y Consultas

        frameInscribir =  tk.Frame(ventana,width=400,height=250)
        frameVer = tk.Frame(ventana,width=400,height=250)
        frameSolicitar = tk.Frame(ventana,width=400,height=250)
        frameRomper = tk.Frame(ventana,width=400,height=250)
        frameTransferir = tk.Frame(ventana,width=400,height=250)
        frameHistoriales = tk.Frame(ventana,width=800,height=500)

                    
        # Se debe definir una función para esconder los frames abiertos cuando se abre otro
        def hide_all_frames():
            frameF1.pack_forget()
            frameF2.pack_forget()
            frameInscribir.pack_forget()
            #PairButton.borrarCampos(frameInscribir)
            frameVer.pack_forget()
            #PairButton.borrarCampos(frameVer)
            frameSolicitar.pack_forget()
            #PairButton.borrarCampos(frameSolicitar)
            frameRomper.pack_forget()
            #PairButton.borrarCampos(frameRomper)
            frameTransferir.pack_forget()
            #PairButton.borrarCampos(frameTransferir)
            resultado.pack_forget()
            frameHistoriales.pack_forget()
            

        # La función F1 define el procesamiento correspondiente a la funcionalidad Inscribir cuenta. En ella se presenta un
        # formulario que tras ser correctamente llenado procede a verificar la existencia de la cuenta objetivo así como que 
        # la cédula ingresada sí coincida con la cédula del presunto titutal. De ser así, el procedo culmina de manera exitosa
        # inscribiendo la cuenta al usuario y notificándole mediante la GUI

        def F1():
            hide_all_frames()
            clearFrame(frameInscribir) 

            # Presentación del formulario
            FieldFrame(frame=frameInscribir,
                        tituloFuncion="Inscribir Cuenta",
                        descripcion='''Esta funcionalidad te permite guardar una cuenta que uses frecuentemente. Así no tendrás que
                                ingresar sus datos cada vez que quieras transferir pues quedará asociada a tu usuario.''',
                        tituloCriterios="Criterio",
                        criterios= ["Banco", "Tipo Cuenta", "Numero Cuenta", "Numero Cedula"],
                        tituloValores= "Valor",
                        valores= ["","","",""])

            # Presentación de los botones
            botonesInscribir=PairButton(frame=frameF2,
                LBotonTitulo="Aceptar")

            # Esta función es la encargada de procesar, desde la lógica del sistema, los datos ingresados por el usuario para 
            # realizar de forma exitosa la inscripción o en su defecto notificar al usuario sobre los errores en el proceso.
            def values_frameF1():
                criterios = ["Banco", "Tipo Cuenta", "Numero Cuenta", "Numero Cedula"]
                inputsF1 = {}

                # Obtención de todos los inputs del formulario
                for widget,criterio in zip([entry for entry in frameInscribir.winfo_children() if isinstance(entry,tk.Entry) or isinstance(entry,ttk.Combobox)],criterios):
                    inputsF1[criterio] = widget.get()

                # Chequeo de campos vacíos
                if any(inputsF1.get(entry)=="" for entry in inputsF1):
                    try:
                        raise ErrorCamposVacios()
                    except:
                        messagebox.showerror(ErrorCamposVacios.mensajeGeneral, ErrorCamposVacios().getMensajeEspecifico())
                        return

                # Chequeo de tipo en el input
                if any(not canBeInt(inputsF1.get(entry)) or  int(inputsF1.get(entry))<0 for entry in list(inputsF1)[2:]):
                    try:
                        raise ErrorDeTipo("Todos los campos deben ser enteros positivos")
                    except:
                        messagebox.showerror(ErrorDeTipo.mensajeGeneral,
                                ErrorDeTipo("Todos los campos deben ser enteros positivos").getMensajeEspecifico())
                        return

                # Proceso que ejecuta la funcionalidad en su aspecto lógico
                bancoInscribir = Banco.extraerBanco(_nombreBanco=inputsF1["Banco"])
                try:
                    cuentaInscribir=bancoInscribir.extraerCuenta(nroCuenta=int(inputsF1["Numero Cuenta"]))
                except:
                        try:
                            raise ErrorExtraccion("El", f"número de cuenta {inputsF1['Numero Cuenta']}",
                                    f" en {inputsF1['Banco']}")
                        except:
                            messagebox.showerror(ErrorExtraccion.mensajeGeneral, 
                                    ErrorExtraccion("El", f"número de cuenta {inputsF1['Numero Cuenta']}",
                                        f" en {inputsF1['Banco']}").getMensajeEspecifico())

                concuerdaUsuarioYCc = cuentaInscribir.getTitular().getCc()==int(inputsF1["Numero Cedula"])
                if (not concuerdaUsuarioYCc):
                    try:
                        raise ErrorCuentaCC(f"El número de cédula {inputsF1.get('Numero Cedula')}",
                                "la cuenta {inputsF1['Numero Cuenta'])}")
                    except:
                        messagebox.showerror(ErrorCuentaCC.mensajeGeneral, 
                                ErrorCuentaCC(f"El número de cédula {inputsF1.get('Numero Cedula')}", 
                                    f"la cuenta {inputsF1['Numero Cuenta']}").getMensajeEspecifico())                
                        return

                usuarioActivo.inscribir(numeroCuenta=int(inputsF1["Numero Cuenta"]),nombreBanco=inputsF1["Banco"])
                messagebox.showinfo("Exito","La inscripción ha sido exitosa")

            # Seteo de la función que ejecutará cada botón en la GUI
            getattr(botonesInscribir,'_LBoton').config(command=values_frameF1)
            getattr(botonesInscribir,'_RBoton').config(command=lambda :PairButton.borrarCampos(frameInscribir))

            # Posicionamiento de los frames usados para mostrar la pantalla de la funcionalidad
            frameInscribir.pack(expand=True,anchor='s')
            frameF2.pack(expand=True,anchor='n')
            
            
        # Funcionalidad Inscribir Cuentas
        menuFuncionalidades.add_command(label="Inscribir cuenta",command=F1)

        # La función F2 define el procesamiento correspondiente a la funcionalidad Ver historial de transacciones asociadas a 
        # una cuenta. En ella se presenta un combobox desde el cual seleccionar la cuenta de la que se desea hacer la consulta.
        # En caso de que la cuenta tenga historial para mostrar se hará, o de lo contrarió se le notificará al usuario mediante
        # una ventana emergente.
        def F2():
            hide_all_frames()
            clearFrame(frameVer)

            # Presentación del formulario
            FieldFrame(frame=frameVer,
                        tituloFuncion="Ver Historial",
                        descripcion="Esta funcionalidad consiste en mostrar el hisotorial de transferencias de una cuenta.",
                        tituloCriterios="Criterio",
                        criterios= ["Cuentas Disponibles"],
                        tituloValores= "Valor",
                        valores =[""],
                        val= [cuentas.getNroCuenta() for cuentas in usuarioActivo.getCuentasAsociadas()])
            
            # Esta función es la encargada de procesar, desde la lógica del sistema, los datos ingresados por el usuario para 
            # mostrar al usuario sus transacciones. Una vez chequeados los tipos de la información ingresada, se ejecutan los
            # métodos definidos en la cuenta que permiten extraer y mostrar en cadenas legibles y formateadas cada transacción
            # realizada desde y hasta la cuenta.

            def values_frameF2():
                inputsF2 = {}
                criterios = ["Cuentas Disponibles"]

                # Obtención de todos los inputs del formulario
                for widget,criterio in zip([entry for entry in frameVer.winfo_children() if isinstance(entry,ttk.Combobox)],criterios):
                    inputsF2[criterio] = widget.get()
                
                # Chequeo campos vacío
                if any(inputsF2.get(entry)=="" for entry in inputsF2):
                    try:
                        raise ErrorCamposVacios()
                    except:
                        messagebox.showerror(ErrorCamposVacios.mensajeGeneral, ErrorCamposVacios().getMensajeEspecifico())
                        return

                # Seleccionar el objeto cuenta que seleccionó el usuario mediante el número
                for cuentaAsociada in usuarioActivo.getCuentasAsociadas():
                    if cuentaAsociada.getNroCuenta() == int(inputsF2["Cuentas Disponibles"]):
                        cuenta = cuentaAsociada
                        
                # Se verifica si la cuenta seleccionada tiene alguna transacción para mostrar en su historial
                if len(cuenta.getHistorialTransferencia())==0:
                    messagebox.showinfo("Ver Historial",
                            f'La cuenta {int(inputsF2["Cuentas Disponibles"])} no tiene historial de transacciones')
                else:
                    hide_all_frames()
                    clearFrame(frameVer)
                    frameHistoriales.pack(expand=True,anchor='s')
                    labelHistoriales = tk.Label(frameHistoriales,text=cuenta.verHistorial(),height=500)
                    labelHistoriales.pack(expand=True,anchor="center")

            botonesVer= PairButton(frame=frameF2,
                                    LBotonTitulo="Aceptar")                        

            # Seteo de la función que ejecutará cada botón en la GUI
            getattr(botonesVer,'_LBoton').config(command=values_frameF2)
            getattr(botonesVer,'_RBoton').config(command=lambda :PairButton.borrarCampos(frameVer))

            # Posicionamiento de los frames usados para mostrar la pantalla de la funcionalidad
            frameVer.pack(expand=True,anchor='s')
            frameF2.pack(expand=True,anchor='n')

        menuFuncionalidades.add_command(label="Ver historial de transacciones",command=F2)

        # La función F3 define el procesamiento correspondiente a la funcionalidad Solicitar crédito. En ella se presenta un
        # formulario que tras ser correctamente llenado procede a verificar las condiciones y atributos del usuario para determinar
        # si se le otorga o no el préstamo solicitado. Tanto si se aprueba como si no el usuario es notificado de la decisión y sus
        # razones.
        def F3():
            hide_all_frames()
            clearFrame(frameSolicitar) 

            # Presentación del formulario
            FieldFrame(frame=frameSolicitar,
                        tituloFuncion="Solicitar Credito",
                        descripcion="Esta funcionalidad crea un credito a un usuario",
                        tituloCriterios="Criterio",
                        criterios= ["Banco","Cuentas Disponibles","Monto","Plazo"],
                        tituloValores= "Valor",
                        valores= ["","","",""],
                        val = [cuentas.getNroCuenta() for cuentas in usuarioActivo.getCuentasAsociadas()])

            # Esta función es la encargada de procesar, desde la lógica del sistema, los datos ingresados por el usuario para 
            # procesar la solicitud de crédito. Una vez chequeados los tipos de la información ingresada, se realizan 
            # comprobaciones sobre el historial crediticio de la persona y su capacidad de endeudamiento. De cumplir los
            # requisitos se concede la solicitud.
            def values_frameF3():
                inputsF3 = {}
                criterios = ["Banco","Cuentas Disponibles","Monto","Plazo"]

                # Obtención de todos los inputs del formulario
                for widget,criterio in zip([entry for entry in frameSolicitar.winfo_children() if isinstance(entry,tk.Entry) or isinstance(entry,ttk.Combobox)],criterios):
                    inputsF3[criterio] = widget.get()
                
                # Chequeo campos vacío
                if any(inputsF3.get(entry)=="" for entry in inputsF3):
                    try:
                        raise ErrorCamposVacios()
                    except:
                        messagebox.showerror(ErrorCamposVacios.mensajeGeneral, ErrorCamposVacios().getMensajeEspecifico())

                # Chequeo de tipo en el input (si alguna entrada no es entera o es menor a cero, se llama el error)
                if any(not canBeInt(inputsF3.get(entry)) or  int(inputsF3.get(entry))<0 for entry in list(inputsF3)[2:]):
                    try:
                        raise ErrorDeTipo("Todos los campos deben ser enteros positivos")
                    except:
                        messagebox.showerror(ErrorDeTipo.mensajeGeneral,
                                ErrorDeTipo("Todos los campos deben ser enteros positivos").getMensajeEspecifico())
                        return
                    
                if usuarioActivo.getCreditoActivo()!=None:
                        messagebox.showinfo("Credito","Esta cuenta ya tiene un credito activo")
                        return

                # Verificación de la información crediticia del usuario, y envío de la decisión tomada.
                bancoSol = Banco.extraerBanco(_nombreBanco=inputsF3["Banco"])

                ## DANIEL -> Este try nunca va a tirar un except porque la cuenta siempre sale del combobox que muestra precisamente
                # las cuentas asociadas del usuario, no?
                try:
                    cuentaSol = bancoSol.extraerCuenta(int(inputsF3["Cuentas Disponibles"]))
                    #cuentaSol= [cuenta for cuenta in usuarioActivo.getCuentasAsociadas() if cuenta.getNroCuenta()==int(inputsF3["Cuentas Disponibles"])][0]
                    credit=usuarioActivo.solicitarCredito(user=usuarioActivo,banco=bancoSol,monto=float(inputsF3.get("Monto")),plazo=int(inputsF3.get("Plazo")),cuentaSc=cuentaSol)
                    if credit ==1:
                        messagebox.showinfo("Credito","Credito rechazado por mal comportamiento crediticio")
                    elif credit==2:
                        messagebox.showinfo("Credito rechazado por falta de capacidad de endeudamiento")
                    else:
                        messagebox.showinfo("Credito",f'Tu solicitud de credito ha sido aprobada y tu saldo actual es: {str(cuentaSol.getSaldo()+float(inputsF3.get("Monto")))}')
                except:
                    try:
                        raise ErrorExtraccion("El", f"número de cuenta {inputsF3['Cuentas Disponibles']}",
                            f" en {inputsF3['Banco']}")
                    except:
                        messagebox.showerror(ErrorExtraccion.mensajeGeneral, 
                                ErrorExtraccion("El", f"número de cuenta {inputsF3['Cuentas Disponibles']}",
                                f" en {inputsF3['Banco']}").getMensajeEspecifico())
                

            botonesSolicitar=PairButton(frame=frameF2,
                LBotonTitulo="Aceptar")

            # Seteo de la función que ejecutará cada botón en la GUI
            getattr(botonesSolicitar,'_LBoton').config(command=values_frameF3)
            getattr(botonesSolicitar,'_RBoton').config(command=lambda :PairButton.borrarCampos(frameSolicitar))


            # Posicionamiento de los frames usados para mostrar la pantalla de la funcionalidad
            frameSolicitar.pack(expand=True,anchor='s')
            frameF2.pack(expand=True,anchor='n')

        menuFuncionalidades.add_command(label="Solicitar crédito",command=F3)


        # La función F4 define el procesamiento correspondiente a la funcionalidad Romper Topes. En ella se presenta un
        # combobox que permite seleccionar al usuario cuál de sus cuentas de bajo monto desea recategorizar a una cuenta de
        # ahorro. 
        def F4():
            hide_all_frames()
            clearFrame(frameRomper) 
            cuentasBajoMonto = [cuenta.getNroCuenta() for cuenta in usuarioActivo.getCuentasAsociadas() if isinstance(cuenta,BajoMonto)]
            # Notificación al usuario en caso de que la funcionalidad no aplique para ninguna de sus cuentas (es decir, el usuario
            # no tiene ninguna cuenta de tipo bajoMonto asociada)
            if len(cuentasBajoMonto)==0:
                habilitado = [False]
                messagebox.showinfo("Romper Topes","Esta funcionalidad no esta habilitada para tus cuentas.")
            else:
                habilitado = [None]
            
            # Presentación del formulario
            FieldFrame(frame=frameRomper,
                        tituloFuncion="Romper Topes",
                        descripcion="Esta funcionalidad consiste en cambiar de una cuenta de bajo monto a una de ahorros.",
                        tituloCriterios="Criterio",
                        criterios= ["Cuentas Disponibles"],
                        tituloValores= "Valor",
                        valores= [""],
                        val=cuentasBajoMonto,
                        habilitados=habilitado)

            # Esta función es la encargada de procesar, desde la lógica del sistema, los datos ingresados por el usuario para 
            # efectuar la ruptura de topes a una cuenta bajo monto. En esta, una vez verificado que el usuario desea efectuar
            # el proceso, se procede a verificar si cuenta con el saldo para hacerlo y en caso de que sí se organizan todos
            # los registros, a nivel de usuario y de banco, para dejar constancia de la nueva cuenta de ahorros y desreferenciar
            # la vieja cuenta de bajo monto.
            def values_frameF4():
                inputsF4 = {}
                criterios = ["Cuentas Disponibles"]

                # Obtención de todos los inputs del formulario
                for widget,criterio in zip([entry for entry in frameRomper.winfo_children() if isinstance(entry,tk.Entry) or isinstance(entry,ttk.Combobox)],criterios):
                    inputsF4[criterio] = widget.get()

                # Chequeo campos vacío
                if any(inputsF4.get(entry)=="" for entry in inputsF4):
                    try:
                        raise ErrorCamposVacios()
                    except:
                        messagebox.showerror(ErrorCamposVacios.mensajeGeneral, ErrorCamposVacios().getMensajeEspecifico())
                        return

                # Se pregunta si se desea continuar con el proceso
                continuar = messagebox.askokcancel("Confirmacion Romper Topes",
                '¡Recuerde! El procedimiento de romper topes consiste en transformar su cuenta de tipo Bajo monto'\
                ' a una cuenta de ahorros convencional, eliminando las limitaciones de este tipo de cuentas.\n' \
                'Este proceso tiene un costo de 15.000 pesos que pagará una unica vez.')

                if continuar:
                    # Seleccionar el objeto cuenta que seleccionó el usuario mediante el número
                    for cuentaAsociada in usuarioActivo.getCuentasAsociadas():
                        if cuentaAsociada.getNroCuenta()==int(inputsF4["Cuentas Disponibles"]):
                            cuentaObjetivo = cuentaAsociada

                    # cuentaObjetivo.romperTopes verifica si la cuenta se puede subir de categoría y de ser así
                    # retorna un True. En caso contrario retorna un false.
                    if not cuentaObjetivo.romperTopes():
                        try:
                            raise ErrorNoSaldo(cuentaObjetivo.getSaldo(), "15.000", "romper topes")
                        except:
                            messagebox.showerror(ErrorNoSaldo.mensajeGeneral,
                                    ErrorNoSaldo(cuentaObjetivo.getSaldo(), "15.000", "romper topes"))
                            return

                    # banco asociado a la cuenta de bajo monto que se eliminará
                    bancoCuentaObjetivo = cuentaObjetivo.getBanco()
                    # Se remueve la cuenta del banco
                    bancoCuentaObjetivo.removerCuenta(cuentaObjetivo)
                    # Se elimina la cuenta de bajo monto de las asociadas que tenia el usuario
                    usuarioActivo.removerCuentaAsociada(cuentaObjetivo)
                    # Se extrae el nuevo objeto cuenta de ahorro del banco objetivo mediante el nroCuenta que es el mismo de la
                    # cuenta bajo monto
                    numeroCuentaNueva = cuentaObjetivo.getNroCuenta()
                    cuentaNueva = bancoCuentaObjetivo.extraerCuenta(numeroCuentaNueva)

                    # Notificación al usuario
                    messagebox.showinfo("Romper Topes",f'Tu solicitud ha sido aprobada y tu nueva cuenta de ahorros quedó con' \
                            f'un saldo de {str(cuentaNueva.getSaldo())} pesos.')


            botonesRomper = PairButton(frame=frameF2,
                LBotonTitulo="Aceptar")

            # Seteo de la función que ejecutará cada botón en la GUI
            getattr(botonesRomper,'_LBoton').config(command=values_frameF4)
            getattr(botonesRomper,'_RBoton').config(command=lambda :PairButton.borrarCampos(frameRomper))

            # Posicionamiento de los frames usados para mostrar la pantalla de la funcionalidad
            frameRomper.pack(expand=True,anchor='s')
            frameF2.pack(expand=True,anchor='n')

        menuFuncionalidades.add_command(label="Romper topes",command=F4)

        # La función F5 define el procesamiento correspondiente a la funcionalidad Transferir. En ella se presenta un
        # combobox que permite seleccionar el tipo de transferencia que se desea realizar, y sobre dicha selección pueden o bien
        # desplegarse más formularios, o simplemente solicitarse una confirmación de pagos de crédito. Cada posible ejecución de
        # la transferencia se documenta adelante
        def F5():
            hide_all_frames()
            clearFrame(frameTransferir) 
            criteriosInicial =["Cuentas Disponibles","Tipo Transferencia"]


            # Presentación del formulario inicial
            FieldFrame(frame=frameTransferir,
                        tituloFuncion="Transferir",
                        descripcion="Esta funcionalidad permite pagar un credito o tranferir a otra cuenta.",
                        tituloCriterios="Criterio",
                        criterios= ["Cuentas Disponibles","Tipo Transferencia"],
                        tituloValores= "Valor",
                        valores= ["","","","","",""],
                        val=[cuentas.getNroCuenta() for cuentas in usuarioActivo.getCuentasAsociadas()])

            botonesTransferir = PairButton(frame=frameF2,
            LBotonTitulo="Aceptar")
            
            # Esta función es la encargada de procesar, desde la lógica del sistema, los datos ingresados por el usuario para 
            # determinar qué tipo de transferencia desea hacer el usuario.
            def values_frameF5():
                # Se obtienen los inputs iniciales
                inputsInicial = {}
                for widget,criterio in zip([entry for entry in frameTransferir.winfo_children() if isinstance(entry,tk.Entry) or isinstance(entry,ttk.Combobox)],criteriosInicial):
                        inputsInicial[criterio] = widget.get()

                # Si hay algun input vacio, se saca una ventana emergente, sino se procede a verificar los tipos de entrada
                if any(inputsInicial.get(entry)=="" for entry in inputsInicial):
                    try:
                        raise ErrorCamposVacios()
                    except:
                        messagebox.showerror(ErrorCamposVacios.mensajeGeneral, ErrorCamposVacios().getMensajeEspecifico())
                        return

                # Capturamos el objeto cuenta asociada al usuario que se seleccionó mediante el número
                for cuentaAsociada in usuarioActivo.getCuentasAsociadas():
                    if cuentaAsociada.getNroCuenta() == int(inputsInicial["Cuentas disponibles"]):
                        cuentaOrigen = cuentaAsociada

                # Si la selección fue de pagar crédito, se verifica que el usuario tenga activo un crédito y de ser así, se 
                # solicita confirmación para posteriormente realizar las comprobaciones de saldo que permitan hacer un pago 
                # exitoso.
                if inputsInicial.get("Tipo Transferencia")=="Pagar credito":
                    if usuarioActivo.getCreditoActivo() is None:
                        messagebox.showinfo("Credito","No tienes ningun credito activo para pagar.")
                    else:
                        creditoActivo = usuarioActivo.getCreditoActivo()
                        messagebox.showinfo("Credito",f'Tu credito es de {creditoActivo.getDeuda()} y pagaras una cuota de {creditoActivo.getCuotaMensual()}.')
                        opcion=messagebox.askokcancel("Confirma Pago","¿Desea confirmar el pago del credito?")
                        if opcion:
                            exito = cuentaOrigen.transferir(creditoActivo)
                            if exito:
                                messagebox.showinfo("Transferencia Exitosa",f'Tu pago ha sido exitoso. Tu credito restante es de {creditoActivo.getDeuda()-creditoActivo.getCuotaMensual()}')
                                messagebox.showinfo("Transferencia Exitosa",f'Tu cuenta queda con un saldo de {cuentaOrigen.getSaldo()}.')
                            else:
                                messagebox.showerror("Transferencia Rechazada","Tu pago ha sido rechazado ya que no cuentas con saldo suficiente o tu producto de origen no permite mover el valor indicado.")

                    # Si la decisión fue transferir a una cuenta inscrita, se refresca el frame de forma que el usuario pueda 
                    # seleccionar mediante un combobox entre sus cuentas inscritas.u
                    if inputsInicial.get("Tipo Transferencia")=="A otra cuenta - Inscrita":
                        if len(usuarioActivo.getListaIncritos())==0:
                            messagebox.showinfo("Transferencia-Inscrita","No tiene cuentas inscritas")
                        else:

                            clearFrame(frameTransferir)

                            FieldFrame(frame=frameTransferir,
                                tituloFuncion="Transferir",
                                descripcion="Esta funcionalidad consiste permite bien sea pagar un credito o tranferir a otra cuenta.",
                                tituloCriterios="Criterio",
                                criterios= ["Cuentas Disponibles","Valor"],
                                tituloValores= "Valor",
                                valores= ["",""],
                                val=[cuentas.getNroCuenta() for cuentas in usuarioActivo.getListaIncritos()])
                            botonesTransferir = PairButton(frame=frameF2,
                                    LBotonTitulo="Aceptar")
                        
                        # Esta función ejecutará el proceso de transferencia a la cuenta inscrita que el usuario seleccionó desde
                        # el frame, notificándole en caso de haber algún error o retornándole mediante una ventana emergente el 
                        # éxito de la operación.
                        def values_FrameIns():
                            inputsIns = {}
                            for widget,criterio in zip([entry for entry in frameTransferir.winfo_children()
                                if isinstance(entry,tk.Entry) or isinstance(entry,ttk.Combobox)],["Cuentas Disponibles","Valor"]):
                                    inputsIns[criterio] = widget.get()

                            # Chequeo de campos vacíos
                            if any(inputsIns.get(entry)=="" for entry in inputsIns):
                                try:
                                    raise ErrorCamposVacios()
                                except:
                                    messagebox.showerror(ErrorCamposVacios.mensajeGeneral, 
                                            ErrorCamposVacios().getMensajeEspecifico())
                                    return

                            # Chequeo de tipo
                            if float(inputsIns.get("Valor"))<0:
                                try:
                                    raise ErrorDeTipo()
                                except:
                                    messagebox.showerror(ErrorDeTipo.mensajeGeneral,
                                            ErrorDeTipo("El valor debe ser positivo"))
                                    return

                            # Capturamos el objeto cuenta asociada al usuario que se seleccionó mediante el número
                            for cuentaAsociada in usuarioActivo.getListaInscritos():
                                if cuentaAsociada.getNroCuenta()==int(inputsIns["Cuentas Disponibles"]):
                                    cuentaDestino = cuentaAsociada

                            bancoDestino = cuentaDestino.getBanco()

                            if not cuentaDestino in bancoDestino.getListaCuentas():
                                messagebox.showinfo("Transferencia-Inscrita",
                                        "La cuenta inscrita que ha seleccionado ya no esta disponible, por lo tanto sera eliminada de su lista de cuentas inscritas.")
                                usuarioActivo.removerCuentaInscrita(cuentaDestino)

                            else:
                                decision=messagebox.askokcancel("Confirma Transferencia","¿Desea confirmar la transferencia?")
                                if decision:
                                    exito = cuentaOrigen.transferir(cuentaDestino,float(inputsIns.get("Valor")))
                                    if exito:
                                        messagebox.showinfo("Transferencia Exitosa",f'Transferencia exitosa.')
                                        messagebox.showinfo("Transferencia Exitosa",f'Tu cuenta queda con un saldo de {cuentaOrigen.getSaldo()}.')
                                    else:
                                        messagebox.showerror("Transferencia Rechazada","Tu pago ha sido rechazado ya que no cuentas con saldo suficiente o tu producto de origen no permite mover el valor indicado.")
                                    
                        # Seteo de la función que ejecutará cada botón en la GUI
                        getattr(botonesTransferir,'_LBoton').config(command=values_FrameIns)
                        getattr(botonesTransferir,'_RBoton').config(command=lambda :PairButton.borrarCampos(frameTransferir))
                        
                    # En caso de que el usuario seleccione realizar una transferencia a una cuenta no inscrita, se actualiza el
                    # formulario que pedirá todos los datos requeridos para realizar la transferencia a la cuenta destino.
                    else:
                        clearFrame(frameTransferir) 
                        FieldFrame(frame=frameTransferir,
                            tituloFuncion="Transferir - Cuenta No Inscrita",
                            descripcion="Está realizando una transferencia a una cuenta no inscrita. Recuerde que el saldo máximo que puede transferir es de 3'000.000",
                            tituloCriterios="Criterio",
                            criterios= ["Banco Destino","Numero Cuenta","Valor"],
                            tituloValores= "Valor",
                            valores= ["","",""])
                        botonesTransferir = PairButton(frame=frameF2,
                                LBotonTitulo="Aceptar")

                        # Esta función se encarga de verificar que los datos ingresados sean válidos, y de ser así, procede a 
                        # realizar la transferencia entre las cuentas dejando los registros correspondientes en ambas mediante
                        # los métodos ya desarrollados para las clases.
                        def values_FrameNoIns():
                            inputsNoIns = {}
                            for widget,criterio in zip([entry for entry in frameTransferir.winfo_children() if isinstance(entry,tk.Entry) or isinstance(entry,ttk.Combobox)],["Banco","Numero Cuenta","Valor"]):
                                    inputsNoIns[criterio] = widget.get()

                            # Chequeo campos vacío
                            if any(inputsNoIns.get(entry)=="" for entry in inputsNoIns):
                                try:
                                    raise ErrorCamposVacios()
                                except:
                                    messagebox.showerror(ErrorCamposVacios.mensajeGeneral, 
                                            ErrorCamposVacios().getMensajeEspecifico())
                                    return

                            # Chequeo de tipo en el input valor
                            if float(inputsNoIns.get("Valor"))<0:
                                try:
                                    raise ErrorDeTipo()
                                except:
                                    messagebox.showerror(ErrorDeTipo.mensajeGeneral,
                                            ErrorDeTipo("El valor debe ser positivo"))
                                    return

                            # Chequeo de tipo en el input numero cuenta
                            if (not canBeInt(inputsNoIns.get("Numero Cuenta"))) or (int(inputsNoIns.get("Numero Cuenta"))<0):
                                try:
                                    raise ErrorDeTipo("El número de cuenta debe ser un entero positivo")
                                except:
                                    messagebox.showerror(ErrorDeTipo.mensajeGeneral,
                                            ErrorDeTipo("El número de cuenta debe ser un entero positivo").getMensajeEspecifico())
                                    return

                            try:
                                bancoDestino = Banco.extraerBanco(inputsNoIns.get("Banco"))
                            except:
                                    try:
                                        raise ErrorExtraccion("El", f"número de cuenta {inputsNoIns.get('Numero Cuenta')}",
                                                f" en {inputsNoIns.get('Banco')}")
                                    except:
                                        messagebox.showerror(ErrorExtraccion.mensajeGeneral, 
                                                ErrorExtraccion("El", f"número de cuenta {inputsNoIns.get('Numero Cuenta')}",
                                                    f" en {inputsNoIns.get('Banco')}").getMensajeEspecifico())
                                        return


                            cuentaDestino = bancoDestino.extraerCuenta(int(inputsNoIns.get("Numero Cuenta")))

                            # Notificación en caso de que la cuenta inscrita ya no esté disponible (debido a que era de bajo monto
                            # y realizó una recategorización a ahorros)
                            if not cuentaDestino in bancoDestino.getListaCuentas():
                                messagebox.showinfo("Transferencia-Inscrita",
                                        "La cuenta inscrita que ha seleccionado ya no esta disponible, por lo tanto sera eliminada de su lista de cuentas inscritas.")
                                usuarioActivo.removerCuentaInscrita(cuentaDestino)

                            # Confirmación, notificación y realización de la transferencia
                            else:
                                decision=messagebox.askokcancel("Confirma Transferencia","¿Desea confirmar la transferencia?")
                                if decision:
                                    if float(inputsNoIns.get("Valor"))>3000000:
                                        try:
                                            raise ErrorMaximoNoInscrito()
                                        except:
                                            messagebox.showerror(ErrorMaximoNoInscrito.mensajeGeneral,
                                                    ErrorMaximoNoInscrito.getMensajeEspecifico())
                                    else:
                                        exito = cuentaOrigen.transferir(cuentaDestino,float(inputsNoIns.get("Valor")))
                                        if exito:
                                            messagebox.showinfo("Transferencia Exitosa",
                                                    f'Transferencia exitosa.\n El saldo de su cuenta es de {cuentaOrigen.getSaldo()}.')
                                        else:
                                            try:
                                                raise ErrorNoSaldo()
                                            except:
                                                messagebox.showerror(ErrorNoSaldo.mensajeGeneral,
                                                        ErrorNoSaldo(considerarLimiteSaldo=True).getMensajeEspecifico())

                        # Seteo de la función que ejecutará cada botón en la GUI
                        getattr(botonesTransferir,'_LBoton').config(command=values_FrameNoIns)
                        getattr(botonesTransferir,'_RBoton').config(command=lambda :PairButton.borrarCampos(frameTransferir))

            # Seteo de la función que ejecutará cada botón en la GUI
            getattr(botonesTransferir,'_LBoton').config(command=values_frameF5)
            getattr(botonesTransferir,'_RBoton').config(command=lambda :PairButton.borrarCampos(frameTransferir))

            # Posicionamiento de los frames usados para mostrar la pantalla de la funcionalidad
            frameTransferir.pack(expand=True,anchor='s')
            frameF2.pack(expand=True,anchor='n')
        menuFuncionalidades.add_command(label="Transferir",command=F5)

        # Estructura menu AYUDA

        def acercaDe():
            messagebox.showinfo("Acerca de:","Daniel \n Diego \n David \n Cesar")

        ayuda.add_command(label="Autores:",command=acercaDe)

        ventana.mainloop()
