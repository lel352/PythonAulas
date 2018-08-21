print('=========Desafio 085========')
numeros = list()
numeros.append(list())
numeros.append(list())
'''
ou
numeros = [[], []]
'''
for c in range(1, 8):
    valor = int(input(f'Valor {c}: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
numeros[0].sort()
numeros[1].sort()
print(f'Os valores pares: {numeros[0]}')
print(f'Os valores impares: {numeros[1]}')
