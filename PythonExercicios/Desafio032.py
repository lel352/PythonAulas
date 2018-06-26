from _datetime import date
print('=========Desafio 032========')
ano = int(input('Digite um Ano(Coloque 0 para o ano atual): '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Ano {} é bissexto '.format(ano))
else:
    print('Ano {} não é bissexto '.format(ano))
