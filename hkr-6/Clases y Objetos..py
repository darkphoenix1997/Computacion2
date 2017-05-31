
# coding: utf-8

# In[ ]:

from math import sqrt
class Point():
    
    def __init__(self,x,y):
        self.x= x
        self.y= y
    
    def move(self,x,y):
        self.x+= x
        self.y+= y
    
    def reset(self):
        self.x= 0
        self.y= 0
    
    def Dist2P(self,OtroPunto):
        puntos=(pow(OtroPunto.x-self.x),2) + (pow(OtroPunto.y-self.y),2)
        return sqrt(puntos)

vacia=[]

for i in range((int(raw_input())/2)):
    
    vacia.append(Point(*map(int,raw_input().split())).Dist2P(Point(*map(int,raw_input().split()))))

for i in vacia:
    print i
#Luis Manuel Garcia Valdivia.

