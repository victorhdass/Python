# -*- coding: utf-8 -*-

#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
#------------------------------------------------------------------

'''

    Nome: Victor Hugo da Silva Souza
    NUSP: 9301238

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
def main():
    '''
        Testes das suas funções

        Deve conter ao menos 10 testes distintos cobrindo casos
        básicos, como listas vazias, com apenas um elemento etc.
        e casos genéricos com vários elementos.
    '''
    print("Testes do EI22 - ordenação por intercalação")
    seq1 = [7, 11, 56]
    seq2 = [-5, 7, 99, 104]
    print(intercale_seqs(seq1, seq2))
    seq2 = [4,30,11,5,10]
    seq1= [ 2,5,28,33]
    print(intercale_seqs(seq1, seq2))
    seq1= [ 12,15,228,3]
    seq2 = [0,41,25,3,58]
    
    print(intercale_seqs(seq1, seq2))
    seq1 = [ 22,3,55,4,2]
    seq2 = [3,25,88,5]
    print(intercale_seqs(seq1, seq2))
    # escreva seus testes

## ------------------------------------------------------------------

def intercale_seqs(seq1, seq2):
    ''' (list, list) -> list

    Recebe seq1 e seq2, duas listas tal que:

        - seq1 é crescente com n1 >= 0 elementos e
        - seq2 é crescente com n2 >= 0 elementos
        
    Retorna uma lista com n1+n2 elementos, contendo
    os elementos de seq1 e seq2 em ordem crescente.

    Exemplo para 
        seq1 = [7, 11, 56] e 
        seq2 = [-5, 7, 99, 104]
    
    a função deve retornar a lista:
        [-5, 7, 7, 11, 56, 99, 104]
    '''

    # escreva sua solução
    
    h = seq1+seq2
    n = len(seq1+seq2)
    
    for i in range (1,n):
         if h[n-i] <h[n-i-1]:
             u = h[n-i-1]
             k = h[n-i]
             h[n-i] = u
             h[n-i-1] = k
         if h[n-i] >h[n-i-1]:
             for j in range (1,n-i+1):
                 if h[n-i] <h[n-i-j]:
                    u = h[n-i-j]
                    k = h[n-i]
                    h[n-i] = u
                    h[n-i-j] = k 
                 
    return h
#--------------------------------------------
if __name__ == '__main__':
    main()