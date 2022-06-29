from exceptions.ErrorEjecucion import ErrorEjecucion

class ErrorDeTipo(ErrorEjecucion):

    ## Aquí se deben cambiar los parámetros del init según los datos que se quieran pasar al mostrar el error
    def __init__(self, indicacionError):
        super().__init__(indicacionError)
