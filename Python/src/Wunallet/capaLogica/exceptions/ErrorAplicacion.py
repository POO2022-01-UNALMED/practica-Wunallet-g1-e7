# Exception ErrorAplicacion

# Esta clase/exception siempre es llamada al ser la clase padre de todas las demás clases Exception definidas en el proyecto.
# En nuestro sistema su funcionalidad consiste en aportar el título característico "Manejo de errores de la aplicación" a las
# ventanas de error, así como producir y almacenar los atributos y métdos para el mensaje de error específico que se construye 
# desde sus clases hijas.

class ErrorAplicacion(Exception):

    mensajeGeneral = "## Manejo de errores de la aplicación ##\n"

    def __init__(self, cadena):
        self.mensajeEspecifico =  cadena
        super().__init__(self.mensajeEspecifico)

    def getMensajeEspecifico(self):
        return self.mensajeEspecifico
