# -*- coding: utf-8 -*-
"""
Created on Sat May 22 02:11:33 2021

@author: Adm
"""


y = int(input('digite um n:'))
count = 0
u=0
while count <y:
    count = count +1    
    numero = int(input("digite um numero:"))
    
    if count %2 == 1 :
       soma =numero
       
       u += soma
       soma = 0         
     
    print(u)