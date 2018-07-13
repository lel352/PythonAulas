print('=========Desafio 067========')
numero = 0
while True:
    numero = int(input('Qual tabuada quer ver? [negativo para sair] '))
    if numero < 0:
        break
    print('='*20)
    print(f'Tabuada de {numero}')
    for i in range(0, 11):
        print(f'{numero} x {i} = {numero * i}')
    print('=' * 20)
print('Fim')
