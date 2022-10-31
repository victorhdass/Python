
# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO
# NÃO ALTERE OS NOMES DAS FUNÇÕES, MÉTODOS E ATRIBUTOS
#------------------------------------------------------------------

'''
    Nome:Victor Hugo da Silva Souza
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
#####################################################################
# MÓDULOS A SEREM UTILIZADOS NO PROGRAMA
# random.shuffle(lst) embaralha os elementos da lista lst.
import random 

#####################################################################
def main():


    print("INÍCIO DOS TESTES")

    # testes da função circular()
    print("Função circular()")
    amigos1 = [1,2,3,4,0]
    amigos2 = [1,2,0,4,3]
    print(f"circular({amigos1}) = {circular(amigos1)}")
    print(f"circular({amigos2}) = {circular(amigos2)}")

    # testes da função experimento()
    print("Função experimento()")
    semente = int(input("Digite o valor da semente do gerador de números pseudo-aleatórios: "))
    random.seed(semente)
    MINN  = int(input("Qual o número mínimo de pessoas: "))
    MAXN  = int(input("Qual o número máximo de pessoas: "))
    passo = int(input("Qual o passo: "))
    T     = int(input("Qual o número de tentativas em cada experimento: "))
    SHOW  = input("Você quer ver as listas que são circulares [s/n]: ")

    debug = False
    if SHOW == 'S' or SHOW == 's':
        debug = True

    N = MINN
    while N <= MAXN:
        pN = experimento(N, T, debug)
        print(f"p({N}) = {pN}")
        N = N + passo

print("TESTES ENCERRADOS")    

###################################################################
def sorteie_amigos( N ):
    ''' (int) -> list
    RECEBE um inteiro N > 0.
    RETORNA uma lista de tamanho N, contendo os números de 0 a N em 
        ordem aleatória.

ATENÇÃO: a tabulação das linhas foi removida e a ordem de algumas 
linhas alterada. Ela deve ser consertada antes possa ser utilizada.
'''
    i = 0
    
    amigos = []
    while i < N:
        
        amigos += [i]
        i +=1
    random.shuffle(amigos)
   
    return amigos
        
######################################################################
def circular(amigo_de):
    ''' (list) -> bool 
    RECEBE uma lista amigo_de (de "amigos secretos")
    RETORNA True se a lista for circular e False em caso contrário.
    '''
    # modifique o código abaixo para conter a sua solução.
    
    j=0
    u = True
    while j < len(amigo_de):
         
         if (amigo_de[j] == j) and j!=0:
                u = False
         elif  j == amigo_de[amigo_de[j]] and j>1:
                u = False
         elif (j>=0 and j<=1) and (amigo_de[j] !=j):
                u = True        
         j+=1
    return u 
###################################################################
def experimento(N, T, debug=False):
    ''' (int, int) -> float
    RECEBE um inteiro N > 0, um inteiro T > 0 e um booleano debug.
    RETORNA a probabilidade de uma lista de "amigo secretos" com
        N participantes ser circular.

    Esta probabilidade deve ser calculada a partir de T sorteios 
    de listas de tamanho N, e calculando a frequência das listas 
    circulares.

    Se a opção debug é True a função deve imprimir todas as 
    listas sortedas que forem circulares, como mostrado no
    enunciado.
    '''
    # modifique o código abaixo para conter a sua solução.
    k = 0
    u = 0
    v = 0
    
    while k < T :
        amigxs = sorteie_amigos(N)

        if circular(amigxs) == True:
            u+=1
            
        else:
            v+=1
        k+=1
        if debug == True and circular(amigxs) == True:
            print(amigxs)
            
     
    return u/(v+u)
#=====================================================================
# Não modifique as linhas abaixo
# Esse if serve para executar a main() dentro do Spyder
# e não atrapalhar o avaliador
if __name__ == '__main__':
    main()
