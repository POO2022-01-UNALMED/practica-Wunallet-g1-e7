# import tkinter as tk
from Wunallet.inicio import Inicio
from Wunallet.capaLogica.baseDatos.deserializador import Deserializador
# from Wunallet.capaLogica.baseDatos.deserializado import deserializar

def main():

    app = Inicio()

    app.mainloop()
    
    print("Hola")
    return 0

if __name__ == '__main__':
    print("Si estoy deserializando en teoria")
    Deserializador.deserializarTodo()
    # deserializar()
    main()
