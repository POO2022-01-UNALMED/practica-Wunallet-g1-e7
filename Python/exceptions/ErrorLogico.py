from exceptions.ErrorAplicacion import ErrorAplicacion

class ErrorLogico(ErrorAplicacion):

    def __init__(self, cadena):
        super().__init__("--- Error lógico ---\n\n" + cadena)



