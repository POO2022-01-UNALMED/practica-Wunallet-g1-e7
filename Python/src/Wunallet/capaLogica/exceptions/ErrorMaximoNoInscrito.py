# Exception ErrorMaximoNoInscrito

# Esta clase/exception es llamada cuando un usuario quiere enviar a una cuenta no inscrita una cantidad superior a la cantidad 
# máxima permitida. Extiende de ErrorLogico ya que las operaciones se podrían ejecutar pero dañarían los comportamientos
# esperados y presupuestados del sistema.

from Wunallet.capaLogica.exceptions.ErrorLogico import ErrorLogico

class ErrorMaximoNoInscrito(ErrorLogico):

    def __init__(self):
        super().__init__("El valor que ingresó supera el valor permitido para cuentas no inscritas. Recuerde que el valor maximo a transferir a una cuenta no inscirta es de 3'000.000")
