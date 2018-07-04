from datetime import date
print('=========Desafio 054========')
atual = date.today().year
maior = menor = 0
for c in range(1, 8):
    ano = int(input('{}º Ano de nascimento: '.format(c)))
    idade = atual - ano
    if idade < 21:
        menor += 1
    else:
        maior += 1
print('Quantidade de maiores de idade: {}'.format(maior))
print('Quantidade de menores de idade: {}'.format(menor))
