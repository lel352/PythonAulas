print('=========Desafio 048========')
soma = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        soma += c
print('Soma total {}'.format(soma))
'''
ou
soma = 0
for c in range(1, 500, 2):
    if c % 2 == 1 and c % 3 == 0:
        soma += c;
print('Soma total {}'.format(soma))
'''
