from Wunallet.capaLogica.exceptions.ErrorLogico import ErrorLogico

class ErrorNoSaldo(ErrorLogico):

    ## Aquí se deben cambiar los parámetros del init según los datos que se quieran pasar al mostrar el error
    def __init__(self, saldo=None, requerimiento=None, tipoProceso=None, considerarLimiteSaldo=False):
        if considerarLimiteSaldo:
            super().__init__(f"Tu operación ha sido rechazado ya que no cuentas con saldo suficiente o tu producto de origen no permite mover el valor indicado.")
        else:
            super().__init__(f"Proceso cancelado por saldo insuficiente. \n\n El saldo de tu cuenta es {saldo} pero necesitas almenos {requerimiento} para culminar el proceso de {tipoProceso}")
