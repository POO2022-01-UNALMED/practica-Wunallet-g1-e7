# Clase Banco

# Cada instancia de esta clase representa uno de los bancos integrados al software, y en sus atributos almacenan toda la
# información sobre sus productos e identidad.

#from gestorAplicacion.productosFinancieros.corriente import Corriente
#from gestorAplicacion.productosFinancieros.credito import Credito
#from gestorAplicacion.productosFinancieros.cuenta import Cuenta

class Banco:

    listaBancos=[]

    '''El Array de clase de clientes de encarga de guardar todas las instancias de
    Cliente para poder guardar y cargarlas en la serializacion'''
    banco = []

    #Constructor
    def __init__(self, _nombreBanco,_tasaInteresAnual):
        self._nombreBanco = _nombreBanco
        self._tasaInteresAnual=_tasaInteresAnual
        Banco.listaBancos.append(self)
        Banco.banco.append(self)

        self._listaCuentas=[]
        self._listaCreditos=[]

    '''Recorre iterativamente la listaBancos de la clase Banco, buscando un banco cuyo nombre coincida con el parámetro ingresado. De
    existir retornará el objeto.'''
    @classmethod
    def extraerBanco(self,_nombreBanco):
        for i in range(len(Banco.listaBancos)):
            if(_nombreBanco == Banco.listaBancos[i].getNombreBanco()):
                banco = Banco.listaBancos[i]
        return banco

    '''Recorre iterativamente la listaDeCuentas del banco desde donde se invoca el método, buscando una cuenta que tenga el numero
    de cuenta ingresado.'''
    def extraerCuenta(self,nroCuenta):
        for i in range(len(self.getListaCuentas())):
            if(nroCuenta==self.getListaCuentas()[i].getNroCuenta()):
                cuenta=self.getListaCuentas()[i]
        return cuenta

    #Añade un crédito a la listaCreditos del banco.
    def añadirCredito(self,credito):
        self._listaCreditos.append(credito)
    # Remueve la cuenta del parámetro de la listaCuentas del banco.
    def removerCuenta(self,cuenta):
        self.getListaCuentas().remove(cuenta)



    '''-------------------------------------- Metodos get-set --------------------------------------'''
    @classmethod
    def getBanco(cls):  return Banco.banco

    @classmethod
    def setBanco(cls,banco): Banco.banco = banco

    def setNombreBanco(self, _nombreBanco): self._nombreBanco = _nombreBanco

    def  getNombreBanco(self): return self._nombreBanco

    def  getListaCuentas(self):	return self._listaCuentas

    def  getListaCreditos(self): return self._listaCreditos

    def  getTasaInteresAnual(self) : return self._tasaInteresAnual
