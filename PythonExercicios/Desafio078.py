print('=========Desafio 078========')
valores = list()
for c in range(0, 5):
    valores.append(int(input(f'Digite o valor Posicao {c}: ')))
print(f'valores digitados: {valores}')
maior = max(valores)
menor = min(valores)
print(f'O Maior valor é {maior} nas posições ', end='')
for p, v in enumerate(valores):
    if maior == v:
        print(f'{p}..', end='')
print(f'\nO Menor valor é {menor} nas posições ', end='')
for p, v in enumerate(valores):
    if menor == v:
        print(f'{p}..', end='')
