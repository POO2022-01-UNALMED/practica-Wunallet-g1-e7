'''/* Clase Credito

Son los objetos creados cuando a un usuario se le aprueba su solicitud de crédito. Su función va desde almacenar los detalles del
préstamo y a qué banco pertenece, hasta ofrecer simulaciones de crédito.'''

from gestorAplicacion.infoClientes.banco import Banco
#from gestorAplicacion.infoClientes.usuario import Usuario


class Credito:

    '''El Array de clase de clientes de encarga de guardar todas las instancias de
    Cliente para poder guardar y cargarlas en la serializacion'''

    _credito=[]

    def __init__(self, _titular,_banco,_deuda,_cuotaMensual):

        self._titular=_titular
        self._banco=_banco
        self._deuda=_deuda
        self._cuotaMensual=_cuotaMensual

        Credito._credito.append(self)

    '''Es un método estático que se ejecuta para verificar si, al solicitar un crédito, la cuota mensual esperada no supera la
    capacidad de endeudamiento del usuario. El método toma la tasa de interes anual del banco, y hará el siguiente cálculo
    
    Deuda = (1+((tasaInteresAnual/12)*plazoEnMeses))*monto
    
    Es decir, el monto que pide, más el interés aplicado a ese monto multiplicado por el plazo del crédito. Una vez calculada la
    deuda, se retorna el valor Deuda/Plazo (valor de cada cuota)'''

    @classmethod
    def simularCredito(cls,banco,monto,plazo):
        deuda= (1+((banco.getTasaInteresAnual()/12)*plazo))*monto
        return deuda/plazo

    '''-------------------------------------- Métodos get-set --------------------------------------'''
    
    @classmethod
    def getCredito(cls): return Credito._credito

    @classmethod
    def setCredito(cls, credito):Credito._credito = credito
    
    def  setTitular(self, titular) : self._titular = titular

    def  getTituar(self) : return self._titular
	
    def  setBanco(self, banco) :self._banco = banco

    def  getBanco(self) : return self._banco
	
    def  setDeuda(self, deuda) :self._deuda = deuda

    def  getDeuda(self) : return self._deuda

    def  setCuotaMensual(self, cuotaMensual) : self._cuotaMensual = cuotaMensual

    def  getCuotaMensual(self) : return self._cuotaMensual