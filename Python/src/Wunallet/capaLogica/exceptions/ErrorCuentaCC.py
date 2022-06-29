# Exception ErrorCuentaCC

# Esta clase/exception es lanzada cuando no se puede realizar una verificación exitosa de la identidad de un usuario (mediante
# su cédula), con la cuenta que se piensa que tiene dicho usuario, en la funcionalidad de Inscripción. Extiende de ErrorLógico
# ya que si bien se podría realizar la inscripción del objeto cuenta al usuario, sería indebido desde el diseño que un usuario
# inscribiera una cuenta (obteniendo transferencias inmediatas que no piden formularios de datos), si la información del destino
# no es acertada y consistente.

from Wunallet.capaLogica.exceptions.ErrorLogico import ErrorLogico

class ErrorCuentaCC(ErrorLogico):

    def __init__(self,itemA, itemB):
        super().__init__(itemA + " no concuerda con " + itemB)
