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
        cuenta4 = BajoMonto(26,hernestoPerez, 6000000.0,Unalombia, "bajoMonto", 1.3,200000.0,200000.0)

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

                    # Chequeo campo vacío 
                    if any(inputsF0.get(entry)=="" for entry in inputsF0):
                        try:
                            raise ErrorCamposVacios()
                        except:
                            messagebox.showerror(ErrorCamposVacios.mensajeGeneral, ErrorCamposVacios().getMensajeEspecifico())
                            return


                    # Cheque de tipo en el input
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
            

        def F1():
            hide_all_frames()
            clearFrame(frameInscribir) 

            FieldFrame(frame=frameInscribir,
                        tituloFuncion="Inscribir Cuenta",
                        descripcion='''Esta funcionalidad te permite guardar una cuenta que uses frecuentemente. Así no tendrás que
                                ingresar sus datos cada vez que quieras transferir pues quedará asociada a tu usuario.''',
                        tituloCriterios="Criterio",
                        criterios= ["Banco", "Tipo Cuenta", "Numero Cuenta", "Numero Cedula"],
                        tituloValores= "Valor",
                        valores= ["","","",""])

            botonesInscribir=PairButton(frame=frameF2,
                LBotonTitulo="Aceptar")

            def values_frameF1():
                criterios = ["Banco", "Tipo Cuenta", "Numero Cuenta", "Numero Cedula"]
                inputsF1 = {}

                # Obtengo todos los inputs
                for widget,criterio in zip([entry for entry in frameInscribir.winfo_children() if isinstance(entry,tk.Entry) or isinstance(entry,ttk.Combobox)],criterios):
                    inputsF1[criterio] = widget.get()

                # Chequeo campos vacío
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

                # Proceso que ejecuta la funcionalidad
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

            getattr(botonesInscribir,'_LBoton').config(command=values_frameF1)
            getattr(botonesInscribir,'_RBoton').config(command=lambda :PairButton.borrarCampos(frameInscribir))

            frameInscribir.pack(expand=True,anchor='s')
            frameF2.pack(expand=True,anchor='n')
            
            
        # Funcionalidad Inscribir Cuentas
        menuFuncionalidades.add_command(label="F1",command=F1)

        def F2():
            hide_all_frames()
            clearFrame(frameVer)
            FieldFrame(frame=frameVer,
                        tituloFuncion="Ver Historial",
                        descripcion="Esta funcionalidad consiste en mostrar el hisotorial de transferencias de una cuenta.",
                        tituloCriterios="Criterio",
                        criterios= ["Cuentas Disponibles"],
                        tituloValores= "Valor",
                        valores =[""],
                        val= [cuentas.getNroCuenta() for cuentas in usuarioActivo.getCuentasAsociadas()])
            
            def values_frameF2():
                inputsF2 = {}
                criterios = ["Cuentas Disponibles"]

                # Obtengo todos los inputs
                for widget,criterio in zip([entry for entry in frameVer.winfo_children() if isinstance(entry,ttk.Combobox)],criterios):
                    inputsF2[criterio] = widget.get()
                
                # Chequeo campos vacío
                if any(inputsF2.get(entry)=="" for entry in inputsF2):
                    try:
                        raise ErrorCamposVacios()
                    except:
                        messagebox.showerror(ErrorCamposVacios.mensajeGeneral, ErrorCamposVacios().getMensajeEspecifico())
                        return

                for cuentaAsociada in usuarioActivo.getCuentasAsociadas():
                    if cuentaAsociada.getNroCuenta() == int(inputsF2["Cuentas Disponibles"]):
                        cuenta = cuentaAsociada
                        
                if len(cuenta.getHistorialTransferencia())==0:
                    messagebox.showinfo("Ver Historial",
                            f'La cuenta {int(inputsF2["Cuentas Disponibles"])} no tiene historial de transacciones')
                else:
                    hide_all_frames()
                    clearFrame(frameVer)
                    frameHistoriales.pack(expand=True,anchor='s')
                    labelHistoriales = tk.Label(frameHistoriales,text=cuenta.verHistorial(),height=500)
                    labelHistoriales.pack(expand=True,anchor="center")
                    #messagebox.showinfo("Ver Historial", "Formato: cc origen - cuenta origen - cc destino - cuenta destino - valor \n" +
                            #cuenta.verHistorial())             

            botonesVer= PairButton(frame=frameF2,
                                    LBotonTitulo="Aceptar")                        
            getattr(botonesVer,'_LBoton').config(command=values_frameF2)
            getattr(botonesVer,'_RBoton').config(command=lambda :PairButton.borrarCampos(frameVer))

            frameVer.pack(expand=True,anchor='s')
            frameF2.pack(expand=True,anchor='n')

        
            

        menuFuncionalidades.add_command(label="F2",command=F2)

        def F3():
            hide_all_frames()
            clearFrame(frameSolicitar) 
            FieldFrame(frame=frameSolicitar,
                        tituloFuncion="Solicitar Credito",
                        descripcion="Esta funcionalidad crea un credito a un usuario",
                        tituloCriterios="Criterio",
                        criterios= ["Banco","Cuentas Disponibles","Monto","Plazo"],
                        tituloValores= "Valor",
                        valores= ["","","",""],
                        val = [cuentas.getNroCuenta() for cuentas in usuarioActivo.getCuentasAsociadas()])

            def values_frameF3():
                inputsF3 = {}
                criterios = ["Banco","Cuentas Disponibles","Monto","Plazo"]
                # Obtengo todos los inputs
                for widget,criterio in zip([entry for entry in frameSolicitar.winfo_children() if isinstance(entry,tk.Entry) or isinstance(entry,ttk.Combobox)],criterios):
                    inputsF3[criterio] = widget.get()
                
                # Chequeo campos vacío
                if any(inputsF3.get(entry)=="" for entry in inputsF3):
                    try:
                        raise ErrorCamposVacios()
                    except:
                        messagebox.showerror(ErrorCamposVacios.mensajeGeneral, ErrorCamposVacios().getMensajeEspecifico())

                # MODIFICADO Chequeo de tipo en el input (si alguna entrada no es entera o es menor a cero, se llama el error)
                elif any(not canBeInt(inputsF3.get(entry)) or  int(inputsF3.get(entry))<0 for entry in list(inputsF3)[2:]):
                    try:
                        raise ErrorDeTipo("Todos los campos deben ser enteros positivos")
                    except:
                        messagebox.showerror(ErrorDeTipo.mensajeGeneral,
                                ErrorDeTipo("Todos los campos deben ser enteros positivos").getMensajeEspecifico())

                # else:
                # for entry in list(inputsF3)[2:]:
                            # try:
                                # int(inputsF3.get(entry))
                                # if int(inputsF3.get(entry))<0:
                                    # messagebox.showerror("Error",f"El campo {entry} debe ser un entero positivio")
                                # else:
                                    # entradasF3 = True
                            # except:
                                # messagebox.showerror("Error",f"El campo {entry} debe ser entero")

                else:
                    
                    if usuarioActivo.getCreditoActivo()!=None:
                            messagebox.showinfo("Credito","Esta cuenta ya tiene un credito activo")

                    # Pedir explicación de la secuencia de errores. Nunca va a fallar la extracción de cuentas por ser combobox, entonces
                    # el único error sería la solicitud de crédito, no?
                    else:
                            bancoSol = Banco.extraerBanco(_nombreBanco=inputsF3["Banco"])
                            try:
                                cuentaSol= [cuenta for cuenta in usuarioActivo.getCuentasAsociadas() if cuenta.getNroCuenta()==int(inputsF3["Cuentas Disponibles"])][0]
                                credit=usuarioActivo.solicitarCredito(user=usuarioActivo,banco=bancoSol,monto=float(inputsF3.get("Monto")),plazo=int(inputsF3.get("Plazo")),cuentaSc=cuentaSol)
                                print("no estamos :(")
                                if credit ==1:
                                    print("estamos 1")
                                    messagebox.showinfo("Credito","Credito rechazado por mal comportamiento crediticio")
                                elif credit==2:
                                    print("estamos 2")
                                    messagebox.showinfo("Credito rechazado por falta de capacidad de endeudamiento")
                                else:
                                    print("estamos 3")
                                    messagebox.showinfo("Credito",f'Tu solicitud de credito ha sido aprobada y tu saldo actual es: {str(cuentaSol.getSaldo()+float(inputsF3.get("Monto")))}')
                            except:
                                messagebox.showerror("Error Cuenta-Banco",f'Numero de cuenta {inputsF3.get("Cuentas Disponibles")} no existe en el banco: {inputsF3.get("Banco")}')
                    

            botonesSolicitar=PairButton(frame=frameF2,
                LBotonTitulo="Aceptar")

            getattr(botonesSolicitar,'_LBoton').config(command=values_frameF3)
            getattr(botonesSolicitar,'_RBoton').config(command=lambda :PairButton.borrarCampos(frameSolicitar))
            frameSolicitar.pack(expand=True,anchor='s')
            frameF2.pack(expand=True,anchor='n')

        menuFuncionalidades.add_command(label="F3",command=F3)

        def F4():
            hide_all_frames()
            clearFrame(frameRomper) 
            cuentasBajoMonto = [cuenta.getNroCuenta() for cuenta in usuarioActivo.getCuentasAsociadas() if isinstance(cuenta,BajoMonto)]
            if len(cuentasBajoMonto)==0:
                habilitado = [False]
                messagebox.showinfo("Romper Topes","Esta funcionalidad no esta habilitada para tus cuentas.")
            else:
                habilitado = [None]
            
            FieldFrame(frame=frameRomper,
                        tituloFuncion="Romper Topes",
                        descripcion="Esta funcionalidad consiste en cambiar de una cuenta de bajo monto a una de ahorros.",
                        tituloCriterios="Criterio",
                        criterios= ["Cuentas Disponibles"],
                        tituloValores= "Valor",
                        valores= [""],
                        val=cuentasBajoMonto,
                        habilitados=habilitado)

            def values_frameF4():
                inputsF4 = {}
                criterios = ["Cuentas Disponibles"]

                # Obtengo todos los inputs
                for widget,criterio in zip([entry for entry in frameRomper.winfo_children() if isinstance(entry,tk.Entry) or isinstance(entry,ttk.Combobox)],criterios):
                    inputsF4[criterio] = widget.get()

                # Si hay algun input vacio se saca una ventana emergente, sino se procede a verificar los tipos de entrada
                if any(inputsF4.get(entry)=="" for entry in inputsF4):
                    try:
                        raise ErrorCamposVacios()
                    except:
                        messagebox.showerror(ErrorCamposVacios.mensajeGeneral, ErrorCamposVacios().getMensajeEspecifico())
                else:
                    # Se pregunta si se desea continuar con el proceso
                    continuar = messagebox.askokcancel("Confirmacion Romper Topes",
                    '''¡Recuerde! El procedimiento de romper topes consiste en transformar su cuenta de tipo Bajo monto,
                    a una cuenta de ahorros convencional, eliminando las limitaciones de este tipo de cuentas.\n 
                    Este proceso tiene un costo de 15.000 pesos que pagará una unica vez.''')
                    if continuar:
                        cuentaRomper = [cuenta for cuenta in usuarioActivo.getCuentasAsociadas() if cuenta.getNroCuenta()==int(inputsF4["Cuentas Disponibles"])][0]
                        #FALTA TESTEAR
                        if not cuentaRomper.romperTopes():
                            try:
                                raise ErrorNoSaldo(cuentaRomper.getSaldo(), "15.000", "romper topes")
                            except:
                                messagebox.showerror(ErrorNoSaldo.mensajeGeneral,
                                        ErrorNoSaldo(cuentaRomper.getSaldo(), "15.000", "romper topes"))
                        else:
                            bancoRomper = cuentaRomper.getBanco()
                            # Se remueve la cuenta del banco
                            bancoRomper.removerCuenta(cuentaRomper)
                            # Se elimina la cuenta de bajo monto de las asociadas que tenia el usuario
                            usuarioActivo.removerCuentaAsociada(cuentaRomper)
                            # Cuenta nueva
                            numeroCuentaNueva = cuentaRomper.getNroCuenta()
                            cuentaNueva = bancoRomper.extraerCuenta(numeroCuentaNueva)
                            #PROPUESTA
                            messagebox.showinfo("Romper Topes",'''Tu solicitud ha sido aprobada y tu nueva cuenta de ahorros quedó con
                                    un saldo de {str(cuentaNueva.getSaldo())} pesos.''')
                            # messagebox.showinfo("Romper Topes","Tu solicitud ha sido aprobada, se descontaran $15.000 de tu saldo para realizar el proceso. Espera un momento...")
                            # messagebox.showinfo("Romper Topes","Tu cuenta ha sido actualizada y ahora no tiene topes.")
                            # messagebox.showinfo("Romper Topes",f'Tu nueva cuenta de ahorros ahora tiene un saldo de: {str(cuentaNueva.getSaldo())}.')


            botonesRomper = PairButton(frame=frameF2,
                LBotonTitulo="Aceptar")

            getattr(botonesRomper,'_LBoton').config(command=values_frameF4)
            getattr(botonesRomper,'_RBoton').config(command=lambda :PairButton.borrarCampos(frameRomper))
            frameRomper.pack(expand=True,anchor='s')
            frameF2.pack(expand=True,anchor='n')

        menuFuncionalidades.add_command(label="F4",command=F4)

        def F5():
            hide_all_frames()
            clearFrame(frameTransferir) 
            #["Cuenta Destino","Banco Destino","Numero Cuenta","Valor"]
            criteriosInicial =["Cuentas Disponibles","Tipo Transferencia"]
            FieldFrame(frame=frameTransferir,
                        tituloFuncion="Transferir",
                        descripcion="Esta funcionalidad consiste permite bien sea pagar un credito o tranferir a otra cuenta.",
                        tituloCriterios="Criterio",
                        criterios= ["Cuentas Disponibles","Tipo Transferencia"],
                        tituloValores= "Valor",
                        valores= ["","","","","",""],
                        val=[cuentas.getNroCuenta() for cuentas in usuarioActivo.getCuentasAsociadas()])

            botonesTransferir = PairButton(frame=frameF2,
            LBotonTitulo="Aceptar")
            
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

                else:

                    cuentaOrigen = [cuenta for cuenta in usuarioActivo.getCuentasAsociadas() if cuenta.getNroCuenta()==int(inputsInicial["Cuentas Disponibles"])][0]

                    if inputsInicial.get("Tipo Transferencia")=="Pagar credito":
                        if usuarioActivo.getCreditoActivo() is None:
                            messagebox.showerror("Error","No tienes ningun credito activo para pagar.")
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
                    elif inputsInicial.get("Tipo Transferencia")=="A otra cuenta - Inscrita":
                        if len(usuarioActivo.getListaIncritos())==0:
                            messagebox.showerror("Error","No tiene cuentas inscritas")
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
                        
                        def values_FrameIns():
                            inputsIns = {}
                            for widget,criterio in zip([entry for entry in frameTransferir.winfo_children()
                                if isinstance(entry,tk.Entry) or isinstance(entry,ttk.Combobox)],["Cuentas Disponibles","Valor"]):
                                    inputsIns[criterio] = widget.get()

                            # Si hay algun input vacio, se saca una ventana emergente, sino se procede a verificar los tipos de entrada
                            if any(inputsIns.get(entry)=="" for entry in inputsIns):
                                try:
                                    raise ErrorCamposVacios()
                                except:
                                    messagebox.showerror(ErrorCamposVacios.mensajeGeneral, ErrorCamposVacios().getMensajeEspecifico())
                            elif float(inputsIns.get("Valor"))<0:
                                messagebox.showerror("Error","El valor debe ser positivo")
                            else:
                                cuentaDestino = [cuenta for cuenta in usuarioActivo.getListaIncritos() if cuenta.getNroCuenta()==int(inputsIns["Cuentas Disponibles"])][0]
                                bancoDestino = cuentaDestino.getBanco()

                                if not cuentaDestino in bancoDestino.getListaCuentas():
                                    messagebox.showerror("Error","La cuenta inscrita que ha seleccionado ya no esta disponible, por lo tanto sera eliminada de su lista de cuentas inscritas.")
                                    usuarioActivo.removerCuentaInscrita(cuentaDestino)

                                    
                                else:
                                    opcion=messagebox.askokcancel("Confirma Transferencia","¿Desea confirmar la transferencia?")
                                    if opcion:
                                        exito = cuentaOrigen.transferir(cuentaDestino,float(inputsIns.get("Valor")))
                                        if exito:
                                            messagebox.showinfo("Transferencia Exitosa",f'Transferencia exitosa.')
                                            messagebox.showinfo("Transferencia Exitosa",f'Tu cuenta queda con un saldo de {cuentaOrigen.getSaldo()}.')
                                        else:
                                            messagebox.showerror("Transferencia Rechazada","Tu pago ha sido rechazado ya que no cuentas con saldo suficiente o tu producto de origen no permite mover el valor indicado.")
                                    
                        getattr(botonesTransferir,'_LBoton').config(command=values_FrameIns)
                        getattr(botonesTransferir,'_RBoton').config(command=lambda :PairButton.borrarCampos(frameTransferir))
                    else:
                        clearFrame(frameTransferir) 
                        FieldFrame(frame=frameTransferir,
                            tituloFuncion="Transferir - Cuenta No Inscrita",
                            descripcion="Esta funcionalidad consiste permite bien sea pagar un credito o tranferir a otra cuenta.",
                            tituloCriterios="Criterio",
                            criterios= ["Banco Destino","Numero Cuenta","Valor"],
                            tituloValores= "Valor",
                            valores= ["","",""])
                        botonesTransferir = PairButton(frame=frameF2,
                                LBotonTitulo="Aceptar")
                        def values_FrameNoIns():
                            inputsNoIns = {}
                            for widget,criterio in zip([entry for entry in frameTransferir.winfo_children() if isinstance(entry,tk.Entry) or isinstance(entry,ttk.Combobox)],["Banco","Numero Cuenta","Valor"]):
                                    inputsNoIns[criterio] = widget.get()

                            # Si hay algun input vacio, se saca una ventana emergente, sino se procede a verificar los tipos de entrada
                            if any(inputsNoIns.get(entry)=="" for entry in inputsNoIns):
                                try:
                                    raise ErrorCamposVacios()
                                except:
                                    messagebox.showerror(ErrorCamposVacios.mensajeGeneral, ErrorCamposVacios().getMensajeEspecifico())
                            elif float(inputsNoIns.get("Valor"))<0:
                                messagebox.showerror("Error","El valor debe ser positivo")
                            else:
                                try:
                                    int(inputsNoIns.get("Numero Cuenta"))
                                    if int(inputsNoIns.get("Numero Cuenta"))<0:
                                        messagebox.showerror("Error","El Numero Cuenta debe ser entero positivo")
                                    else:
                                        try:
                                            bancoDestino = Banco.extraerBanco(inputsNoIns.get("Banco"))
                                            cuentaDestino = bancoDestino.extraerCuenta(int(inputsNoIns.get("Numero Cuenta")))

                                            if not cuentaDestino in bancoDestino.getListaCuentas():
                                                messagebox.showerror("Error","La cuenta inscrita que ha seleccionado ya no esta disponible, por lo tanto sera eliminada de su lista de cuentas inscritas.")
                                                usuarioActivo.removerCuentaInscrita(cuentaDestino)   
                                            else:
                                                opcion=messagebox.askokcancel("Confirma Transferencia","¿Desea confirmar la transferencia?")
                                                if opcion:
                                                    if float(inputsNoIns.get("Valor"))>3000000:
                                                        messagebox.showerror("Error","El valor que ingreso supera el valor pertitido para cuentas no inscritas")
                                                        messagebox.showinfo("Recordatorio","Recuerde que valor maximo a transferir a una cuenta no inscirta es de 3'000.000")
                                                    else:
                                                        exito = cuentaOrigen.transferir(cuentaDestino,float(inputsNoIns.get("Valor")))
                                                        if exito:
                                                            messagebox.showinfo("Transferencia Exitosa",f'Transferencia exitosa.')
                                                            messagebox.showinfo("Transferencia Exitosa",f'El saldo de su cuenta es de {cuentaOrigen.getSaldo()}.')
                                                        else:
                                                            messagebox.showerror("Error","Hubo un error en la operacion. Verifique que su cuenta de origen tenga y permita mover el saldo indicado.")
                                        except:
                                            messagebox.showerror("Error",f'Numero de cuenta {inputsNoIns.get("Numero Cuenta")} no existe en el banco: {inputsNoIns["Banco"]}')
                                except:
                                    messagebox.showerror("Error","El Numero Cuenta debe ser entero")     

                        getattr(botonesTransferir,'_LBoton').config(command=values_FrameNoIns)
                        getattr(botonesTransferir,'_RBoton').config(command=lambda :PairButton.borrarCampos(frameTransferir))


            getattr(botonesTransferir,'_LBoton').config(command=values_frameF5)
            getattr(botonesTransferir,'_RBoton').config(command=lambda :PairButton.borrarCampos(frameTransferir))

            frameTransferir.pack(expand=True,anchor='s')
            frameF2.pack(expand=True,anchor='n')
        menuFuncionalidades.add_command(label="F5",command=F5)

        # Estructura menu AYUDA

        def acercaDe():
            messagebox.showinfo("Acerca de:","Daniel \n Diego \n David \n Cesar")

        ayuda.add_command(label="Autores:",command=acercaDe)








        ventana.mainloop()
