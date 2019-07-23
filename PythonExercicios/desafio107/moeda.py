# modulo moeda
def valorPorcentagem(valor, taxa):
    return (valor * taxa) / 100


def aumentar(valor, taxa):
    return valor + valorPorcentagem(valor, taxa)


def diminuir(valor, taxa):
    return valor - valorPorcentagem(valor, taxa)


def dobro(valor):
    return valor * 2


def metade(valor):
    return valor / 2

