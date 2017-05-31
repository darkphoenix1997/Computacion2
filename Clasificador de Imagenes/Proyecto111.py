
# coding: utf-8

# In[ ]:

from os import listdir
import os.path
from PIL import Image
import os


class Imagen():
  def __init__(self,Name,Rout,Label,Weigth):
## incluir el id de imagen
    self.Name=Name
    self.Rout=Rout
    self.Label=Label # Tiene que ser una lista
    self.Weigth=Weigth

# La Etiqueta es una lista por ejemplo ["Gatos","Perros","Lugares"]

## Vas a construir una structura (lista o arbol que permita agregar elementos imagen)
## Incluir los siguientes metodos
## Buscar Imagenes por categoria
## Mostrar imagenes por categoria
	
	
mypat="C:\Users\Luis Manuel\Desktop\Proyecto"

class Labels():  
    if os.path.isdir(mypat):
	  for i in listdir(mypat):
	    if os.path.isdir(mypat+"/"+i):
	      pass
	    elif os.path.isfile(mypat+"/"+i):
	      if i.endswith(".jpg") or (".jpeg") or (".gif") or (".png"):
	        img=Image.open(mypat+"/"+i)
	        img.show()
	        etiquetas={}
	        a=raw_input("Ponga su etiqueta:")	      
	        if a in etiquetas:
	          etiquetas[a].append(Imagen(i,mypat,a,os.stat(mypat+"/"+i)[6]))
	        else:
	          etiquetas[a]=[Imagen(i,mypat,a,os.stat(mypat+"/"+i)[6])]
	        img.close()

