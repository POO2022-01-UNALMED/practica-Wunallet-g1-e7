'''Clase Corriente
 Siendo una clase hija de Cuenta, se diferencia por incluir la capacidad de sobregirarse, de tal forma que el usuario puede
 realizar transferencias de mayor cantidad que las de su saldo.'''
from multipledispatch import dispatch

from gestorAplicacion.infoClientes.transaccion import Transaccion
from gestorAplicacion.productosFinancieros.credito import Credito
from gestorAplicacion.productosFinancieros.cuenta import Cuenta
from gestorAplicacion.infoClientes.banco import Banco
from gestorAplicacion.infoClientes.usuario import Usuario


class Corriente(Cuenta):

    _capacidadSobregiro=600000

    '''El Array de clase de clientes de encarga de guardar todas las instancias de
    Cliente para poder guardar y cargarlas en la serializacion'''
    _corriente = []

    #Constructor
    def __init__(self, nroCuenta, titular, saldo, banco, tipoDeCuenta,sobregiroActual):
        super().__init__(nroCuenta,titular,saldo,banco,tipoDeCuenta)
        self._sobregiroActual = sobregiroActual
        banco.getListaCuentas().append(self)
        titular.getCuentasAsociadas().append(self)

        Corriente._corriente.append(self)

    '''Verifica si el usuario cuenta con saldo y capacidad de sobregiro para realizar la transacción. De ser así setea el
    sobregiroActual en caso de haberse usado, realiza los ajustes de saldo en cada cuenta, crea el objeto transaccion y lo
    añade al historial de las cuentas involucradas.'''

    @dispatch(Cuenta,float)
    def transferir(self, cuentaDestino,valorTransferencia):

        if self.saldo + (self._capacidadSobregiro-self._sobregiroActual)>=valorTransferencia:
            if valorTransferencia>self.saldo:
                self.setSaldo(0)
                self.setSobregiroActual(self._sobregiroActual+(valorTransferencia-self.saldo))
            else:
                self.restarSaldo(valorTransferencia)

            cuentaDestino.sumarSaldo(valorTransferencia)
            trans = Transaccion(self,cuentaDestino,valorTransferencia)
            self.historialTransferencia.append(trans)
            cuentaDestino.historialTransferencia.append(trans)
            return True
        else:
            return False

    '''Verifica si el usuario cuenta con saldo y capacidad de sobregiro para realizar el pago de la cuota mensual. De ser así setea
    el sobregiroActual en caso de haberse usado; realiza los ajustes de saldo en la cuenta origen y la deuda del crédito; 
    crea el objeto transaccion y lo añade al historial de la cuenta origen'''

    @dispatch(Credito)
    def transferir(self,credito):
        if self.saldo + (self._capacidadSobregiro-self._sobregiroActual)>= credito.getCuotaMensual():
            if credito.getCuotaMensual()>self.saldo:
                self.setSaldo(0)
                self.setSobregiroActual(self._sobregiroActual+(credito.getCuotaMensual()-self.saldo))
            else:
                self.restarSaldo(credito.getCuotaMensual())

            credito.setDeuda(credito.getDeuda()-credito.getCuotaMensual())
            trans=Transaccion(self,credito.getBanco().getNombreBanco(),credito.getCuotaMensual())
            self.historialTransferencia.append(trans)
            return True
        else:
            return False



    #-------------------------------------- Metodos get-set --------------------------------------
    @classmethod
    def  getCorriente(cls) : return Corriente._corriente
    @classmethod
    def  setCorriente(cls, corriente) : Corriente._corriente = corriente
	
    def  setSobregiroActual(self, sobregiroActual) : self._sobregiroActual = sobregiroActual

    def  getSobregiroActual(self) : return self._sobregiroActual

    def getHistorialTransferencia(self): return self.historialTransferencia
	
    def  setHistorialTransferencia(self, historial): self.historialTransferencia = historial

