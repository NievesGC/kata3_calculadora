import tkinter as tk
from calculator.controls import Display

WIDTH = 272
HEIGHT = 300

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora") #ponemos el titulo de la ventana
        self.geometry(f"{WIDTH}x{HEIGHT}") #le decimos el tamaño de la ventana con las constantes que hemos creado arriba

        display = Display(self) #llamamos a display (que es el contenedor frame donde dentro esta la label)
        display.pack() #dibujamos display centrado y arriba porque la geometria pack viene asi predefinida 

        display.typing("Probando") #llamamos e introdicimos el texto que la class dispplay 