print('=========Desafio 038========')
numero1 = int(input('Numero 1: '))
numero2 = int(input('Numero 2: '))
if numero1 > numero2:
    print('Primeiro valor {} é maior'.format(numero1))
elif numero1 < numero2:
    print('Segundo valor {} é maior'.format(numero2))
else:
    print('Não existe valor maior, os dois são iguais')
