from datetime import date
print('=========Desafio 041========')
anoNascimento = int(input('Ano de Nascimento: '))
anoAtual = date.today().year
idade = anoAtual - anoNascimento
print('Idade {} anos.'.format(idade))
if idade <= 9:
    print('Categoria: Mirin ')
elif idade <= 14:
    print('Categoria: Infantil ')
elif idade <= 19:
    print('Categoria: Junior ')
elif idade <= 25:
    print('Categoria: Senior ')
else:
    print('Categoria: Master ')
