print('=========Desafio 064========')
numero = 0
quantidade = -1
soma = -999
while numero != 999:
    numero = int(input('Numero[999 para parar]: '))
    soma += numero
    quantidade += 1
print('Quantidade de Numero: {}'.format(quantidade))
print('Soma dos Numero: {}'.format(soma))

#ou

numero = quantidade = soma = 0
numero = int(input('Numero[999 para parar]: '))
while numero != 999:
    soma += numero
    quantidade += 1
    numero = int(input('Numero[999 para parar]: '))
print('Quantidade de Numero: {}'.format(quantidade))
print('Soma dos Numero: {}'.format(soma))


