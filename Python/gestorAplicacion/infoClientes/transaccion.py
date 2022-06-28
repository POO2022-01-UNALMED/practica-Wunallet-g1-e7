'''/* Clase Transcacion
 Es una clase que sólamente tiene atributos de tal forma que, en conjunto, permiten reconstruir a detalle la información sobre
 una operación bancaria.'''

from multipledispatch import dispatch

from gestorAplicacion.productosFinancieros.cuenta import Cuenta
#from gestorAplicacion.productosFinancieros.corriente import Corriente



class Transaccion:
    '''El Array de clase de clientes de encarga de guardar todas las instancias de
     Cliente para poder guardar y cargarlas en la serializacion'''
    _transaccion=[]

    @dispatch(Cuenta,Cuenta,float)
    def __init__(self, cuentaOrigen, cuentaDestino, valorTransaccion):
        self._cuentaOrigen=cuentaOrigen
        self._cuentaDestino=cuentaDestino
        self._valorTransaccon=valorTransaccion
        Transaccion._transaccion.append(self)

    @dispatch(Cuenta,str,float)
    def __init__(self,cuentaOrigen,nombreBanco,valorTransaccion):
        self._cuentaOrigen=cuentaOrigen
        self._nombreBanco=nombreBanco
        self._valorTransaccon=valorTransaccion
        Transaccion._transaccion.append(self)


    #Formateo del texto al imprimirse un objeto de tipo transacción

    def __str__(self):
        if hasattr(self, '_cuentaDestino') is False:
            return "Transferencia de" + self.cuentaOrigen.getTitular().getCc() + " desde la cuenta " + self.cuentaOrigen.getNroCuenta() + " a " + self.getNombreBanco() + " por valor de " + self.getValorTransaccion() + ".";
        else:
            return "Transferencia de " + self.cuentaOrigen.getTitular().getCc() + " desde la cuenta " + self.getCuentaOrigen().getNroCuenta() + " al usuario con CC: " + self.cuentaDestino.getTitular().getCc() + " con cuenta " + self.cuentaDestino.getNroCuenta() + " por valor de " + self.getValorTransaccion() + ".";

    '''-------------------------------------- Metodos get-set --------------------------------------'''
    @classmethod
    def getTransaccion(cls): return Transaccion._transaccion
    @classmethod
    def setTransaccion(cls, transaccion): Transaccion._transaccion = transaccion
	
    def setCuentaOrigen(self, cuentaOrigen) : self._cuentaOrigen = cuentaOrigen

    def getCuentaOrigen(self) : return self._cuentaOrigen
	
    def  getCuentaDestino(self, cuentaDestino) : self._cuentaDestino = cuentaDestino

    def getCuentaDestino(self) : return self._cuentaDestino
	
    def setNombreBanco(self, nombreBanco) : self._nombreBanco = nombreBanco

    def getNombreBanco(self) : return self._nombreBanco
	
    def setValorTransaccion(self, valorTransaccion) : self._valorTransaccion = valorTransaccion

    def getValorTransaccion(self) : return self._valorTransaccion