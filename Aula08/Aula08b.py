'''
importa de math so o que deseja ai não precisa usar
math."a função que deseja usar" como no import total da biblioteca
'''
from math import sqrt, ceil, floor
numero = int(input('Digite um numero: '))
raiz = sqrt(numero) #raiz quadrada
#raiz3 = math.sqrt(numero, 3) #raiz Cubica
print('A raiz de um {} é igual {}'.format(numero, raiz))
print('A raiz de um {} é igual {:.3f}'.format(numero, raiz))
#math.ceil arredonda para cima
print('A raiz de um {} é igual (arredondando para cima) {}'.format(numero, ceil(raiz)))
#math.floor arredonda para baixo
print('A raiz de um {} é igual (arredondando para baixo) {}'.format(numero, floor(raiz)))
#print('A raiz cubica de um {} é igual {}'.format(numero, raiz3))