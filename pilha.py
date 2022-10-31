# -*- coding: utf-8 -*-

#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
#------------------------------------------------------------------

'''

    Nome:Victor Hugo da Silva Souza
    NUSP:9301238

    Ao preencher esse cabeçalho com o meu nome e o meu número USP,
    declaro que todas as partes originais desse exercício programa
    foram desenvolvidas e implementadas por mim e que, portanto, não 
    constituem desonestidade acadêmica ou plágio.
    
    Entendo que trabalhos sem assinatura devem receber nota zero e, ainda
    assim, poderão ser punidos por desonestidade acadêmica.
    Declaro também que sou responsável por todas as cópias desse
    programa e que não distribui ou facilitei a sua distribuição.
    
    Estou ciente que os casos de plágio e desonestidade acadêmica
    estarão sujeitos às penalidades descritas na página da disciplina
    na seção "Sobre colaboração em MAC0122".

    Reconheço que utilizei as seguintes fontes externas ao conteúdo 
    utilizado e recomendado em MAC0122, ou recebi auxílio das pessoas
    listadas abaixo.

    - LISTA de fontes externas utilizadas (links ou referências como livros)
        - 

    - LISTA das pessoas que me auxiliaram a fazer esse trabalho
        - 
'''


## ==================================================================
## Escreva a sua função palindromo()

def palindromo( s ):
    ''' documentacao da funcao '''
    i = 0
    j=0
    u =[]
    v = []
    
    while i < len(s):
        u += s[i] 
        i+=1
    while j < len(s):
        v += s[len(s)-i]
        j+=1
        
    if v == u:
        return True
    else:
        return False


## ==================================================================
##
class Pilha:

     def __init__(self):
         self.dados = []

     def vazia(self):
         return self.dados == []

     def empilhe(self, item):
         self.dados.append(item)

     def desempilhe(self):
         return self.dados.pop()

     def topo(self):
         return self.dados[len(self.dados)-1]

     def size(self):
         return len(self.dados)

## ==================================================================
## Escreva outras funções e classes caso desejar


## ==================================================================
if __name__ == '__main__':
    palindromo( '' )

