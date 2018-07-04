print('=========Desafio 049========')
numero = int(input('Digite um Numero: '))
print('{:=^20}'.format('Tabuada'))
for c in range(0, 11):
    print('{} x  {} = {}'.format(numero, c, numero * c))
