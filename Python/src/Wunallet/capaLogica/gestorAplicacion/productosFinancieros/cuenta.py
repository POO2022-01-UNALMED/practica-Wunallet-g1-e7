# Clase Abstracta Cuenta

# Como clase abstracta se encarga de dar el cuerpo, a nivel de atributos y métodos, a sus clases hijas: Ahorro, Corriente y
# BajoMonto. Siempre están asociadas a un banco y usuario.

from abc import ABC, abstractmethod
from Wunallet.capaLogica.gestorAplicacion.infoClientes.gestor import Gestor
#from gestorAplicacion.infoClientes.banco import Banco
#from gestorAplicacion.infoClientes.usuario import Usuario
#from gestorAplicacion.infoClientes.transaccion import Transaccion

class Cuenta(Gestor,ABC):
    #Constructor
    def __init__(self, nroCuenta, titular, saldo, banco, tipoDeCuenta):
        self.nroCuenta = nroCuenta
        self.titular = titular
        self.saldo = saldo
        self.banco = banco
        self.tipoDeCuenta = tipoDeCuenta
        self.historialTransferencia=[]

    '''Al ser ejecutado desde la cuenta origen, itera sobre la lista historialTransferencia e imprime cada uno de los
    objetos ya formateados por el método toString()'''

    def verHistorial(self):
        historialString = ''
        for i in range(len(self.historialTransferencia)):
            historialString += self.historialTransferencia[i].getDescripcion() + '\n'
        return historialString

    '''Ejecutará las comprobaciones y actualizaciones de saldo correspondientes al realizar una transferencia. Este proceso depende
    del tipo de cuenta que lo ejecute, y por eso debe ser un método abstracto. Ademas se utiliza *args ya que deberia existir una sobrecarga
    del metodo, debido a que tambien corresponde a las comprobaciones y actualizaciones de saldo correspondientes al realizar el pago de un crédito.'''

    @abstractmethod
    def transferir(self, *args):
        pass

    '''Es un método implementado por requerimiento de la interfaz gestor. Sumará el saldo del parámetro a la cuenta desde la que se 
    invoca el método'''

    def sumarSaldo(self,valor):
        self.setSaldo(self.getSaldo()+valor)

    '''Restará el saldo del parámetro a la cuenta desde la que se invoca el método.'''
    def restarSaldo(self,valor):
        self.setSaldo(self.getSaldo()-valor)

    '''-------------------------------------- Metodos get-set --------------------------------------'''

    def setNroCuenta(self, nroCuenta): self.nroCuenta = nroCuenta

    def getNroCuenta(self): return self.nroCuenta

    def setTitular(self, titular): self.titular = titular

    def getTitular(self):  return self.titular

    def setSaldo(self, saldo):  self.saldo = saldo

    def getSaldo(self):  return self.saldo

    def setBanco(self, banco): self.banco = banco

    def getBanco(self): return self.banco

    def setTipoCuenta(self, tipoDeCuenta):  self.tipoDeCuenta = tipoDeCuenta

    def getTipoCuenta(self): return self.tipoDeCuenta

    def getHistorialTransferencia(self): return self.historialTransferencia

    def setHistorialTransferencia(self,historialTransferencia): self.historialTransferencia=historialTransferencia


















