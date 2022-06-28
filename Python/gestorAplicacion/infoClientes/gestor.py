'''/Interface Gestor
Esta interface le exige a las clases que la implementan que declaren métodos de gestión de dichos productos financieros.
 Adicionalmente almacena constantes relevantes para la gestión de dichos productos.'''

from abc import ABC, abstractmethod

class Gestor(ABC):

    costoRomperTopes = 15000.0

    #Metodo para sumar saldo del producto bancario en que se implementa.
    @abstractmethod
    def sumarSaldo(self,valorTransferencia): pass

    #Metodo para restar saldo del producto bancario en que se implementa.

    @abstractmethod
    def restarSaldo(self,valorTransferencia): pass