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


import numpy as np

## ------------------------------------------------------------------
def main():

    print("Testes da classe NPImagem\n")

## ------------------------------------------------------------------
class NPImagem():
    # escreva aqui os métodos da classe NPImagem
    def __init__(self, shape=(0, 0), val=0):
        
        if type(val) is np.ndarray:
            self.data = val.copy()
        else:
            self.data = np.full(shape, val) 
        self.shape = self.data.shape
    
    def crop(self, sup=0, esq=0, inf=None, dir=None):
       ''' (NPImagem, int, int, int, int) -> NPImagem
       RECEBE uma NPImagem self e inteiros sup, esq, inf e dir.
       RETORNA uma nova NPImagem formada pelos pixels de self na janela 
           retangular delimitada pelas posições [sup, esq] e [inf, dir].
       '''
       if inf is None or dir is None:
            inf, dir = self.shape
            novo_data   =  np.copy(self.data[sup:inf, esq:dir])
            nova_imagem = NPImagem((),novo_data)
            return nova_imagem
    def pinte_retangulo(self, sup, esq, inf, dir, val=0):
        self_nlins,  self_ncols = self.shape
        # forma da janela *virtual/imaginária* com val que será sobreposta sobre self
        other_nlins, other_ncols = inf - sup, dir - esq
        if sup >= self_nlins or esq >= self_ncols or inf <= 0  or dir <= 0:
            return
        self_sup = max(0, sup)
        self_esq = max(0, esq)
        self_inf = min(sup + other_nlins, self_nlins)
        self_dir = min(esq + other_ncols, self_ncols)
        self.data[self_sup:self_inf, self_esq:self_dir] = val
    def paste(self, other, sup, esq):
        self_nlins,  self_ncols = self.shape
        other_nlins, other_ncols = other.shape
        inf, dir = other_nlins + sup, other_ncols + esq
        
        self.data[sup:inf,esq:dir]=other.data
        
    def __add__(self, other):
        soma = 0
        for i in range(self.size):
            soma += self.data[i]+other.data[i]
        return soma
    def __mul__(self, other):
            prod = 1
            for i in range(self.size):
                prod *= self.data[i]*other.data[i]
            return prod
## ------------------------------------------------------------------
## ------------------------------------------------------------------
if __name__ == '__main__':
    main()
