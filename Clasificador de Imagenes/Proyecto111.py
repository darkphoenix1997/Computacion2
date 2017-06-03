# coding: utf-8

# In[ ]:

from os import listdir
import os.path
from PIL import Image
import os


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
					img = Image.open(mypat + "/" + i)
					img.show()
					etiquetas = {}
					a = raw_input("Etiqueta:")
					if a in etiquetas:
						etiquetas[a].append(Imagen(i, mypat, a, os.stat(mypat + "/" + i)[6]))
					else:
						etiquetas[a] = [Imagen(i, mypat, a, os.stat(mypat + "/" + i)[6])]
					img.close()

					print etiquetas
					b=raw_input("Categoria:") #Convertir a metodo.
					print 'Existe', len(etiquetas[b]),'imagenes en esta categoria:',etiquetas[a]
