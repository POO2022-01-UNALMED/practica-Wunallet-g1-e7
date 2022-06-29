# import tkinter as tk
from Wunallet.inicio import Inicio
from Wunallet.capaLogica.baseDatos.deserializador import Deserializador

def main():

    app = Inicio()

    app.mainloop()
    
    print("Hola")
    return 0

if __name__ == '__main__':
    
    Deserializador.deserializarTodo()
    main()
