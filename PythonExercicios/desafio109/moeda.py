# modulo moeda

def valorPorcentagem(valor, porcento):
    return ((valor * porcento) / 100)


def aumentar(valor, porcento, formata=True):
    if formata:
        return moeda(valor + valorPorcentagem(valor, porcento))
    else:
        return valor + valorPorcentagem(valor, porcento)


def diminuir(valor, porcento, formata=True):
    if formata:
        return moeda(valor - valorPorcentagem(valor, porcento))
    else:
        return valor - valorPorcentagem(valor, porcento)


def dobro(valor, formata=True):
    if formata:
        return moeda(valor * 2)
    else:
        return valor * 2


def metade(valor, formata=True):
    if formata:
        return moeda(valor / 2)
    else:
        return valor / 2


def moeda(valor=0, moeda='RS'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')

