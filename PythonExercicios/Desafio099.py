from random import randint
from time import sleep
print('=========Desafio 099========')

def maior(*valores):
    print('--Analisando--')
    if len(valores) <= 0:
        print(f'Nenhum valor informado ')
    else:
        maiorValor = max(valores)
        for valor in valores:
            print(f'{valor}', end=' ', flush=True)
            sleep(0.3)
           # if maiorValor < valor:
            #    maiorValor = valor
        print(f'. Foram informados {len(valores)} ao todo')
        print(f'Maior valor é {maiorValor}')
    print('--------------')


maior(randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
maior(randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
maior(randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
maior(randint(1, 10), randint(1, 10), randint(1, 10))
maior()
