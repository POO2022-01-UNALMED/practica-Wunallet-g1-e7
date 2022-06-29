# Enum comportamientoDePago

# Este enum es usado como atributo en la clase PerfilCrediticio y según su nivel aprueba o rechaza uno de los filtros
# para aprobar una solicitud de crédito

import random
from enum import Enum

class comportamientoDePago(Enum):
    BUENO=1
    REGULAR=2
    MALO=3

    #Constructor
    def __init__(self, _nivel):
        self._nivel=_nivel


    #Método para seleccionar aleatoriamente un nivel del enum.
    @classmethod
    def randomNivel(cls):
        return random.choice(list(comportamientoDePago))

    def setNivel(self, level): self._nivel = level

    def getNivel(self): return self._nivel




