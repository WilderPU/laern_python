#Aprendiendo un poco de TKinter, solo para saber como funciona las interfaces gráficas.
import tkinter as tk

#Esta función permite hacer la accion del boton.
def handler():
    print("presionado")

root=tk.Tk() #Con esto creamos la ventana
root.title("Hola") #Le ponemos titulo
root.geometry("600x400") #Sive para el tamaño
root.iconbitmap("./building.ico") #pone un icono
root.resizable(0,0) #permite cambiar el tamaño de la ventano o no XD
label=tk.Label(root, text="Hello World") #Esto es un label
label.pack(side=tk.TOP) #Se empaqueta el label y se muestra en pantalla
btn=tk.Button(root, text="Boton", command=handler) #esto es un boton, y la acción que hace es una función llamada "handler"
btn.pack()
root.mainloop()

#De aquí en adelante comenzaremos atrabajar la libreria pickle
import pickle as pk

contactos = [
    {"Nome":"Wilder"},
    {"Number":"3165431660"}]

#podemos renombrar el archivo como pyw para que funcione como un programa de escritorio
#Casi se me olvida como era el comentario de python
""" Y este es el otro tipo XD"""

"""
*** LO QUE DBO ESTUDIAR ***
TKINTER
Estructuras de python (repaso)
Git and GitHub (Empezar de cero)

***************************

*** PROYECTO UN DIRECTORIO TELEFONICO ***

*****************************************
"""
