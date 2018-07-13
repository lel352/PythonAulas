contador = 1
while contador <= 10:
    print(contador, '->', end='')
    contador += 1
print('Acabou')

contador = 0
while True:
    print(contador, '->', end='')
    contador += 1
    if contador == 10:
        break
print('Acabou')

numero = soma = 0
while True:
    numero = int(input('Digite um numero: '))
    if numero == 999:
        break
    soma += numero

print('Soma é {}'.format(soma))
