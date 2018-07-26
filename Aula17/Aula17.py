'''
Lista é mutavel e usa colchetes
'''
valores = [2, 5, 9, 1]
print(f'Lista: {valores}')
valores[2] = 3
#valores[4] = 3 da erro acessando um indece inválido
print(f'Lista: {valores}')
#append adiciona valores
valores.append(4)
print(f'Lista: {valores}')
valores.sort()
print(f'Sort: Lista: {valores}')
valores.sort(reverse=True)
print(f'Sort reverse = True: Lista: {valores}')
print(f'Essa lista tem {len(valores)} elementos. ')
#inserindo o valor '0' na posição 2
valores.insert(2, 0)
print(f'valores.insert(2, 0) Lista: {valores}')
#remove o valor na ultima posição
valores.pop()
print(f'Remove: valores.pop() Lista: {valores}')
#remove o valor na posição 2
valores.pop(2)
print(f'Remove na posição: valores.pop(2) Lista: {valores}')
print(f'Lista: {valores}')
valores.insert(2, 2)
print(f'valores.insert(2, 2) Lista: {valores}')
#remove o valor 2, na primeira aparição
#procurando do inicio da lista
valores.remove(2)
print(f'valores.remove(2) Lista: {valores}')
#valores.remove(9) da erro pois o valor 9 não existe na lista
#Antes precisa ver se ele existe
if 9 in valores:
    valores.remove(9)
    print(f'valores.remove(9) Lista: {valores}')
else:
    print(f'Valor 9 não se encontra na lista: {valores}')
if 5 in valores:
    valores.remove(5)
    print(f'valores.remove(5) Lista: {valores}')
else:
    print(f'Valor 5 não se encontra na lista: {valores}')

print('='*20)
print('Novo Exemplo')
#lista vazia
valores = []
#ou
valores = list()
valores.append(5)
valores.append(9)
valores.append(4)
print(f'Usando Append: Valores {valores}')

for valor in valores:
    print(f'{valor}...', end='')

print('\n')
for indice, valor in enumerate(valores):
    print(f'Na posição {indice} encontrei o valor {valor}!')
print('Cheguei ao final da lista.')

print('\nDigite os valores')
valores = list()
for contador in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print('\n')
for indice, valor in enumerate(valores):
    print(f'Na posição {indice} encontrei o valor {valor}!')
print('Cheguei ao final da lista.')
print('\n')
print('='*20)
a = [2, 3, 4, 7]
b = a #cria ligação entre lsita
print(f'Lista A: {a}')
print(f'Lista B: {b}')
b[2] = 8 #O que mexi numa mexe na outra
print(f'Lista A: {a}')
print(f'Lista B: {b}')
b = a[:] #uma copia sem ligação
b[2] = 4
print(f'Lista A: {a}')
print(f'Lista B: {b}')
