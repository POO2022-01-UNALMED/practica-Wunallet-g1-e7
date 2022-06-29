'''Este módulo fue hecho con la finalidad de crear la función para deserializar los objetos guardados, para
así luego  usados en el main de nuestra aplicación.'''

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

class Deserializador():
    
    def deserializar(lista, className):
        def camino(className):
            string = os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\"+className+".txt")
            return string
        # Leo el archivo
        try:
            picklefile = open(camino(className), 'rb')
        except:
            picklefile = open(camino(className), 'x')
            picklefile = open(camino(className), 'rb')
        # unpickle los datos
        if os.path.getsize(camino(className)) > 0:
            lista = pickle.load(picklefile)
        
        # Cierro el archivo
        picklefile.close()
        return lista
        # Cierro el archivo
    
    def deserializarTodo():
        Banco.banco = Deserializador.deserializar(Banco.banco, "Banco")
        PerfilCrediticio._perfilCrediticio = Deserializador.deserializar(PerfilCrediticio._perfilCrediticio, "PerfilCrediticio")
        Transaccion._transaccion =  Deserializador.deserializar(Transaccion._transaccion, "Transaccion")
        Usuario._usuario = Deserializador.deserializar(Usuario._usuario, "Usuario")
        Ahorro.ahorro = Deserializador.deserializar(Ahorro.ahorro, "Ahorro")
        BajoMonto._bajoMonto = Deserializador.deserializar(BajoMonto._bajoMonto, "BajoMonto")
        Corriente._corriente = Deserializador.deserializar(Corriente._corriente, "Corriente")
        Credito._componentes = Deserializador.deserializar(Credito._credito, "Credito")
