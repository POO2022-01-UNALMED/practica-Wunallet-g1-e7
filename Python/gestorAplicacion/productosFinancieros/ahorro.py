'''Clase Ahorro
 Es el producto financiero más simple, diferenciándose de su clase padre Cuenta al ofrecer una tasa de interés que producirá
 ingresos en el tiempo. '''
from multipledispatch import dispatch
from gestorAplicacion.infoClientes.transaccion import Transaccion
from gestorAplicacion.productosFinancieros.credito import Credito
from gestorAplicacion.productosFinancieros.cuenta import Cuenta
from gestorAplicacion.infoClientes.banco import Banco
from gestorAplicacion.infoClientes.usuario import Usuario



class Ahorro(Cuenta):
    '''El Array de clase de clientes de encarga de guardar todas las instancias de
    Cliente para poder guardar y cargarlas en la serializacion'''
    ahorro = []

    #Constructor
    def __init__(self, nroCuenta, titular, saldo, banco, tipoDeCuenta,tasaDeInteres,historial_ant=[]):
        super().__init__(nroCuenta,titular,saldo,banco,tipoDeCuenta)
        self.historialTransferencia=historial_ant
        self.tasaDeInteres=tasaDeInteres
        banco.getListaCuentas().append(self)
        titular.getCuentasAsociadas().append(self)



        Ahorro.ahorro.append(self)

    '''Verifica si el usuario cuenta con saldo para realizar la transacción. De ser así realiza los ajustes de saldo en cada cuenta,
    crea el objeto transaccion y lo añade al historial de las cuentas involucradas.'''

    @dispatch(Cuenta,float)
    def transferir(self,cuentaDestino,valorTransferencia):
        if self.saldo>= valorTransferencia:
            self.restarSaldo(valorTransferencia)
            cuentaDestino.sumarSaldo(valorTransferencia)
            trans = Transaccion(self,cuentaDestino,valorTransferencia)
            self.historialTransferencia.append(trans)
            cuentaDestino.historialTransferencia.append(trans)
            return True
        else:
            return False


    '''Verifica si el usuario cuenta con saldo para realizar el pago de la cuota mensual. De ser así realiza los ajustes de saldo
    en la cuenta origen y la deuda, crea el objeto transaccion y lo añade al historial de la cuenta de origen.'''
    @dispatch(Credito)
    def transferir(self,credito):
        if self.saldo >= credito.getCuotaMensual():
            self.restarSaldo(credito.getCuotaMensual())
            credito.setDeuda(credito.getDeuda()-credito.getCuotaMensual())
            trans = Transaccion(self,credito.getBanco().getNombreBanco(),credito.getCuotaMensual())
            self.historialTransferencia.append(trans)
            return True
        else:
            return False

    #-------------------------------------- Metodos get-set --------------------------------------
    @classmethod
    def getAhorro(cls): return Ahorro.ahorro

    @classmethod
    def setAhorro(cls, ahorro):  Ahorro.ahorro = ahorro
	
    def  setTasaDeInteres(self, tasaDeInteres) : self.tasaDeInteres = tasaDeInteres

    def  getTasaDeInteres(self) : return self.tasaDeInteres
	
    def  getHistorialTransferencia(self): return self.historialTransferencia
	
    def  setHistorialTransferencia(self,historial): self.historialTransferencia = historial


