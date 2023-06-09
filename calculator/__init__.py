import tkinter as tk
from calculator.controls import Display,CalcButton, KeyBoard
from cromannumbers import RomanNumber, RomanNumberError
WIDTH = 272
HEIGHT = 300

operaciones ={
     "+": lambda a,b:a+b,
     "-": lambda a, b: a-b,
     "x": lambda a, b: a*b,
     "÷": lambda a, b: a//b
}

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora") #ponemos el titulo de la ventana
        self.geometry(f"{WIDTH}x{HEIGHT}") #le decimos el tamaño de la ventana con las constantes que hemos creado arriba
        self.op1 =  None
        self.op2 = None 
        self.operation = None
        self.equal = False
        self.value= ""

        self.display = Display(self) #llamamos a display (que es el contenedor frame donde dentro esta la label)
        self.display.pack() #dibujamos display centrado y arriba porque la geometria pack viene asi predefinida 
        self.display.typing("0")
        KeyBoard(self,self.clic).pack()
        

    def reset(self):
        self.value = ""
        self.op1 = self.op2 = self.operation = None
        self.equal = False

    def clic(self,tecla):
        try:
            if tecla == "AC":
                    self.reset()
                
            elif tecla in(operaciones):
                if self.operation:
                    if self.equal:
                        resultado = RomanNumber(self.value)
                    else:
                        self.op2 = RomanNumber(self.value)
                        resultado = operaciones[self.operation](self.op1, self.op2)
                    self.op1 = resultado
                    self.op2 = None
                    self.value = resultado.simbolo
                else:
                    self.op1= RomanNumber(self.value)
                self.operation = tecla
            elif tecla == "=":
                if self.equal:
                    resultado = operaciones[self.operation](RomanNumber(self.value),self.op2)
                else:
                    self.op2= RomanNumber(self.value)
                    resultado = operaciones[self.operation](self.op1,self.op2)
                self.value = resultado.simbolo
            else:
                if self.equal:
                    self.reset()
                

                if self.operation is not None and self.op2 is None:
                        self.value = ""
                        self.op2 = ""
                self.value+= tecla
            
            self.display.typing(self.value)
            
            self.equal = tecla == "="
        except RomanNumberError:
            self.value = "ERROR"
            self.display.typing(self.value)
            self.reset()

   
         