from math import hypot
print('=========Desafio 017========')
catetoOposto = float(input('Cateto oposto: '))
catetoAdjacente = float(input('Cateto adjacente: '))
hipotenusa = hypot(catetoOposto, catetoAdjacente)
print('Hipotenusa de {} e {} é {:.2f}'.format(catetoOposto, catetoAdjacente, hipotenusa))
'''
OU
hipotenusa = catetoOposto**2 + catetoAdjacente**2
hipotenusa = hipotenusa**(1/2)
print('Hipotenusa de {} e {} é {:.2f}'.format(catetoOposto, catetoAdjacente, hipotenusa))
'''