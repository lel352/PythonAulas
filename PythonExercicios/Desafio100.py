from builtins import print
from random import randint
print('=========Desafio 100========')

def sorteia(lista):
    print('-' * 20)
    print('Números: ')
    for v in range(0, 5):
        lista.append(randint(1, 10))
        print(f'{lista[v]}', end=' ')
    print(' - Números Sorteados.')

def somaPar(lista):
    print('-'*20)
    print('Par(es): ')
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
            print(f'{v}', end=' ')
    print(f' - Soma dos valores pares é {soma}')

lista = list()
sorteia(lista)
somaPar(lista)

