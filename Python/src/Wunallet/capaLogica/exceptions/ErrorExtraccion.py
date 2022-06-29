# Exception ErrorExtraccion

# Esta clase/exception es llamada cuando se intenta extraer un objeto de alguna estructura de datos, y dicho objeto no está.
# Extiende de error de ejecución ya qué, si el programa continuase su ejecución, se realizarían operaciones entre tipos 
# potencialmente indeseados que forzarían la detención del programa.

from Wunallet.capaLogica.exceptions.ErrorEjecucion import ErrorEjecucion

class ErrorExtraccion(ErrorEjecucion):

    def __init__(self, articulo, tipoObjeto, complemento="."):
        cadena = f'{articulo} {tipoObjeto} no existe{complemento}'
        super().__init__(cadena)
