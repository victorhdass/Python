# -*- coding: utf-8 -*-
"""
Created on Sat May 22 17:29:23 2021

@author: Adm
"""

y = int(input('digite um limite:'))

print('2')
for i in range (1,y):
    for j in range (2,y):
        if (i%j) == 0:
           
            break
        elif i>j and (i%j)!=0 and (j == i-1):
            print (i)
            continue             
           