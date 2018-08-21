from random import randint
from time import sleep
print('=========Desafio 088========')
quantidade = int(input('Quantos jogos deseja: '))
print('-'*20)
print('Sorteando os jogos')
print('-'*20)
jogos = list()
for c in range(0, quantidade):
    jogos.append(list())
    total = 0
    while True:
        numero = randint(1, 60)
        if numero not in jogos[c]:
            jogos[c].append(numero)
            total += 1
        if total == 6:
            break
    jogos[c].sort()
    print(f'Jogo {c+1}: {jogos[c]}')
    sleep(1)

'''for p, c in enumerate(jogos):
    print(f'Jogo {p+1}: {c}')
    sleep(1)
print('-'*20)
'''
