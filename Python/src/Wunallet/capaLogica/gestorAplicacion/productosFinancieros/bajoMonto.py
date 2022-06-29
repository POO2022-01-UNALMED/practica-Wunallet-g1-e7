# Clase BajoMonto
 
# Es el resultado de especializar las cuentas Ahorro, ya que si bien disponen de los mismos atributos, sus métodos están limitados
# a un tope máximo mensual que pueden transferir.

from multipledispatch import dispatch

from Wunallet.capaLogica.gestorAplicacion.infoClientes.gestor import Gestor
from Wunallet.capaLogica.gestorAplicacion.infoClientes.transaccion import Transaccion
from Wunallet.capaLogica.gestorAplicacion.productosFinancieros.ahorro import Ahorro
from Wunallet.capaLogica.gestorAplicacion.productosFinancieros.credito import Credito
from Wunallet.capaLogica.gestorAplicacion.productosFinancieros.cuenta import Cuenta
from Wunallet.capaLogica.gestorAplicacion.infoClientes.banco import Banco
from Wunallet.capaLogica.gestorAplicacion.infoClientes.usuario import Usuario


class BajoMonto(Ahorro):

    '''El Array de clase de clientes de encarga de guardar todas las instancias de
    Cliente para poder guardar y cargarlas en la serializacion'''
    _bajoMonto=[]

    #Constructor
    def __init__(self, nroCuenta, titular, saldo, banco, tipoDeCuenta,tasaDeInteres,limiteMensual,acumuladorTransferencia):
        super().__init__(nroCuenta,titular,saldo,banco,tipoDeCuenta,tasaDeInteres)
        self._limiteMensual=limiteMensual
        self._acumuladorTransferencia=acumuladorTransferencia
        BajoMonto._bajoMonto.append(self)

    '''Verifica si el usuario cuenta con saldo y capaciadad suficiente en sus límites mensuales para realizar la transacción. De
    ser así realiza los ajustes de saldo en cada cuenta, crea el objeto transaccion y lo añade al historial de las cuentas
     involucradas.'''

    @dispatch(Cuenta,float)
    def transferir(self,cuentaDestino,valorTransferencia):
        if self.saldo>= valorTransferencia and valorTransferencia + self._acumuladorTransferencia<=self._limiteMensual:

            self.restarSaldo(valorTransferencia)
            cuentaDestino.sumarSaldo(valorTransferencia)
            trans = Transaccion(self,cuentaDestino,valorTransferencia)
            self.historialTransferencia.append(trans)
            cuentaDestino.historialTransferencia.append(trans)
            self._acumuladorTransferencia+=valorTransferencia
            return True
        else:
            return False

    '''	Verifica si el usuario cuenta con saldo y capaciadad suficiente en sus límites mensuales para realizar el pago de la cuota
    mensual. De ser así realiza los ajustes de saldo en la cuenta y el crédito crea el objeto transaccion y lo añade al 
     historial de la cuenta origen.'''
    @dispatch(Credito)
    def transferir(self,credito):
        if self.saldo >= credito.getCuotaMensual() and credito.getCuotaMensual()+self._acumuladorTransferencia<=self._limiteMensual:
            self.restarSaldo(credito.getCuotaMensual())
            credito.setDeuda(credito.getDeuda()-credito.getCuotaMensual())
            trans = Transaccion(self,credito.getBanco().getNombreBanco(),credito.getCuotaMensual())
            self.historialTransferencia.append(trans)
            self._acumuladorTransferencia+=credito.getCuotaMensual()
            return True
        else:
            return False


    '''Verifica que la cuenta tenga un saldo mayor al costo de romper topes, crea una nueva cuenta de ahorro con los datos de la
    cuenta bajo monto, y le setea su historial para preservar toda la información de la cuenta.'''

    def romperTopes(self):
        salida = False
        if self.getSaldo()<Gestor.costoRomperTopes:
            salida=False
        else:
            nuevaCuentaAhorro = Ahorro(self.getNroCuenta(),self.getTitular(),(self.getSaldo()-Gestor.costoRomperTopes),self.getBanco(),"ahorro",self.getTasaDeInteres(), self.getHistorialTransferencia())
            salida=True

        return salida

    #-------------------------------------- Metodos get-set --------------------------------------

    @classmethod
    def getBajoMonto(cls): return BajoMonto._bajoMonto
    
    @classmethod
    def setBajoMonto(cls, bajoMonto): BajoMonto._bajoMonto = bajoMonto

    def  setLimiteMensual(self, limiteMensual) : self._limiteMensual = limiteMensual

    def  getlimiteMensual(self) : return self._limiteMensual

    def  setAcumuladorTransferencia(self, acumuladorTransferencia) :	self._acumuladorTransferencia = acumuladorTransferencia

    def  getAcumuladorTransferencia(self) :	return self._acumuladorTransferencia
	
    def  getHistorialTransferencia(self): return self.historialTransferencia
	
    def  setHistorialTransferencia(self, historial): self._historialTransferencia = historial


