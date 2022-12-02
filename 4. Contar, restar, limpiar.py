#4: Contador, restador y limpiar conteo

import tkinter as tk
from tkinter import ttk


def sumar():
    numero.set(str(int(numero.get()) + 1))     

def restar():
    numero.set(str(int(numero.get()) - 1))  
    
def limpiar():
    numero.set("0")
    
    
root = tk.Tk()
root.title("Contador, Restador y limpiar")
root.geometry("400x250")
root.config(bg="#404258")

numero = tk.StringVar(root, "0")
num = tk.Entry(root, textvariable=numero, justify="center")
num.pack()
num.place(x=140, y=50)

contador = ttk.Button(root, text="Count Up", command=sumar)
contador.pack()
contador.place(x=165, y=90)

restar = ttk.Button(root, text="Count Down", command=restar)
restar.pack()
restar.place(x=165, y=130)

limpiar = ttk.Button(root, text="Reset", command=limpiar)
limpiar.pack()
limpiar.place(x=165, y=170)

root.mainloop() 