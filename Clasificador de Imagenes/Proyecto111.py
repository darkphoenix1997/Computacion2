
# coding: utf-8

# In[ ]:

from os import listdir
import os.path
from PIL import Image
import os
from Tkinter import *
from PIL import ImageTk, Image
import Tkinter as tk

class Imagen():
	def __init__(self, Name, Rout, Label, Weigth):
		self.Name = Name
		self.Rout = Rout
		self.Label = []
		self.Weigth = Weigth
	def __repr__(self):
		return (self.Name)


mypat = "C:\Users\Luis Manuel\Desktop\Proyecto"


class Labels():
	if os.path.isdir(mypat):
		for i in listdir(mypat):
			if os.path.isdir(mypat + "/" + i):
				pass
			elif os.path.isfile(mypat + "/" + i):
				if i.endswith(".jpg") or (".jpeg") or (".gif") or (".png"):
					#INTERFAZ GRAFICA.(en proceso).

					def hacer_click():
						valor2 = entrada_txt.get()
						etiqueta.config(text=valor2)

					app = Tk()
					app.title("Clasificador de imagenes")
					app.geometry('700x500')
					app.configure(bg='dark turquoise')
					vp = Frame(app)
					vp.grid(column=0, row=0, padx=(50, 50), pady=(10, 10,))

					try:
						img = ImageTk.PhotoImage(Image.open('11.jpeg'))    #prueba.
						panel = Label(app, image=img)
					except:
						'Comprueba tu  archivo.'

					valor = ""
					entrada_txt = Entry(vp, width=10, textvariable=valor)
					entrada_txt.grid(column=3, row=1)

					vp.columnconfigure(0, weight=1)
					vp.rowconfigure(0, weight=1)
					etiquetaz = Label(vp, text="Etiqueta:",fg='white')
					etiquetaz.grid(column=1, row=1)
					boton = Button(vp, text="Listo.",bg='dark turquoise',fg='white', command=hacer_click)
					boton.grid(column=4, row=1)

					app.mainloop()

	#				etiquetas = {}  #DICCIONARIO.
	#				a = raw_input("Etiqueta:")
	#				if a in etiquetas:
	#					etiquetas[a].append(Imagen(i, mypat, a, os.stat(mypat + "/" + i)[6]))
	#				else:
	#					etiquetas[a] = [Imagen(i, mypat, a, os.stat(mypat + "/" + i)[6])]
#
#					print etiquetas
#					b=raw_input("Categoria a buscar:")  #CONVERTIR A METODO.
#					if b in etiquetas:
#						print 'Existe', len(etiquetas[b]),'imagenes en esta categoria:',etiquetas[a]
#					else:
#						print "No es posible encontrar esa categoria."
#
#					c=raw_input("Imagen a buscar:")  #CONVERTIR A METODO.
#					if c in etiquetas:
#						print etiquetas[a]
#					else:
#						print "Verifique la etiqueta del elemento a acceder."
						print "Verifique la etiqueta del elemento a acceder"
