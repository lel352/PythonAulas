# modulo moeda

def valorPorcentagem(valor, porcento):
    return ((valor * porcento) / 100)


def aumentar(valor, porcento):
    return valor + valorPorcentagem(valor, porcento)


def diminuir(valor, porcento):
    return valor - valorPorcentagem(valor, porcento)


def dobro(valor):
    return valor * 2


def metade(valor):
    return valor / 2


def moeda(valor=0, moeda='RS'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')
