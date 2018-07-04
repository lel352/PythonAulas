print('=========Desafio 053========')
frase = str(input('Frase: '))
frase2 = frase.split()
frase2 = ''.join(frase2)
frase3 = frase2[::-1]
if frase3 == frase2:
    print('{} \nA frase é um palindromo'.format(frase))
else:
    print('{} \nA frase não é um palindromo'.format(frase))
print('{} ao contrario {}'.format(frase2, frase3))

#ou
frase2 = frase.split()
frase2 = ''.join(frase2)
frase3 = ''
for c in frase2[::-1]:
    frase3 += c
if frase3 == frase2:
    print('{} \nA frase é um palindromo'.format(frase))
else:
    print('{} \nA frase não é um palindromo'.format(frase))
print('{} ao contrario {}'.format(frase2, frase3))

