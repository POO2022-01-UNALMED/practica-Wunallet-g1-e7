from Wunallet.capaLogica.exceptions.ErrorLogico import ErrorLogico

class ErrorMaximoNoInscrito(ErrorLogico):

    def __init__(self):
        super().__init__("El valor que ingresó supera el valor permitido para cuentas no inscritas. Recuerde que el valor maximo a transferir a una cuenta no inscirta es de 3'000.000")
