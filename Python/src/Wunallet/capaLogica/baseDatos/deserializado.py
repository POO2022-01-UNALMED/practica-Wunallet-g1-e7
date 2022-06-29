import pickle
import os

from Wunallet.capaLogica.gestorAplicacion.infoClientes.banco import Banco
from Wunallet.capaLogica.gestorAplicacion.infoClientes.perfilCrediticio import PerfilCrediticio
from Wunallet.capaLogica.gestorAplicacion.infoClientes.transaccion import Transaccion
from Wunallet.capaLogica.gestorAplicacion.infoClientes.usuario import Usuario

from Wunallet.capaLogica.gestorAplicacion.productosFinancieros.ahorro import Ahorro
from Wunallet.capaLogica.gestorAplicacion.productosFinancieros.bajoMonto import BajoMonto
from Wunallet.capaLogica.gestorAplicacion.productosFinancieros.corriente import Corriente
from Wunallet.capaLogica.gestorAplicacion.productosFinancieros.credito import Credito


def deserializar():
    """ Método encargado de carcar  los datos del
        sistema al abrir la app"""

    datos = {
             "Banco": lambda x : Banco.setBanco(x),
             "Transaccion" : lambda x : Transaccion.setTransaccion(x),
             "Usuario" : lambda x : Usuario.setUsuario(x),
             "Ahorro" : lambda x : Ahorro.setAhorro(x),
             "BajoMonto" : lambda x : BajoMonto.setBajoMonto(x),
             "Corriente" : lambda x : Corriente.setCorriente(x),
             "Credito" : lambda x : Credito.setCredito(x)
            }

    
    # direccion_parcial = os.path.join("src", "Wunallet","capaLogica","baseDatos", "temp")
    direccion_parcial = os.path.join("src", "Wunallet","capaLogica","baseDatos", "temp")

    for archivo, set in datos.items():
        picklefile = open(os.path.join(direccion_parcial, archivo), 'rb')
        dato = pickle.load(picklefile)
        set(dato)
        picklefile.close()


