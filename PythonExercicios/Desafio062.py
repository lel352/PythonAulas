print('=========Desafio 062========')
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
c = 0
soma = termo
quatidadeTermos = 10
quatidadeTotal = 10
while quatidadeTermos != 0:
    while c != quatidadeTermos:
        print(soma, end=' -> ')
        soma += razao
        c += 1
    print('Pausa')
    quatidadeTermos = int(input('Deseja ver mais quantos termos: '))
    if quatidadeTermos > 0:
        quatidadeTotal += quatidadeTermos
        c = 0
print('FIM')
print('Foram mostra {} termos'.format(quatidadeTotal))
