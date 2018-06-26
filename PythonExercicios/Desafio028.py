from random import randint
from time import sleep
print('=========Desafio 028========')
aleatorio = randint(0, 5) #numero inteiro entre 1 e 10
numero = int(input('Escolha um numero de 0 a 5: '))
print('Processando...')
sleep(2)#segundos
if aleatorio == numero:
    print('Você acertou!')
else:
    print('Você Errou!')
print('Seu numero é {} numero aletorio é {}'.format(numero, aleatorio))
