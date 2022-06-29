# Exception ErrorDeTipo

# Esta clase/exception es llamada cuando el tipo de dato que ingresa un usuario no corresponde al tipo de dato esperado o requerido
# por el sistema. Corresponde a un error de ejecución ya que sin esta excepción se podrían hacer operaciones enter tipos
# incompatibles que resultarían en la detención del programa.

from Wunallet.capaLogica.exceptions.ErrorEjecucion import ErrorEjecucion

class ErrorDeTipo(ErrorEjecucion):

    def __init__(self, indicacionError):
        super().__init__(indicacionError)
