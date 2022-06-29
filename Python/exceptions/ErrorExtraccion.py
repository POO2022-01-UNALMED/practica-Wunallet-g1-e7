from exceptions.ErrorEjecucion import ErrorEjecucion

class ErrorExtraccion(ErrorEjecucion):

    ## Aquí se deben cambiar los parámetros del init según los datos que se quieran pasar al mostrar el error
    def __init__(self, articulo, tipoObjeto, complemento="."):
        cadena = f'{articulo} {tipoObjeto} no existe{complemento}'
        super().__init__(cadena)
