print('=========Desafio 055========')
maior = menor = 0
for c in range(1, 6):
    peso = float(input('Peso {}: '.format(c)))
    if c == 1:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

print('Maior Peso {}Kg'.format(maior))
print('Menor Peso {}Kg'.format(menor))
