# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES, MÉTODOS E ATRIBUTOS
# NÃO APAGUE OS DOCSTRINGS
#------------------------------------------------------------------
     
'''
    Nome: Victor Hugo da Silva Souza
    NUSP: 9301238

    Ao preencher esse cabeçalho com o meu nome e o meu número USP,
    declaro que todas as partes originais desse exercício programa (EP)
    foram desenvolvidas e implementadas por mim e que portanto não 
    constituem desonestidade acadêmica ou plágio.
    Declaro também que sou responsável por todas as cópias desse
    programa e que não distribui ou facilitei a sua distribuição.
    Estou ciente que os casos de plágio e desonestidade acadêmica
    serão tratados segundo os critérios divulgados na página da 
    disciplina.
    Entendo que EPs sem assinatura devem receber nota zero e, ainda
    assim, poderão ser punidos por desonestidade acadêmica.

    Abaixo descreva qualquer ajuda que você recebeu para fazer este
    EP.  Inclua qualquer ajuda recebida por pessoas (inclusive
    monitores e colegas). Com exceção de material de MAC0110, caso
    você tenha utilizado alguma informação, trecho de código,...
    indique esse fato abaixo para que o seu programa não seja
    considerado plágio ou irregular.

    Exemplo:

        A monitora me explicou que eu devia utilizar a função int() quando
        fazemos leitura de números inteiros.

        A minha função quicksort() foi baseada na descrição encontrada na 
        página https://www.ime.usp.br/~pf/algoritmos/aulas/quick.html.

    Descrição de ajuda ou indicação de fonte:

'''

# escreva seu programa a seguir
x=input('Digite n:')


h=0
for i in range (0,len(x)):  
        
        h=h+(i+1)*int(x[i])
        i+=1
        if i == len(x):
         h=h
         
if h%11 == 10:
    dv1 = 0
else:
    dv1 = h%11
    

k=0
for i in range (0,len(x)):  
        
        k=k+(i)*int(x[i])
        i+=1
        if i == len(x):
            k=k + i*dv1
            
if k%11 == 10:
    dv2 = 0
else:
    dv2 = k%11


print( 'DVs =', f'{dv1}', f'{dv2}')