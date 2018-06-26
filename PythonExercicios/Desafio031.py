print('=========Desafio 031========')
distancia = int(input('Distancia em KM: '))
'''
if distancia > 200:
    valor = distancia * 0.45
else:
    valor = distancia * 0.50
'''
valor = distancia * 0.45 if distancia > 200 else distancia * 0.50
print('Valor da passagem é {:.2f}'.format(valor))
