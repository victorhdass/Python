# -*- coding: utf-8 -*-
"""
Created on Sun May 16 00:07:46 2021

@author: Adm
"""

import math
x = [1,5,7,8,9,31,25,11]
y = [3,2,1,5,8,7,9,11]

x.sort()
y.sort()



def mediana(x):
    
    if len(x)%2 == 0:
        return (x[len(x)//2]+x[(len(x)-1)//2])/2
    elif len(x)%2 ==1:
        return x[(len(x)-1)-(len(x)//2)]

def media (x):
    k=0
    avg = 0
    while k < len(x):
      k=k+1
      avg += x[k-1]
 
    return avg/len(x)

def media_x_ao_quadrado(x):
    k=0
    avg_1 = 0
    while k < len(x):
      k=k+1
      avg_1 += x[k-1]**2
 
    return avg_1/len(x)


def media_xy (x,y):
  h=0
  for i in range (0,len(y)):   
           
            h=h+(x[i]-medx)*(y[i]-medy)
            if i==(len(x)-1):
                
                return h/len(x)      

print (y)

print(x)

medx = media(x)
medy = media(y)
m = mediana(x)

media_y_ao_quadrado = media_x_ao_quadrado(y)
med_x_quadrado = media_x_ao_quadrado(x)
med_y_quadrado = media_x_ao_quadrado(y)
varx=(med_x_quadrado)-(medx**2)
vary = med_y_quadrado-medy**2
dpx = math.sqrt(varx)
dpy = math.sqrt(vary)
cov = media_xy(x,y)

print(f'Lista: {x}')
print(f'Mediana: {m}')
print(f'Elementos: {len(x)}')
print(f'Média: {medx}')
print(f'media de y :{medy}')
print(f'Variancia de x: {varx}')
print(f'Variancia de y: {vary} ')
print(f'desvio padrao de x: {dpx}')
print(f'desvio padrao de y: {dpy}')
print(f'covariancia (x,y):{cov}')