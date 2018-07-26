print('=========Desafio 082========')
valores = list()
par = list()
impar = list()
while True:
    valores.append(int(input(f'Digite um valor: ')))
    reposta = str(input('Deseja Continuar? [S/N]')).strip().upper()[0]
    while reposta not in 'SN':
        reposta = str(input('Resposta invlida! Deseja Continuar? [S/N]')).strip().upper()[0]
    if reposta in 'N':
        break
#foi pedido assim
for v in valores:
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print(f'Valores: {valores}')
print(f'Par: {par}')
print(f'Impar: {impar}')
