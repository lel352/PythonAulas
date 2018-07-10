print('=========Desafio 063========')
numero = int(input('Quantos termos deseja ver? '))
c = 1
proximo = 0
anterior = 1
meio = 0
print(proximo, end='')
while c != numero:
    meio = proximo
    proximo = anterior + meio
    anterior = meio
    print('-> {}'.format(proximo), end='')
    c += 1
print('\nFim\n')
#ou
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('{} → {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' → {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' → FIM')
