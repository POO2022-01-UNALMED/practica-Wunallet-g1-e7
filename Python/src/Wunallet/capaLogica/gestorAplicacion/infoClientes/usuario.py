'''Clase Usuario
 Como piedra angular del diseño, cada instancia de esta clase representa un _usuario. Es su información y operaciones las que dan
 sentido y cohesión a todas las demás clases, y es el único parámetro que todas las funcionalidades deben garantizar.'''
from Wunallet.capaLogica.gestorAplicacion.infoClientes.banco import Banco
from Wunallet.capaLogica.gestorAplicacion.infoClientes.perfilCrediticio import PerfilCrediticio
from Wunallet.capaLogica.gestorAplicacion.infoClientes.comportamientoDePago import comportamientoDePago
from Wunallet.capaLogica.gestorAplicacion.productosFinancieros.credito import Credito
#from gestorAplicacion.productosFinancieros.cuenta import Cuenta


class Usuario:

    '''El Array de clase de clientes de encarga de guardar todas las instancias de
    Cliente para poder guardar y cargarlas en la serializacion'''
    _usuario=[]
    #Constructor
    def __init__(self, _perfilCrediticio,_ingresoMensuales,_cc,_creditoActivo=None):
        self._perfilCrediticio=_perfilCrediticio
        self._ingresosMensuales=_ingresoMensuales
        self._cc=_cc
        self._creditoActivo=_creditoActivo

        self._listaInscritos=[]
        self._bancosAsociados=[]
        self._cuentasAsociadas=[]

        Usuario._usuario.append(self)

    '''Extrae el objeto banco a partir de su nombre, para luego buscar en dicho objeto la cuenta solicitada y añadirla a la lista
    de cuentas incritas'''

    def inscribir(self,numeroCuenta,nombreBanco):
        banco=Banco.extraerBanco(nombreBanco)
        cuenta=banco.extraerCuenta(numeroCuenta)
        self._listaInscritos.append(cuenta)


    '''Verifica si el _usuario tiene perfil crediticio o le crea y asigna uno en caso contrario. Posteriormente se verifica que
    el comportamientoDePago sea válido, y luego se verifica que el _usuario esté en capacidad de asumir una cuota mensual
    tentativa. De ser así el crédito se crea, se asigna al _usuario, se ajusta el saldo de la cuenta del _usuario en la que
    recibirá el saldo del crédito y se deja registro del crédito en el banco. Su retorno permitirá gestionar el comportamiento
    de la interfaz'''

    def solicitarCredito(self,user,banco,monto,plazo,cuentaSc):
        salida=0
        if self.getPerfilCrediticio()==None:
            perfil = PerfilCrediticio(_user=user,_ingresosMensuales=user.getIngresosMensuales(),_nivel=comportamientoDePago.randomNivel())
            user.setPerfilCrediticio(perfil)
            
        print(salida,"Se creo PC")
        print(user.getPerfilCrediticio().getComportamientoDePago().getNivel())
        if user.getPerfilCrediticio().getComportamientoDePago().getNivel()==3 :
            salida=1
            
        else:
            print(salida,"Credito Rechazado 1")
            datos = [banco,monto,plazo]
            print(datos)
            cuotaTentativa=Credito.simularCredito(banco,monto,plazo)
            print(salida,"Se creo CT")
            if cuotaTentativa>self.getPerfilCrediticio().getCapacidadEndeudamiento():
                salida=2
                print(salida,"Credito Rechazado 2")
            else:
                credito = Credito(self, banco, monto, cuotaTentativa)
                self.setCreditoActivo(credito)
                cuentaSc.setSaldo(cuentaSc.getSaldo()+monto)
                salida=3
                print(salida,"Credito Aceptado 3")

        return salida

    #Remueve de la lista cuentasAsociadas la cuenta dada en el parámetro.
    def removerCuentaAsociada(self,cuenta):
        self.getCuentasAsociadas().remove(cuenta)

    #Remueve de la lista listaInscritos la cuenta dada en el parámetro.
    def removerCuentaInscrita(self,cuenta):
        self.getListaIncritos().remove(cuenta)

    #Formateo del texto que se imprime con los objetos usuario
    def __str__(self):
        print("Las cuentas inscritas del usuario"+self.getCc()+" son: ")
        for i in self.getListaIncritos():
            print(i.getNroCuenta())


    '''-------------------------------------- Métodos get-set --------------------------------------'''
    @classmethod
    def getUsuario(cls): return Usuario._usuario

    @classmethod
    def setUsuario(cls,usuario): Usuario._usuario = usuario

    def  setIngresosMensuales(self, ingresosMensuales) :	self._ingresosMensuales = ingresosMensuales

    def  getIngresosMensuales(self) : return self._ingresosMensuales

    def  setPerfilCrediticio(self, perfilCrediticio) :	self._perfilCrediticio = perfilCrediticio

    def  getPerfilCrediticio(self) : return self._perfilCrediticio

    def  setCc(self, cc) :	self._cc = cc

    def  getCc(self) : return self._cc

    def  setCreditoActivo(self, creditoActivo) : self._creditoActivo = creditoActivo

    def  getCreditoActivo(self) :	return self._creditoActivo

    def  getListaIncritos(self): return self._listaInscritos

    def  getCuentasAsociadas(self): return self._cuentasAsociadas