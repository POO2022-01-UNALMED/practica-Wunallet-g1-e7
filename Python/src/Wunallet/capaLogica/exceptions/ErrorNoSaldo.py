# Exception ErrorNoSaldo

# Esta clase/exception es llamada cuando una cuenta no tiene saldo o capacidad para concluir una operación. Es hija de la clase
# ErrorLogico ya que si bien las operaciones que se deben realizar son sintácticamente correctas, carecen de sentido bajo la
# lógica del programa (i.e., aunque tiene sentido sintáctico y semántico restar 1.000 - 2.000, no tiene sentido lógico bajo
# nuestro objetos ya que esto nos daría cuentas con saldos negativos, lo que, en general, está prohibido).


from Wunallet.capaLogica.exceptions.ErrorLogico import ErrorLogico

class ErrorNoSaldo(ErrorLogico):

    def __init__(self, saldo=None, requerimiento=None, tipoProceso=None, considerarLimiteSaldo=False):
        if considerarLimiteSaldo:
            super().__init__(f"Tu operación ha sido rechazado ya que no cuentas con saldo suficiente o tu producto de origen no permite mover el valor indicado.")
        else:
            super().__init__(f"Proceso cancelado por saldo insuficiente. \n\n El saldo de tu cuenta es {saldo} pero necesitas almenos {requerimiento} para culminar el proceso de {tipoProceso}")
