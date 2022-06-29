# Exception ErrorCamposVacios

# Esta clase/exception es lanzada cuando en un formulario el usuario no ingresa los campos solicitados y obligatorios.
# Es hija de ErrorEjecucion ya que si el usuario no suministra dichos datos, el procesamiento de las funcionalidades procurarían 
# hacer operaciones con objetos que no están determinados o son del tipo incorrecto (None), generando así que el programa,
# eventualmente, detenga su ejecución.

from Wunallet.capaLogica.exceptions.ErrorEjecucion import ErrorEjecucion

class ErrorCamposVacios(ErrorEjecucion):

    def __init__(self):
        super().__init__("Se deben llenar todos los campos")


