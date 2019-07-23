print('=========Desafio 108========')
import moeda

valor = float(input("Digite um valor: R$ "))
print(f'A Metadade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}')
print(f'A dobro de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))}')
print(f'Aumentando 10% em {moeda.moeda(valor)} é {moeda.moeda(moeda.aumentar(valor, 10))}')
print(f'Reduzindo 13% em {moeda.moeda(valor)} é {moeda.moeda(moeda.diminuir(valor, 13))}')

