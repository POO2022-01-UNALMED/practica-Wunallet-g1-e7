'''Este módulo fue hecho con la finalidad de crear la función para serilizar los objetos creados, para
así luego poder ser deserializados y usados en el main de nuestra aplicación. Cada tipo de objeto
es serializado por aparte, en su función correspondiente, y luego invocado en la función serializar"""'''

import os
import pathlib
import pickle

from Wunallet.capaLogica.gestorAplicacion.infoClientes.banco import Banco
from Wunallet.capaLogica.gestorAplicacion.infoClientes.perfilCrediticio import PerfilCrediticio
from Wunallet.capaLogica.gestorAplicacion.infoClientes.transaccion import Transaccion
from Wunallet.capaLogica.gestorAplicacion.infoClientes.usuario import Usuario

from Wunallet.capaLogica.gestorAplicacion.productosFinancieros.ahorro import Ahorro
from Wunallet.capaLogica.gestorAplicacion.productosFinancieros.bajoMonto import BajoMonto
from Wunallet.capaLogica.gestorAplicacion.productosFinancieros.corriente import Corriente
from Wunallet.capaLogica.gestorAplicacion.productosFinancieros.credito import Credito

# Se llaman a todas las funciones de serilización
def serializar():
    serializarBanco()
    serializarPerfilCrediticio()
    serializarTransaccion()
    serializarUsuario()

    serializarAhorro()
    serializarBajoMonto()
    serializarCorriente()
    serializarCredito()


def serializarBanco():
    # Creación y apertura del archivo donde será guardado el flujo de bytes que representen el objeto. En este caso se trata de banco
    fichero_banco = open(os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\banco.pkl"), "wb")
    # Indicamos el dato que será serializado. En este caso el valor de la caja de banco
    pickle.dump(Banco.getBanco(), fichero_banco)
    # Se cierra el archivo creado
    fichero_banco.close()


def serializarPerfilCrediticio():
    # Creación y apertura del archivo donde será guardado el flujo de bytes que representen el objeto. En este caso se trata de PerfilCrediticio
    fichero_perfil = open(os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\perfilCrediticio.pkl"), "wb")
    # Indicamos el dato que será serializado. En este caso la lista de PerfilCrediticio
    pickle.dump(PerfilCrediticio.getPerfilCrediticio(), fichero_perfil)
    # Se cierra el archivo creado
    fichero_perfil.close()


def serializarTransaccion():
    # Creación y apertura del archivo donde será guardado el flujo de bytes que representen el objeto. En este caso se trata de Transaccion
    fichero_trans = open(os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\transaccion.pkl"), "wb")
    # Indicamos el dato que será serializado. En este caso la lista de Transaccion
    pickle.dump(Transaccion.getTransaccion(), fichero_trans)
    # Se cierra el archivo creado
    fichero_trans.close()


def serializarUsuario():
    # Creación y apertura del archivo donde será guardado el flujo de bytes que representen el objeto. En este caso se trata de Usuario
    fichero_usuario = open(os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\usuario.pkl"), "wb")
    # Indicamos el dato que será serializado. En este caso la lista de Usuario
    pickle.dump(Usuario.getUsuario(), fichero_usuario)
    # Se cierra el archivo creado
    fichero_usuario.close()





def serializarAhorro():
    # Creación y apertura del archivo donde será guardado el flujo de bytes que representen el objeto. En este caso se trata de Ahorro
    fichero_ahorro = open(os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\ahorro.pkl"), "wb")
    # Indicamos el dato que será serializado. En este caso la lista de Ahorro
    pickle.dump(Ahorro.getAhorro(), fichero_ahorro)
    # Se cierra el archivo creado
    fichero_ahorro.close()


def serializarBajoMonto():
    # Creación y apertura del archivo donde será guardado el flujo de bytes que representen el objeto. En este caso se trata de BajoMonto
    fichero_bajoMonto = open(os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\bajoMonto.pkl"), "wb")
    # Indicamos el dato que será serializado. En este caso la lista de BajoMonto
    pickle.dump(BajoMonto.getBajoMonto(), fichero_bajoMonto)
    # Se cierra el archivo creado
    fichero_bajoMonto.close()


def serializarCorriente():
    # Creación y apertura del archivo donde será guardado el flujo de bytes que representen el objeto. En este caso se trata de Corriente
    fichero_corriente = open(os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\corriente.pkl"), "wb")
    # Indicamos el dato que será serializado. En este caso la lista de Corriente
    pickle.dump(Corriente.getCorriente(), fichero_corriente)
    # Se cierra el archivo creado
    fichero_corriente.close()

def serializarCredito():
    # Creación y apertura del archivo donde será guardado el flujo de bytes que representen el objeto. En este caso se trata de Credito
    fichero_credito = open(os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\credito.pkl"), "wb")
    # Indicamos el dato que será serializado. En este caso la lista de Credito
    pickle.dump(Credito.getCredito(), fichero_credito)
    # Se cierra el archivo creado
    fichero_credito.close()