# modulo moeda
from enum import auto


def valorPorcentagem(valor, porcento):
    return ((valor * porcento) / 100)


def aumentar(valor, porcento, formata=True):
    resultado = valor + valorPorcentagem(valor, porcento)
    return resultado if formata is False else moeda(resultado)


def diminuir(valor, porcento, formata=True):
    resultado = valor - valorPorcentagem(valor, porcento)
    return resultado if formata is False else moeda(resultado)


def dobro(valor, formata=True):
    return valor * 2 if formata is False else moeda(valor * 2)


def metade(valor, formata = True):
    return valor / 2 if formata is False else moeda(valor / 2)


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:>.2f}'.replace('.', ',')


def resumo(valor=0, aumenta=0, diminui=0):
    print('-' * 30)
    print('Resumo do Valor'.center(30))
    print('-' * 30)
    print(f'Preço Analisado: \t{moeda(valor)}')
    print(f'Dobro do Preço: \t{dobro(valor)}')
    print(f'Metade do Preço: \t{metade(valor)}')
    print(f'{aumenta}% do Preço: \t\t{aumentar(valor, aumenta)}')
    print(f'{diminui}% do Preço: \t\t{diminuir(valor, diminui)}')
    print('-' * 40)

