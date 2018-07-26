print('=========Desafio 081========')
valores = list()
while True:
    valores.append(int(input(f'Digite um valor: ')))
    reposta = str(input('Deseja Continuar? [S/N]')).strip().upper()[0]
    while reposta not in 'SN':
        reposta = str(input('Resposta invlida! Deseja Continuar? [S/N]')).strip().upper()[0]
    if reposta in 'N':
        break
print(f'Total de elemetos: {len(valores)}')
valores.sort(reverse=True)
print(f'Ordem descrescente: {valores}')
if 5 in valores:
    print('O valor 5 está na lista!')
    print(f'Apareceu {valores.count(5)} vezes.')
else:
    print('O valor 5 não está na lista!')
