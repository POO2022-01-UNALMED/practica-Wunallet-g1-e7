from ErrorLogico import ErrorLogico

class ErrorNoSaldo(ErrorLogico):

    ## Aquí se deben cambiar los parámetros del init según los datos que se quieran pasar al mostrar el error
    def __init__(self, saldo, requerimiento, tipoProceso):
        super().__init__("Proceso cancelado por saldo insuficiente. \n\n El saldo de tu cuenta es {saldo} pero necesitas almenos {requerimiento} para culminar el proceso de {tipoProceso}")
