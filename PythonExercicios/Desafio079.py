print('=========Desafio 079========')
valores = list()
while True:
    valor = int(input(f'Digite um valor: '))
    if valor not in valores:
        valores.append(valor)
    else:
        print(f'{valor} ja foi adicionado')
    reposta = str(input('Deseja Continuar? [S/N]')).strip().upper()[0]
    while reposta not in 'SN':
        reposta = str(input('Resposta invlida! Deseja Continuar? [S/N]')).strip().upper()[0]
    if reposta in 'N':
        break
valores.sort()
print(f'Ordem {valores}')
