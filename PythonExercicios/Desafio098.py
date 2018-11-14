from time import sleep
print('=========Desafio 098========')
def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    p2 = passo
    print(f'Contagem de {inicio} até {fim} de {p2}:')
    if inicio > fim:
        fim -= 1
        if passo > 0:
            passo *= -1
    else:
        if passo < 0:
            passo *= -1
        fim += 1

    for valor in range(inicio, fim, passo):
        print(f'{valor}', end=' ', flush=True)
        sleep(0.1)
    print(' - fim')

inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('passo: '))

contador(1, 10, 1)
contador(10, 0, -1)
contador(inicio, fim, passo)
