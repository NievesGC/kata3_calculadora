import tkinter as tk

class Ventana(tk.Tk):
    def __init__(self):
        super().__init__() #super para que deje invocar tk.TK
        self.title("Mi primera pantalla kinter")
        self.geometry("800x600+400+100")
        self.label = tk.Label(self, text = "",bd = 2, relief = tk.RAISED, width = 50)
        self.label.pack()
        self.valor_nombre = tk.StringVar()
        nombre = tk.Entry(self, textvariable = self.valor_nombre) 
        nombre.pack()
        boton = tk.Button(self,text = "Pulsame",command =self.imprimir_saludo ) 
        boton.pack()

    def imprimir_saludo(self):
        self.label.config(text = f"Hola,{self.valor_nombre.get()}")

  
Ventana().mainloop()