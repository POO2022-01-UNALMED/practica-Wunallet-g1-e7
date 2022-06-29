# import tkinter as tk
from Wunallet.inicio import Inicio

def main():

    app = Inicio()

    app.mainloop()
    
    print("Hola")
    return 0

if __name__ == '__main__':
    print("antes de main()")
    main()
    print("después de main()")