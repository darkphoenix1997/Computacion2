
# coding: utf-8

# In[ ]:

m=int(raw_input("Ingrese el número de filas: "))
n=int(raw_input("Ingrese el número de columnas: "))
minimo = min(m,n)

A=[]
suma=[]
for j in range(m):
  A.append([0]*n)
  
print "Lectura de la matriz A"
for j in range(m):
  for k in range(n):
    A[j][k] = (raw_input("Dame el componente (%d,%d): " %(j+1,k+1)))
print A

#Convertir tupla a enteros.(en progreso)
#Luis Manuel Garcia Valdivia


