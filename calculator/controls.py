import tkinter as tk
from tkinter.font import Font

class Display(tk.Frame):                            #se crea un frame (un contenedor invisible) parea que se la label se pueda expandir detro y delimitarla 
    def __init__(self,location):
        super().__init__(location, width = 272, height = 50)  #definimos el anchoy la altura del cocntenedor
        self.pack_propagate(False)                       #dejamos la propagacion del contenedor parada ppara que la label se adapte al contenedor y no sea al contrario 
        self.label = tk.Label(self, background="#000000", text = "", foreground="#FFFFFF",                               #bg definimos el color del fondo, le metemos texto en vacio, fg definimos el color de la letra, anchor le decimos hacia que lado queremos que salga s ehace con parametros norte sur este y oeste, y con el padx le indicamos a que altura queremos que salga para que salga un poco mas a la izquierda, con la font que ademas hemos importado le decimos fuente y tamaño d efuente 
                              anchor=tk.E, padx=8, 
                              font=Font(family="Helvetica", size="40"))
        self.label.pack(side=tk.TOP, fill=tk.BOTH, expand=True) #le decimos que se expanda haacia top y both y ponemos la expansion en true ppara que se pueda expandir 

    def typing(self,text):
        self.label.config(text=text) #definimos el texto que vamos a meter

class CalcButton(tk.Frame):
    def __init__(self,location,tiny_wire,text):
        super().__init__(location, width=68,height=50)
        self.pack_propagate(False)
        self.tiny_wire = tiny_wire
        self.text = text
        self.button = tk.Button(self, text=text,command=self.pressed)
        self.button.pack(side = tk.TOP, fill=tk.BOTH, expand=True)

    def pressed(self):
        self.tiny_wire(self.text)

class KeyBoard(tk.Frame):
    def __init__(self,location,tiny_wire):
        super().__init__(location,width=272,height=250)
        CalcButton(self,tiny_wire,"AC").grid(column=0,row=0,columnspan=3,sticky="WE")
        CalcButton(self,tiny_wire,"÷").grid(column=3,row=0)
        CalcButton(self,tiny_wire,"C").grid(column=0,row=1)
        CalcButton(self,tiny_wire,"D").grid(column=1,row=1)
        CalcButton(self,tiny_wire,"M").grid(column=2,row=1,rowspan=3,sticky="NS")
        CalcButton(self,tiny_wire,"X").grid(column=0,row=2)
        CalcButton(self,tiny_wire,"x").grid(column=3,row=1)
        CalcButton(self,tiny_wire,"L").grid(column=1,row=2)
        CalcButton(self,tiny_wire,"-").grid(column=3,row=2)
        CalcButton(self,tiny_wire,"I").grid(column=0,row=3)
        CalcButton(self,tiny_wire,"V").grid(column=1,row=3)
        CalcButton(self,tiny_wire,"+").grid(column=3,row=3)
        CalcButton(self,tiny_wire,"=").grid(column=0,row=4,columnspan=4,sticky="EW")


   