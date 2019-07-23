print('=========Desafio 107========')
import moeda

valor = float(input("Digite um valor: R$ "))
print(f'A Metadade de {valor} é R${moeda.metade(valor)}')
print(f'A dobro de {valor} é R${moeda.dobro(valor)}')
print(f'Aumentando 10% em {valor} é R${moeda.aumentar(valor, 10)}')
print(f'Reduzindo 13% em {valor} é R${moeda.diminuir(valor, 13)}')

