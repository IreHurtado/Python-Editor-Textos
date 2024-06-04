"""Este es un editor de textos creado con el modulo tkinter para python"""

#Importamos los módulos

from tkinter import *
from tkinter import font, filedialog, PhotoImage



#Definimos nuestras funciones

def guardar():

    global texto

    documento=texto.get("1.0","end-1c")

    #filedialog nos permite seleccionar donde guardar el archivo

    guardarEn=filedialog.asksaveasfilename()

    archivo=open(guardarEn, "w+")

    archivo.write(documento)

    archivo.close()

#Funciones para tipografias

def arial():
    global texto
    texto.config(font="Arial")

def times():
    global texto
    texto.config(font="Times")

def verdana():
    global texto
    texto.config(font="Verdana")

#Funciones para negrita e italica

def bold():
    global texto
    texto.config(font=("Arial", 14,'bold'))

def italic():
    global texto
    texto.config(font=("Arial", 14,'italic'))

#Creamos la ventana

root=Tk()
root.title("Editor de textos en Python")

#Agregamos los botones e insertamos comandos

imagen_guardar= PhotoImage(file="guardar.png")
botonGuardar=Button(root, command=guardar, image=imagen_guardar)
botonGuardar.grid(row=1, column=0)
botonGuardar.config(font=("Arial", 10, "bold"), fg="black")

botonFuente=Menubutton(root,text="Fuente")
botonFuente.grid(row=1, column=1)
botonFuente.config(font=("Arial", 10, "bold"), fg="black")

botonFuente.menu = Menu(botonFuente, tearoff=0)
botonFuente["menu"]=botonFuente.menu
botonFuente.menu.add_checkbutton(label="Arial", command=arial)
botonFuente.menu.add_checkbutton(label="Times", command=times)
botonFuente.menu.add_checkbutton(label="Verdana", command=verdana)

botonBold=Button(root, command=bold, text="Bold")
botonBold.grid(row=1, column=2)
botonBold.config(font=("Arial", 10, "bold"), fg="black")

botonItalica=Button(root, command=italic, text="Italica")
botonItalica.grid(row=1, column=3)
botonItalica.config(font=("Arial", 10, "bold"), fg="black")

#Creamos el control de texto

texto=Text(root)
texto.grid(row=2, columnspan=5)
texto.config(font=("arial", 12, "bold"))

mainloop()