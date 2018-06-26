print('=========Desafio 034========')
salario = float(input('Salario R$: '))
aumento = 15
if salario > 1250:
    aumento = 10
valor = (salario * aumento) / 100
print('Aumento será de R$ {:.2f} '.format(valor))
print('Salario é de R$ {:.2f} '.format(valor+salario))

