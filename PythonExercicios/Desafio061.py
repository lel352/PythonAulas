print('=========Desafio 061========')
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
c = 0
soma = termo
while c != 10:
    print(soma, end=' -> ')
    soma += razao
    c += 1
print('FIM')
