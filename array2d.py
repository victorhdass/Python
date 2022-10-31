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

def main():

    print("Testes da classe Array2d\n")


## ==================================================================
#   A classe Array2d permite a manipulação de 'matrizes' de duas 
#   dimensões. O exercício é utilizar uma lista linear, ao invés
#   de uma lista aninhada, para armazenar os dados da matriz 
#   internamente.
#   A lista linear deve ser um atributo de nome 'data'.

class Array2d:

    # ---------------------------------------------------------------
    def __init__(self, shape, val):
        ''' (Array2d, tuple, obj) -> None
        Constrói um objeto do tipo Array2d com os atributos:
        data : lista onde os valores são armazenados
        shape: tupla que armazena as dimensões da matriz
        size : número total de elementos da matriz
        '''
        print("Vixe! ainda não fiz o construtor da classe.")
        self.shape = (shape[0],shape[1])
        self.size = shape[0]*shape[1]
        self.data = [val]*self.size
        

    # ---------------------------------------------------------------
    def __getitem__(self, key):
        ''' (Array2d, tupla) -> obj
        recebe uma tupla key contendo a posição (lin, col)
        e retorna o item nessa posição do Array2d self.

        Esse método é usado quando o objeto é chamado com 
        uma tupla entre colchetes, como self[0,0]. 
        Exemplo:
        >>> a = Array2d( (2,3), -1)
        >>> a[1,1] + 100
        99
        >>> print( a[1,1] )
        -1
        '''
        b =  self.shape[1]*key[0] + key[1]
        return self.data[b]

    # ---------------------------------------------------------------
    def __setitem__(self, key, valor):
        ''' (Array2d, tupla, obj) -> None
        recebe uma tupla key contendo a posição (lin, col)
        e um objeto valor e armazena o valor nessa posição
        do Array2d self.

        Esse método é usado para atribuir 'valor' na posição
        indicada pela tupla `key`, como self[0,0] = 0. 
        Exemplo:
        >>> a = Array2d( (2,3), -1)
        >>> print( a[1,1] )
        -1
        >>> a[1,1] = 100
        >>> print( a[1,1] )
        100
        '''
        b =  self.shape[1]*key[0] + key[1]
        self.data[b] = valor
        print("Vixe! ainda não fiz o método __setitem__.")

    # ---------------------------------------------------------------
    def __str__(self):
        ''' (Array2d) -> None
        ao ser usada pela função print, deve exibir cada linha
        do Array2d em uma linha separada, separando seus elementos por um espaço.

        Exemplo: para self.data = [1, 2, 3, 4, 5, 6] e self.shape = (2,3)
        o método deve retornar a string 
        "1 2 3\n4 5 6" 
        e, caso self.shape = (3,2) o método deve retornar a string
        "1 2\n3 4\n5 6" 
        '''
        print("Vixe! ainda não fiz o método __str__.")
        for i in range (0,self.size,self.shape[1]):
             self.data[i] += '\n' 
            
        u=''
        for a in range(0,self.size):
            u += str(self.data[a])
        return print(u)
            

    # ---------------------------------------------------------------
    # Escreva outros métodos e funções caso desejar
    def getlin(self, lin):
        u =''
        for k in range(0,self.shape[1]):
             u += ' ' + str(self.data[self.shape[1]*(lin-1)+k])
        return u
    def getcol(self, col):
    
        for i in range(1,self.shape[0]):
            print(str(self.data[i*col-1]))
        
    def dot(self, other):
        x = 0
        for i in range(0,self.size):
            x +=self.data[i]*other.data[i] 
        
        
        return x
    def matmul( esq, dir ):
        resultado = Array2d((esq.shape[0],dir.shape[1]),None)
        
        for lin in range (0,esq.shape[0]):
            for col in range (0,dir.shape[1]):
                for k in range(0,dir.shape[1]):
                    resultado[lin][col] += esq.data[esq.shape[1]*(lin-1)+k]*dir.data[k*col-1]
        

        return resultado
## ==================================================================

if __name__ == '__main__':
    main()