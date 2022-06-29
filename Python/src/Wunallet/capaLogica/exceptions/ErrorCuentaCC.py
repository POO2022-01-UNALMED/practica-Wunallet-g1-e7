from Wunallet.capaLogica.exceptions.ErrorLogico import ErrorLogico

class ErrorCuentaCC(ErrorLogico):

    ## Aquí se deben cambiar los parámetros del init según los datos que se quieran pasar al mostrar el error
    def __init__(self,itemA, itemB):
        super().__init__(itemA + " no concuerda con " + itemB)
