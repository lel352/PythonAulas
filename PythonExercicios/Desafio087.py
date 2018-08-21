print('=========Desafio 087========')
matriz = list()
matriz.append(list())
matriz.append(list())
matriz.append(list())
for l in range(0, 3):
    for c in range(0, 3):
        valor = int(input(f'Posição [{l}, {c}]: '))
        matriz[l].append(valor)
somaPar = 0
somaColuna = 0
print('Matriz:')
for p, l in enumerate(matriz):
    if p == 1:
        maior = max(l)
    for p2, c in enumerate(l):
        print(f'[{c:^3}]', end='') #print(f'[ {c} ]', end='')
        if c % 2 == 0:
            somaPar += c
        if p2 == 2:
            somaColuna += c
    print()
print('-'*20)
print(f'A soma dos valores pares é {somaPar}')
print(f'A Soma dos valores da terceira Coluna é {somaColuna}')
print(f'O Maior valor da segunda linha é {maior}')
