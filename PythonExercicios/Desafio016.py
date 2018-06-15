from math import trunc
print('=========Desafio 016========')
numero = float(input('Digite um numero: '))
print('Parte inteira de {} é {}'.format(numero, trunc(numero)))
#print('Parte inteira de {} é {}'.format(numero, int(numero)))
#print('Parte inteira de {} é {}'.format(numero, (numero - numero % 1)))