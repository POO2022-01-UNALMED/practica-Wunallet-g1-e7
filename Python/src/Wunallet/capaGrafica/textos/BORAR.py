import tkinter as tk
import pathlib
import os
from tkinter import Label, Entry, Button, Text, PhotoImage, Frame, INSERT, scrolledtext
from PIL import Image,ImageTk
import os 
import pathlib
import codecs
import io
import sys

path = os.path.join(pathlib.Path(__file__).parent.absolute())

with open(path+"/0.txt", encoding="utf-8") as archivo:
    # Y al abrir para escribir
    # with open("salida.txt", "w", encoding="utf-8") as a:
    for linea in archivo:
        print(linea)
        # a.write(linea)