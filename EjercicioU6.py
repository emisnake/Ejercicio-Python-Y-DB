from tkinter import *

import sqlite3
from sqlite3 import Error

root = Tk()
root.title("EjercicioU5")
subtititulo = Label(root, text="Ingrese sus datos", bg="DarkOrchid3", fg="thistle1", height=1, width=60)
subtititulo.grid(row=0, column=0, columnspan=3, padx=1, pady=1, sticky=W)

pimercampo = Label(root, text="Titulo")
pimercampo.grid(row=1, column=0, sticky=W)
segundocapo = Label(root, text="Rutta")
segundocapo.grid(row=2, column=0, sticky=W)
tercercampo = Label(root, text="Descripción")
tercercampo.grid(row=3, column=0, sticky=W)

campo1= StringVar()
campo2= StringVar()
campo3= StringVar() 


def Muestra(valor,fila,columna):
	entrada = Entry(root, textvariable=valor)
	entrada.grid(row=fila, column=columna)
	return entrada

b1 = Muestra(campo1, 1, 1)
c2 = Muestra(campo2, 2, 1)
d3 = Muestra(campo3, 3, 1)    
	
         
        




colores =      ['snow', 'old lace', 'linen', 'antique white', 'papaya whip', 'blanched almond',
               'bisque', 'peach puff','navajo white', 'alice blue', 'lavender', 'lavender blush', 'misty rose', 'dark slate gray', 'dimgray', 'slate gray',
               'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
               'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue', 'blue',
               'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
               'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
               'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olivegreen',
               'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'springgreen',
               'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
               'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
               'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
               'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
               'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
               'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
               'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2'
               'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
               'coral1', 'tomato2', 'OrangeRed2']
def colorRandom():
	
	color= random.choice(colores)
	root.configure(background=color)
a1= Button(root, text= "Sorpresa", command= colorRandom)
a1.grid(row=4,column=2)


Lista=[]

def limpiar():
    b1.delete(0, END)
    c2.delete(0, END)
    d3.delete(0, END)   
    
def alta():
        if ((campo1.get() == "") and (campo2.get() == "") and (campo3.get() == "")):error()
        else:
                diccionario = dict(Titulo=campo1.get(),Ruta=campo2.get(),Descripción=campo3.get())
                global Lista
                Lista.append(diccionario)
                print(len(Lista)-1)
                print("Revise sus datos")
                for x in Lista:
                        print(x)
                limpiar()

"""def basededatos():
    try:
        mibase= mysql.connector.connect(host="localhost", user="root", passwd="")
        micursor= mibase.cursor()
        micursor.execute("CREATE DATABASE baseprueba1")
    except:
        print("La base de datos ya existe")

    try:
        mibase= mysql.connector.connect(host="localhost", user="root", database="baseprueba1")
        micursor= mibase.cursor()
        micursor.execute("CREATE TABLE producto(id int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT, Titulo VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL, Ruta VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL, Descripción text COLLATE utf8_spanish2_ci NOT NULL)")
		mibase.commit()
    except:
        print("La tabla ya existe")

b2= Button(root, text="Crear bd", command=basededatos)
b2.grid(row=4, column=0)

a2= Button(root, text= "Alta", command= alta)
a2.grid(row=4, column=1)


root.mainloop()"""

