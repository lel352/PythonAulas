from math import factorial
print('=========Desafio 060========')
numero = int(input('Digite um numero: '))
fatorial = numero
print('{0} != {0}'.format(numero), end='')
while numero - 1 != 0:
    numero += -1
    fatorial = fatorial * numero
    print(' x {}'.format(numero), end='')
print(' = {}'.format(fatorial))
#ou
numero = int(input('Digite um numero: '))
fatorial = factorial(numero)
print('{} != {}'.format(numero, fatorial))
