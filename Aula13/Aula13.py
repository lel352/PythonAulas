#estruturas de repetições
# Estrutura For
for c in range(0, 6):# 0 até 6
    print('Oi')
print('Fim')
for c in range(1, 7):# 1 até 6
    print(c)
print('Fim')
for c in range(6, 0, -1):# 6 até 1 , tira -1 a cada interação: 6,5,4,3,2,1
    print(c)
print('Fim')
for c in range(0, 7, 2):# 0 até 6, contando de 2 em 2: 0,2,4,6
    print(c)
print('Fim')

n = int(input('Digite um numero: '))
for c in range(0, n+1):
    print(c)
print('Fim')

inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
for c in range(inicio, fim+1, passo):
    print(c)
print('Fim')

s = 0
for c in range(0, 3):
    n = int(input('Digite o valor:'))
    s += n
print('Somatorio {}'.format(s))
print('Fim')
