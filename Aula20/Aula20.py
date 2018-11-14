from builtins import print
from distutils.command.config import config


def linha():
    print('*' * 20)


linha()
print('Teste')
linha()

def mensagem(msg):
    linha()
    print(msg)
    linha()


mensagem('Alunos')
mensagem('Sistemas')

def soma(a, b):
    s = a + b
    print(f'{a} + {b} = {s}')


soma(4, 5)
soma(8, 9)
soma(2, 1)
soma(a=2, b=1)
soma(b=2, a=1)

#*antes permite ele passar vario informação no paramentro
def contador(*numero):
    print(numero) #é uma tupla
    for valor in numero:
        print(f'{valor} ', end='')
    print(f'Fim tamanho = {len(numero)}')


contador(2, 3, 7)
contador(2, 0)
contador(4, 5, 9, 6, 2)

print('')

def soma(* valores):
    s = 0;
    for valor in valores:
        s += valor
    print(f'soma é {s}')


soma(5, 2)
soma(2, 9 ,5, 2)

print('')
#passagem de paramentros é por referência
#diferente de outras que é por valor
def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)
