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


class Horario:
    '''Classe utilizada para representar um horário.

    Um horário é representado por três números inteiros maiores ou iguais
    a zero, armazenados em um atributo do tipo lista e de nome 'dados'.
 
       * `dados[2]`: um número inteiro entre 0 e 23 que indica horas
       * `dados[1]`: um número inteiro entre 0 e 59 que indica minutos
       * `dados[0]`: um número inteiro entre 0 e 59 que indica segundos

    Essa classe deve se "comportar" ilustrados no enunciado.
    '''
        
    def __init__(self, horas, minutos, segundos, dados):
        self.dados = [horas, minutos, segundos]
        if horas < 10 and (minutos and segundos >10) :
            self.horas = '0'+str(dados[0])
            self.minutos = dados[1]
            self.segundos = dados[2]
        if minutos < 10 and (segundos>10 and segundos<60) and (horas>10 and horas<24) :
            self.horas = dados[0]
            self.minutos = '0'+str(dados[1])
            self.segundos = dados[2]
        if segundos < 10 and (minutos>10 and minutos<60) and (horas >10 and horas<24) :  
            self.horas = dados[0]
            self.minutos = dados[1]
            self.segundos = '0'+str(dados[2])
        if segundos < 10 and minutos<10 and (horas >10 and horas<24):  
            self.horas = dados[0]
            self.minutos = '0' +str(dados[1])
            self.segundos = '0'+str(dados[2])
        if segundos < 10 and minutos<10 and horas <10:  
            self.horas = '0'+str(dados[0])
            self.minutos = '0' +str(dados[1])
            self.segundos = '0' +str(dados[2])
        if horas < 10 and minutos<10 and (horas >10 and horas<24): 
            self.horas = '0'+str(dados[0])
            self.minutos = '0' +str(dados[1])
            self.segundos = dados[2]
        if segundos < 10 and horas<10 and (minutos >10 and minutos <60):
            self.horas = '0'+str(dados[0])
            self.minutos = dados[1]
            self.segundos ='0' +str(dados[2])
        if (segundos <= 59 and segundos >= 10) and (horas>=10 and horas <=24) and (minutos >=10 and minutos <=59) :
            self.horas = dados[0]
            self.minutos = dados[1]
            self.segundos = dados[2]
        if segundos>59 or horas >23 or minutos >59:
            print('digite um numero valido')
        
    def __repr__(self):
        return f"{self.horas}:{self.minutos}:{self.segundos}"
    def __add__(self,other):
        if int(self.horas)+int(other.horas) >= 24:
            self.horas = (int(self.horas)+int(other.horas))%24
        else:
            self.horas = int(self.horas)+int(other.horas)
        if int(self.minutos)+int(other.minutos)>= 60:
             self.minutos = (int(self.minutos)+int(other.minutos))%60   
        else:
             self.minutos = int(self.minutos)+int(other.minutos)
        if int(self.segundos)+int(other.segundos)>= 60:
            self.segundos = int(self.segundos)+int(other.segundos)%60
        else:
            self.segundos = int(self.segundos)+int(other.segundos)
        
        return Horario(int(self.horas),int(self.minutos),int(self.segundos))
    def __add__(self)
   