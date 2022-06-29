from exceptions.ErrorAplicacion import ErrorAplicacion

class ErrorEjecucion(ErrorAplicacion):

    def __init__(self, cadena):
        super().__init__("--- Potencial error de ejecución ---\n\n" + cadena)



