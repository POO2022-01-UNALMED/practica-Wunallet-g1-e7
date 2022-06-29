# Exception ErrorEjecucion

# Esta clase/exception es la clase padre de todos los errores que producen (o pueden producir más adelante) un error que fuerce a
# detener la ejecución del programa por errores sintácticos o semánticos. 

from Wunallet.capaLogica.exceptions.ErrorAplicacion import ErrorAplicacion

class ErrorEjecucion(ErrorAplicacion):

    def __init__(self, cadena):
        super().__init__("--- Potencial error de ejecución ---\n\n" + cadena)



