print('=========Desafio 075========')
numeros = tuple(int(input(f'Numero {i+1}: ')) for i in range(4))
#ou
'''numeros = (int(input('Numero 1: ')), int(input('Numero 2: ')),
           int(input('Numero 3: ')), int(input('Numero 4: ')))'''
print(f'numero 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'numero 3 apareceu na {numeros.index(3) + 1} posição')
else:
    print(f'numero 3 não foi digitado')
print('Numeros pares digitados: ', end='')
for c in numeros:
    if c % 2 == 0:
        print(c, end=' ')

