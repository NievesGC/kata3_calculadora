import tkinter as tk #truco para abreviar rl tkinter (solo con import) 
#from tkinter import ttk - para libreria de estilos

def imprimir_saludo():
    label.config(text=f"Hola,{valor_nombre.get()}") #config - configura lo que le sale en lo que le has dicho delante 


root = tk.Tk() #crear la pantalla
root.title("Mi primera pantalla tkintel") #poner titulo de la pantalla
#print(root.geometry()) #ver el tamaño de la ventana

root.geometry("800x600+400+100") #cambiar el tamaño de la pantalla + coordenadas en las que aparece

label = tk.Label(root, text = "Hola mundo!",bd = 2, relief = tk.RAISED, width = 50) #para determinarle parametros (padre(donde aparecera),parametro,parametro...) bd = borde/relief relieve/wiidth ancho
label.pack()
#label.place(x = 100, y =100) # con esta geometria le dices que aparezca y en que posicion
#label1 = tk.Label(root, text = "Y ahora otra label")
#label.pack() #esta geometria le dice que parezca  centrada 
#label1.pack(side =tk.LEFT) #Le puedes decir donde ponerla


valor_nombre = tk.StringVar() # es una clase que va ser una variable de control get()-saber valor y set()

nombre = tk.Entry(root, textvariable = valor_nombre) #sirve para generar una barra en la que puedes escribir
nombre.pack()

boton = tk.Button(root,text = "Pulsame",command =imprimir_saludo ) #comand funcion que se va llmar cada vez que se aga click en el boton
boton.pack()
root.mainloop() #es necesario invocarlo para que todo funciones