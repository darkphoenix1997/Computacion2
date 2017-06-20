
# coding: utf-8

# In[ ]:


from Tkinter import *
import tkFileDialog as dialog
from PIL import Image, ImageTk
import os

class Imagen():
    def __init__(self, rout, name, label,id, direc):
        self.rout = rout
        self.name = name
        self.label = label
        self.id = str(id)
        self.direct = direc

    def __repr__(self):
        return (self.Name)

class Directorio:
    def __init__(self):
        self.etiquetas = {}
        self.path = os.path.dirname(os.path.realpath(__file__))
        self.id = 0

    def Verificar_imagenes(self, direc):
        a = []
        for i in os.listdir(direc):
            if i.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                a.append([i, direc])
            elif os.path.isdir(direc + '/' + i):
                for i in self.Verificar_imagenes(direc + '/' + i):
                    a.append(i)
            else:
                pass
        return a

class ventana:

    def __init__(self, images):
        self.ventana = Tk()
        self.ventana.title('Clasificador de imagenes')
        self.images = images
        self.main_screen()

    def main_screen(self):
        for child in self.ventana.winfo_children():
            child.destroy()
        frame1 = Frame(self.ventana, bg='Honeydew')
        frame1.pack(fill=BOTH, expand=1)
        Button(frame1, fg='Dark Olive Green', activeforeground='Honeydew', bg='Honeydew', activebackground='white', borderwidth=0, text='Buscar carpeta con imagenes.', command=self.carpeta).pack(expand=1)
        self.screen()
        self.ventana.mainloop()

    def open_image(self, tag, etiquetas, actual, r, equis=None):
        if 0 <= actual[0] + r < len(etiquetas):
            if all(isinstance(i, Imagen) for i in etiquetas):
                try:
                    actual[0] += r
                    img = Image.open(etiquetas[actual[0]].direc+'/'+etiquetas[actual[0]].etiquetas)
                    img = img.resize((500, 400), Image.ANTIALIAS)
                    img = ImageTk.PhotoImage(img)
                    tag['image'] = img
                    tag.image = img
                    if isinstance(variable, Entry):
                        equis.delete(0, END)
                        equis.insert(0, etiquetas[actual[0]].label)
                    else:
                        pass
                except:
                    actual[0] += r
            elif all(isinstance(j, list) for j in etiquetas):
                try:
                    i, path = etiquetas[actual[0] + r]
                    img = Image.open(path + '/' + i)
                    actual[0] += r
                    img = img.resize((500, 500), Image.ANTIALIAS)
                    img = ImageTk.PhotoImage(img)
                    tag['image'] = img
                    tag.image = img
                except:
                    etiquetas.pop(actual[0] + r)
        else:
            print "Sus imagenes han terminado."

    def carpeta(self):

        dir = dialog.askdirectory()

        if os.path.isdir(dir):
            for child in self.ventana.winfo_children():
                child.destroy()

            image_list = self.images.Verificar_imagenes(dir)
            elemento = [0]

            fps = Frame(self.ventana)
            fps.pack(side=TOP, fill=BOTH, expand=2)

            izquierda = Frame(self.ventana)
            izquierda.pack(side=LEFT, fill=BOTH, expand=2)

            derecha = Frame(self.ventana)
            derecha.pack(side=RIGHT, fill=BOTH, expand=2)

            centro = Frame(self.ventana)
            centro.pack(side=BOTTOM, fill=BOTH, expand=2)

            img_label = Label(fps)
            img_label.pack()

            Label(centro, text='Label: ',bg='snow').grid(row=0, column=0)
            tag = Entry(centro)
            tag.grid(row=0, column=1)
            Button(izquierda, text='Back',bg='snow',borderwidth=0, command=lambda: self.open_image(img_label, image_list, elemento, -1)).pack()
            Button(derecha, text='Next',bg='snow', borderwidth=0, command=lambda: self.open_image(img_label, image_list, elemento, 1)).pack()
            Button(centro, text='Back to the start',bg='snow', borderwidth=0, command=self.main_screen).grid(row=2, column=1)

            self.open_image(img_label, image_list, elemento, 0)
            self.screen()

        else:
            return False

    def screen(self):
        option_menu = Menu(self.ventana)
        self.ventana.config(menu=option_menu)
        config_menu = Menu(option_menu)


x = Directorio()
y = ventana(x)