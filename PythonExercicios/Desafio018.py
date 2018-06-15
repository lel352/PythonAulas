from math import sin, cos, tan, radians
print('=========Desafio 018========')
angulo = float(input('Informe o angulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('Seno: {:.2f} \ncosseno: {:.2f} \ntangente: {:.2f}'.format(seno, cosseno, tangente))
