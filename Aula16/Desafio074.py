from random import randint
print('=========Desafio 074========')
numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Numeros sorteados foram: {numeros}')
maior = max(numeros)
menor = min(numeros)
print(f'O maior valor sorteado: {maior}')
print(f'O menor valor sorteado: {menor}')
