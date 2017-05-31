
# coding: utf-8

# In[ ]:

import sys

x =[]
a=[]

for i in xrange(6):
    x.append(map(int,raw_input().strip().split(' ')))

for i in xrange((len(x)-2)):
    for ii in xrange((len(x[i])-2)):
        a.append(x[i][ii:ii+3]+[x[i+1][ii+1]]+x[i+2][ii:ii+3])

print sum(max(a,key=lambda x: sum(x)))

#Luis Manuel Garcia Valdivia.

