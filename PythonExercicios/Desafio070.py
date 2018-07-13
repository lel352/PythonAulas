print('=========Desafio 070========')
totalCompra = preco1000 = precoBarato = 0
nomeBarato = ''
while True:
    print('-' * 20)
    print(' Cadastro de Produto')
    print('-' * 20)
    nome = str(input('Nome: ')).strip()
    preco = float(input('Preço R$ '))
    if totalCompra == 0:
        precoBarato = preco
        nomeBarato = nome
    elif preco < precoBarato:
        precoBarato = preco
        nomeBarato = nome
    if preco > 1000:
        preco1000 += 1
    totalCompra += preco
    resposta = str(input('Deseja Continuar? S/N: ')).strip().upper()[0]
    while resposta not in 'SN':
        resposta = str(input('Opção inválido, digite novamente! Deseja Continuar? S/N: ')).strip().upper()[0]
    if resposta in 'N':
        break
print('='*20)
print(f'Total da compra foi de R$ {totalCompra:.2f}.')
print(f'Total de produtos que custa  mais de R$ 1000.00 é {preco1000}.')
print(f'Como preco de R$ {precoBarato:.2f} o {nomeBarato} é o produto mais barato.')
print('='*20)