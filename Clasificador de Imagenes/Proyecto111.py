

# coding: utf-8

# In[ ]:

from os import listdir
import os.path
from PIL import Image
import os
from Tkinter import *
from PIL import ImageTk, Image
import Tkinter as tk
import PIL

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
				if i.lower().endswith(".jpg") or (".jpeg") or (".gif") or (".png"):
					etiquetas = {}  # DICCIONARIO.
					#				a = raw_input("Etiqueta:")
					#				if a in etiquetas:
					#					etiquetas[a].append(Imagen(i, mypat, a, os.stat(mypat + "/" + i)[6]))
					#				else:
					#					etiquetas[a] = [Imagen(i, mypat, a, os.stat(mypat + "/" + i)[6])]

					#INTERFAZ GRAFICA.(en proceso).

					#def hacer_click():
					#	valor2 = entrada_txt.get()
					#	etiqueta.config(text=valor2)

					ventana = tk.Tk()
					ventana.title("Clasificador de imagenes")
					ventana.geometry('1000x600')
					ventana.configure(background='dark turquoise')

					#def etiquetar():
					#	etiquetas = {}
					#	# DICCIONARIO.
					#	if a in etiquetas:
					#		etiquetas[a].append(Imagen(i, mypat, a, os.stat(mypat + "/" + i)[6]))
					#	else:
					#		etiquetas[a] = [Imagen(i, mypat, a, os.stat(mypat + "/" + i)[6])]

					e1 = tk.Label(ventana, text="Etiqueta:", bg='black', fg='white')
					e1.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

					entrada1 = tk.Entry(ventana,width=10)
					entrada1.pack(fill=tk.X, padx=5, pady=5, ipadx=5, ipady=5)
					entrada1.focus_set()

					#def callback():
					#	print text

					boton = tk.Button(ventana, text="Listo", bg='black', fg='white') #,command=callback
					boton.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

					img = Image.open(mypat + "/" + i)
					res=img.resize((400, 400), Image.ANTIALIAS)
					img2=ImageTk.PhotoImage(res)
					label = tk.Label(ventana, image=img2)
					label.pack()

					# def hacer_click():
					#   valor2=entrada_txt.get()
					#  etiqueta.config(text=valor2)

					# vp=Frame(ventana)
					# vp.grid(column=0,row=0,padx=(50,50),pady=(10,10))
					# vp.columnconfigure(0,weight=1)
					# vp.rowconfigure(0,weight=1)

					# etiquetass=Label(vp,text="Escribe")
					# etiquetass.grid(column=1,row=1)
					# boton=Button(vp,text="Apuchame",command=hacer_click)
					# boton.grid(column=2,row=2)
					# valor=""
					# entrada=Entry(vp,width=10,textvariable=valor)
					# entrada.grid(column=3,row=1)

					mainloop()

					#entrada1 = tk.Entry(ventana, width=10)
					#entrada1.pack(fill=tk.X, padx=5, pady=5, ipadx=5, ipady=5)
					#text = entrada1.get()

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
