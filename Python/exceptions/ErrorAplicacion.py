class ErrorAplicacion(Exception):

    mensajeGeneral = "## Manejo de errores de la aplicación ##\n"

    def __init__(self, cadena):
        self.mensajeEspecifico =  cadena
        super().__init__(self.mensajeEspecifico + self.mensajeGeneral)

    def getMensajeEspecifico(self):
        return self.mensajeEspecifico
