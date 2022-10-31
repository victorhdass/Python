# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 05:53:01 2022

@author: Adm
"""

def acha_no_conjunto():
    x = int(input('digite o tamanho do conjunto:'))
    lista = set()

    for i in range (x):
        y = input ('Digite o texto:')
        lista.add(y)
    h = input("Digite o texto a procurar:")
    if h in lista:
        print('MESMO VALOR')
    else:
        print('nenhuma correspondencia encontrada')
def add_na_lista():
    x = int(input('digite o tamanho da lista:'))
    lista =[]
    for i in range (x):
        lista += [input("Digite o elemento:")]
    return lista    
            
def acha_na_lista(lista):
    
    lenght = len(lista)
    k=0
    i=1
    while k < lenght:
       
       
       while i < lenght:
           if lista[k] == lista[i] :
               print("correspondencia encontrada em:" + f"{i+1}")
               return
           else:
                i+=1
       k+=1
        
            
            
        