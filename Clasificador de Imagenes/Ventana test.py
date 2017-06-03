import Tkinter
from PIL import Image, ImageTk
 
imagenAnchuraMaxima=600
imagenAlturaMaxima=300
 
# abrimos una imagen
img = Image.open('11.jpeg')
 
root = Tkinter.Tk()
 
# titulo de la ventana
root.title("Mostrar imagen")
 
# Convertimos la imagen a un objeto PhotoImage de Tkinter
tkimage = ImageTk.PhotoImage(img)
 
# Ponemos la imagen en un Lable dentro de la ventana
label=Tkinter.Label(root, image=tkimage, width=imagenAnchuraMaxima, height=imagenAlturaMaxima).pack()
 
# Mostramos la ventana
root.mainloop()




ventana.mainloop()