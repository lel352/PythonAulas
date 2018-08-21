print('=========Desafio 086========')
matriz = list() #ou  matriz = [[],[],[]]
matriz.append(list())
matriz.append(list())
matriz.append(list())
for l in range(0, 3):
    for c in range(0, 3):
        valor = int(input(f'Posição [{l}, {c}]: '))
        matriz[l].append(valor)
print('Matriz:')
for l in matriz:
    for c in l:
        print(f'[{c:^5}]', end='')
    print()
'''ou
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for x in range(0, 3):
    for c in range(0, 3):
        matriz[x][c] = int(input(f'Digite um valor para [{x}, {c}]: '))
print('-='*20)
for x in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[x][c]:^5}]', end='')
    print()
print()
print('-='*20)
'''

