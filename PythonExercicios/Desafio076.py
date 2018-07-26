print('=========Desafio 075========')
produtos = ('Pão', 2.50, 'Lapis', 1.20, 'Caneta', 2.00, 'Livro', 50)

print('-'*50)
print('{:^50}'.format('Listagem de Preços'))
print('-'*50)
for posicao in range(0, len(produtos), 2):
    print(f'{produtos[posicao]:.<40}R${produtos[posicao+1]:>8.2f}')
'''
for posicao, dados in enumerate(produtos):
    if posicao % 2 == 0:
        print(f'{dados:.<40}', end='');
    else:
        print(f'R${dados:>8.2f}');
'''
print('-'*50)
