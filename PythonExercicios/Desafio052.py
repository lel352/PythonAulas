print('=========Desafio 052========')
numero = int(input('Numero: '))
primo = True
for c in range(numero-1, 1, -1):
    if numero % c == 0:
        primo = False;
        break
if primo:
    print('{} é um numero Primo'.format(numero))
else:
    print('{} não é um numero Primo'.format(numero))


