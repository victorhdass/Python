# -*- coding: utf-8 -*-
"""
Created on Sun May 23 21:03:43 2021

@author: Adm
"""

x=float(input(('digite um numero:')))
y=float(input('digite outro numero:'))
def mdc (x,y):
        
    while x>y:
            if x%y !=0 and x>y:
                x=x-y
                
                return(x)
            elif x%y == 0:
                return (y)
    while y>x:
            if y%x !=0 and y>x:
                y=y-x
                
                return(y)
            elif y%x == 0:
                return (x)
        
        
md=mdc(x,y) 
print(md)           