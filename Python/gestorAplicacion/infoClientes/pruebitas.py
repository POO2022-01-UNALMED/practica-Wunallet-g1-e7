from multipledispatch import dispatch

from gestorAplicacion.productosFinancieros.cuenta import Cuenta


class Transaccion:
    '''El Array de clase de clientes de encarga de guardar todas las instancias de
     Cliente para poder guardar y cargarlas en la serializacion'''
    transaccion = []

    @dispatch(int, str, float)
    def __init__(self, cuentaOrigen, cuentaDestino, valorTransaccion):
        self._cuentaOrigen = cuentaOrigen
        self._cuentaDestino = cuentaDestino
        self._valorTransaccon = valorTransaccion

    @dispatch(float,str,float)
    def __init__(self, cuentaOrigen, nombreBanco, valorTransaccion):
        self._cuentaOrigen = cuentaOrigen
        self._nombreBanco = nombreBanco
        self._valorTransaccon = valorTransaccion

    def xd(self):
        if hasattr(self, '_cuentaDestino') is False:
            print('happy')

trans=Transaccion(1.0,'1202',12222.0)

trans.xd()
