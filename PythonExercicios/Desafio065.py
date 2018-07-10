print('=========Desafio 065========')
numero = quantidade = soma = 0
res = 'S'
while res in 'Ss':
    numero = int(input('Numero: '))
    if quantidade == 0:
       maior = menor = numero
    elif maior < numero:
        maior = numero
    elif menor > numero:
        menor = numero
    soma += numero
    quantidade += 1
    res = str(input('Deseja continuar? [S/N]')).strip().upper()[0] # só a primera letra
    while res not in 'SN':
        print('Opção Inválida, digite novamente! ')
        res = str(input('Deseja continuar? [S/N]')).strip().upper()[0] # só a primera letra
media = soma / quantidade
print('Quantidade de Numeros: {}'.format(quantidade))
print('Soma dos Numero: {}'.format(soma))
print('Media dos Numero: {:.2f}'.format(media))
print('Maior  Numero: {}'.format(maior))
print('Menor  Numero: {}'.format(menor))
