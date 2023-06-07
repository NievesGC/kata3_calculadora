import tkinter as tk
from calculator.controls import Display,CalcButton

WIDTH = 272
HEIGHT = 300

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora") #ponemos el titulo de la ventana
        self.geometry(f"{WIDTH}x{HEIGHT}") #le decimos el tamaño de la ventana con las constantes que hemos creado arriba

        self.display = Display(self) #llamamos a display (que es el contenedor frame donde dentro esta la label)
        self.display.pack() #dibujamos display centrado y arriba porque la geometria pack viene asi predefinida 
        self.display2 = Display(self) 
        self.display2.pack(side =tk.BOTTOM) 
        self.display.typing("ARRIBA") #llamamos e introdicimos el texto que la class dispplay 
        self.display2.typing("ABAJO")
        
        CalcButton(self,self.clic1,"1").pack() 
        CalcButton(self,text="2",tiny_wire=self.clic2).pack()
        CalcButton(self,text="3",tiny_wire=self.clic3).pack()
        CalcButton(self,text="4",tiny_wire=self.clic4).pack()

    def clic1(self):
        self.display.typing("1")

    def clic2(self):
        self.display2.typing("2")

    def clic3(self):
        self.display.typing("3")

    def clic4(self):
        self.display2.typing("4")