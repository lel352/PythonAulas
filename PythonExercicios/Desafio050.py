print('=========Desafio 050========')
soma = 0
for c in range(1, 7):
    numero = int(input('Numero {}: '.format(c)))
    if numero % 2 == 0:
        soma += numero
print('Soma de todos os numeros pares é {}'.format(soma))
