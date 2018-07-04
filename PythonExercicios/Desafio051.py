print('=========Desafio 051========')
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
soma = termo + 10 * razao
for c in range(termo, soma, razao):
    print(c, end=' -> ')
print('FIM')
#ou
decimo = termo + (10-1) * razao
for c in range(termo, decimo + razao, razao):
    print(c, end=' -> ')
print('FIM')
#ou
soma = termo
print(soma, end=' -> ')
for c in range(1, 10):
    soma += razao
    print(soma, end=' -> ')
print('FIM')


