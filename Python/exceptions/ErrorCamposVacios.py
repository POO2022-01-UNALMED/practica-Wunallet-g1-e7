from ErrorEjecucion import ErrorEjecucion

class ErrorCamposVacios(ErrorEjecucion):

    ## Aquí se deben cambiar los parámetros del init según los datos que se quieran pasar al mostrar el error
    def __init__(self):
        super().__init__("Se deben llenar todos los campos")


