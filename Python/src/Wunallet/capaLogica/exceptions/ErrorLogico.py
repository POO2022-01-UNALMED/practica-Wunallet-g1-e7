# Exception ErrorLogico

# Esta clase/exception es la clase padre de todos los errores que sin ser perjudiciales para la ejecución correcta del programa,
# suponen un error para la lógica que impone nuestro diseño del sistema bancario. 

from Wunallet.capaLogica.exceptions.ErrorAplicacion import ErrorAplicacion

class ErrorLogico(ErrorAplicacion):

    def __init__(self, cadena):
        super().__init__("--- Error lógico ---\n\n" + cadena)



