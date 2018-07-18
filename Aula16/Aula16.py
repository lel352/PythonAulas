#Variaveis composta
#Tuplas
#Tuplas são Imutaveis
# () = tupla

print('--Forma de fatiar dados com tuplas--')
lanche = ('Hmabúrger', 'Suco', 'Pizza', 'Pudim') # or lanche = 'Hmabúrger', 'Suco', 'Pizza', 'Pudim'
print('lanche:', lanche)
print('lanche[-3]:', lanche[-3]) #suco
print('lanche[3]:', lanche[3]) #pudim
print('lanche[1:3]:', lanche[1:3]) #'Suco', 'Pizza',
print('lanche[2:]:', lanche[2:]) #'Pizza', 'Pudim'
print('lanche[:2]:', lanche[:2]) #'Hmabúrger', 'Suco',
print('lanche[-2:]:', lanche[-2:]) #'Pizza', 'Pudim'
print('lanche[-3:]:', lanche[-3:]) #'Suco', 'Pizza', 'Pudim'

#Tuplas são Imutaveis
'''
print('lanche[1]:', lanche[1]) #suco
lanche[1] = 'Refrigerante'
Não permiete atribuir valores a tupla
são imutaveis
erro: TypeError: 'tuple' object does not support item assignment
'''
# forma para mostrar os dados
print('--Forma para mostrar os dados--')
print(f'\nlanche: {lanche}',)

print('Quantidade: ', len(lanche))
lanche = ('Hmabúrger', 'Suco', 'Pizza', 'Pudim','Batata-Frita')
print('Quantidade: ', len(lanche))

print('\nlanche (comida in lanche):')
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Satisfeito')

print('\nlanche (contador in range(0, len(lanche)):')
for contador in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[contador]} posicao {contador}')
print('Satisfeito')

print('\nlanche (posicao, comida in enumerate(lanche)):')
for posicao, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} e posicao {posicao}')
print('Satisfeito')

print(f'Mostrando o lanche em orderm (sorted) {sorted(lanche)}')

print('Fim da brincadeira com o lanche')

a = (2, 5, 4)
b = (5, 8, 1, 2)
print(f'a = {a}')
print(f'b = {b}')
c = a + b
print(f'c = a + b = {c}')
d = b + a
print(f'd = b + a = {d}')
print(f'Len(c): {len(c)}')
print(f'c.count(5) - quantas vezes a parece o numero 5 na tupla: {c.count(5)} vezes')
print(f'c.count(4) - quantas vezes a parece o numero 4 na tupla: {c.count(4)} vezes')
print(f'c.count(9) - quantas vezes a parece o numero 9 na tupla: {c.count(9)} vezes')

print(f'd.index(8) - Em que posicão está o 8 na tupla: {d.index(8)}')
print(f'd.index(4) - Em que posicão está o 4 na tupla: {d.index(4)}')
print(f'd.index(2) - Em que posicão está o 2 na tupla: {d.index(2)}')
print(f'd.index(5) - Em que posicão está o 5 na tupla: {d.index(5)}')
print(f'd.index(5, 1) - Em que posicão está o 5 vendo da posicao 1(ignora a posicao 0) em diante e na tupla: {c.index(2, 1)}')
print('Fim da brincadeira com o numero')

print('Tupla pode ter dados de tipos diferente dentro dela')
pessoa = ('Gustavo', 39, 'M', 99.88)
print(pessoa)

del(pessoa)# apaga da memória
