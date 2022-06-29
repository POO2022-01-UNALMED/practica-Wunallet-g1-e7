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

class Serializador():
    
    def serializar(lista, className):
        def camino(className):
            string = os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\"+className+".txt")
            # string = os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\"+className)
            print("La ruta es",string)
            return string
        try:
            # Creo el archivo pickle para guardar los objetos
            picklefile = open(camino(className), 'wb')
            # pickle el objeto en el archivo
            pickle.dump(lista, picklefile)
            # cierro el archivo para guardar
            picklefile.close()
            
        except:
            print("paila tuqui tuqui muñeco")

    def serializarTodo():
        print("Estoy aca en serializador, debería funcionar")
        Serializador.serializar(Banco.banco, "Banco")
        Serializador.serializar(PerfilCrediticio._perfilCrediticio, "PerfilCreditico")
        Serializador.serializar(Transaccion.getTransaccion(), "Transaccion")
        Serializador.serializar(Usuario.getUsuario(), "Usuario")
        Serializador.serializar(Ahorro.getAhorro(), "Ahorro")
        Serializador.serializar(BajoMonto.getBajoMonto(), "BajoMonto")
        Serializador.serializar(Corriente.getCorriente(), "Corriente")
        Serializador.serializar(Credito.getCredito(), "Credito")
        # Serializador.serializar(Empleado.getEmpleados(), "Empleados")

        # print("Banco:", Banco.banco)
        # print("PerfilCrediticio:", PerfilCrediticio._perfilCrediticio)
        # print("Transaccion:", Transaccion.getTransaccion())
        # print("Usuario:", Usuario.getUsuario())
        # print("Ahorro:", Ahorro.getAhorro())
        # print("BajoMonto:", BajoMonto.getBajoMonto())
        # print("Corriente:", Corriente.getCorriente())
        # print("Credito:", Credito.getCredito())
