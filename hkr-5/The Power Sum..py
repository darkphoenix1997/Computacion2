
# coding: utf-8

# In[ ]:

from itertools import combinations

x=int(raw_input())
n=int(raw_input())

total=0; p=[i**n for i in range(1,int(round(x**(1.0/float(n))))+1)]
for j in range(1,len(p)):
  for k in combinations(p,j):
    if sum(k)==x:
      total+=1
    else:
      pass

print total
#Luis Manuel Garcia Valdivia

