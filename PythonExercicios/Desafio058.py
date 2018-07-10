from random import randint
print('=========Desafio 058========')
aleatorio = randint(0, 10) #numero inteiro entre 1 e 10
numero = -1
tentativas = 0
acertou = False
while not acertou:
    numero = int(input('Escolha um numero de 0 a 10: '))
    tentativas += 1
    if aleatorio == numero:
        print('Você acertou!')
        acertou = True
    elif aleatorio > numero:
        print('Você Errou! Numero é maior')
    else:
        print('Você Errou! Numero é menor')
print('Seu numero é {} numero aletorio é {}'.format(numero, aleatorio))
print('Numero te palpites até acertar foi de {} vezes'.format(tentativas))
