print('=========Desafio 071========')
print('{:^40}'.format('Banco'))
print('-'*40)
valor = int(input('Digite o valor que deseja sacar R$ '))
nota1 = nota10 = nota20 = nota50 = 0
while True:
     if valor // 50 > 0:
        nota50 = valor // 50
        valor = valor % 50
     elif valor // 20 > 0:
         nota20 = valor // 20
         valor = valor % 20
     elif valor // 10 > 0:
         nota10 = valor // 10
         valor = valor % 10
     else:
         nota1 = valor // 1
         valor = 0
     if valor == 0:
         break
print('-'*40)
if nota50 > 0:
    print(f'Total de {nota50} cédulas de R$50')
if nota20 > 0:
    print(f'Total de {nota20} cédulas de R$20')
if nota10 > 0:
    print(f'Total de {nota10} cédulas de R$10')
if nota1 > 0:
    print(f'Total de {nota1} cédulas de R$20')
print('-'*40)
