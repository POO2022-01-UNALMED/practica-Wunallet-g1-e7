'''Este módulo fue hecho con la finalidad de crear la función para deserializar los objetos guardados, para
así luego  usados en el main de nuestra aplicación.'''

import os
import pathlib
import pickle

from gestorAplicacion.infoClientes.banco import Banco
from gestorAplicacion.infoClientes.perfilCrediticio import PerfilCrediticio
from gestorAplicacion.infoClientes.transaccion import Transaccion
from gestorAplicacion.infoClientes.usuario import Usuario

from gestorAplicacion.productosFinancieros.ahorro import Ahorro
from gestorAplicacion.productosFinancieros.bajoMonto import BajoMonto
from gestorAplicacion.productosFinancieros.corriente import Corriente
from gestorAplicacion.productosFinancieros.credito import Credito

#Se llaman a todas las funciones de deserialización
def deserializar():
    deserializarBanco()
    deserializarPerfilCrediticio()
    deserializarTransaccion()
    deserializarUsuario()

    deserializarAhorro()
    deserializarBajoMonto()
    deserializarCorriente()
    deserializarCredito()

def deserializarBanco():
    #Apertura del archivo donde será leido el flujo de bytes que representen el objeto. En este caso se trata de banco
    fichero_banco=open(os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\banco.pkl"), "rb")
    #Indicamos la variable donde se guardará el objeto deserializado. En este caso la lista de banco
    Banco.setBanco(pickle.load(fichero_banco))
    #Se cierra el archivo abierto
    fichero_banco.close()

def deserializarPerfilCrediticio():
    #Apertura del archivo donde será leido el flujo de bytes que representen el objeto. En este caso se trata de PerfilCrediticio
    fichero_perfil=open(os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\perfilCrediticio.pkl"), "rb")
    #Indicamos la variable donde se guardará el objeto deserializado. En este caso la lista de PerfilCrediticio
    PerfilCrediticio.setPerfilCrediticio(pickle.load(fichero_perfil))
    #Se cierra el archivo abierto
    fichero_perfil.close()

def deserializarTransaccion():
    #Apertura del archivo donde será leido el flujo de bytes que representen el objeto. En este caso se trata de Transaccion
    fichero_trans=open(os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\transaccion.pkl"), "rb")
    #Indicamos la variable donde se guardará el objeto deserializado. En este caso la lista de Transaccion
    Transaccion.setTransaccion(pickle.load(fichero_trans))
    #Se cierra el archivo abierto
    fichero_trans.close()

def deserializarUsuario():
    #Apertura del archivo donde será leido el flujo de bytes que representen el objeto. En este caso se trata de Usuario
    fichero_usuario=open(os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\usuario.pkl"), "rb")
    #Indicamos la variable donde se guardará el objeto deserializado. En este caso la lista de Usuario
    Usuario.setUsuario(pickle.load(fichero_usuario))
    #Se cierra el archivo abierto
    fichero_usuario.close()



def deserializarAhorro():
    #Apertura del archivo donde será leido el flujo de bytes que representen el objeto. En este caso se trata de Ahorro
    fichero_ahorro=open(os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\ahorro.pkl"), "rb")
    #Indicamos la variable donde se guardará el objeto deserializado. En este caso la lista de Ahorro
    Ahorro.setAhorro(pickle.load(fichero_ahorro))
    #Se cierra el archivo abierto
    fichero_ahorro.close()

def deserializarBajoMonto():
    #Apertura del archivo donde será leido el flujo de bytes que representen el objeto. En este caso se trata de BajoMonto
    fichero_bajo=open(os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\bajoMonto.pkl"), "rb")
    #Indicamos la variable donde se guardará el objeto deserializado. En este caso la lista de BajoMonto
    BajoMonto.setBajoMonto(pickle.load(fichero_bajo))
    #Se cierra el archivo abierto
    fichero_bajo.close()

def deserializarCorriente():
    #Apertura del archivo donde será leido el flujo de bytes que representen el objeto. En este caso se trata de Corriente
    fichero_corriente=open(os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\corriente.pkl.pkl"), "rb")
    #Indicamos la variable donde se guardará el objeto deserializado. En este caso la lista de Corriente
    Corriente.setCorriente(pickle.load(fichero_corriente))
    #Se cierra el archivo abierto
    fichero_corriente.close()

def deserializarCredito():
    #Apertura del archivo donde será leido el flujo de bytes que representen el objeto. En este caso se trata de Credito
    fichero_credito=open(os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\credito.pkl.pkl"), "rb")
    #Indicamos la variable donde se guardará el objeto deserializado. En este caso la lista de Credito
    Credito.setCredito(pickle.load(fichero_credito))
    #Se cierra el archivo abierto
    fichero_credito.close()

