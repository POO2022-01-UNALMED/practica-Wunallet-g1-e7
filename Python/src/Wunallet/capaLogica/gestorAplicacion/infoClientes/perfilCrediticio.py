# Clase PerfilCrediticio

# Cada instancia está asociada a un usuario, y describe precisamente el perfil crediticio de éste. Es usada por los bancos para
# determinar si una solicitud de crédito se aprueba o rechaza.

#from gestorAplicacion.productosFinancieros.corriente import Corriente


class PerfilCrediticio:
    '''El Array de clase de clientes de encarga de guardar todas las instancias de
	Cliente para poder guardar y cargarlas en la serializacion'''
    _perfilCrediticio=[]

    #Constructor
    def __init__(self,_user,_ingresosMensuales,_nivel):
        self._user=_user
        self._capacidadEndeudamiento=0.2*_ingresosMensuales
        self._comportamientoDePago=_nivel

        PerfilCrediticio._perfilCrediticio.append(self)

    '''-------------------------------------- Metodos get-set --------------------------------------'''
    @classmethod
    def getPerfilCrediticio(cls): return PerfilCrediticio._perfilCrediticio

    @classmethod
    def setPerfilCrediticio(cls, PerfilCrediticio): PerfilCrediticio._PerfilCrediticio = PerfilCrediticio

    def  setNombreBanco(self, user) : self._user = user

    def  getBanco(self) :return self._user

    def  setCapacidadEndeudamiento(self, nivelDeEndeudamiento) :self._capacidadEndeudamiento = nivelDeEndeudamiento

    def  getCapacidadEndeudamiento(self) : return self._capacidadEndeudamiento

    def  getComportamientoDePago(self) : return self._comportamientoDePago

