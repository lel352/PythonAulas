print('=========Desafio 023========')
#forma de se fazer numerica
numero = int(input('Digite um Numero: '))
milhar = numero // 1000
resto = numero % 1000
centena = resto // 100
resto = resto % 100
dezena = resto // 10
unidade = resto % 10
print('Forma numerica')
print('Milhar: {}'.format(milhar))
print('Centena: {}'.format(centena))
print('Dezena: {}'.format(dezena))
print('Unidade: {}'.format(unidade))


'''
milhar = numero // 1000 % 10
centena = numero // 100 % 10
dezena = numero // 10 % 10
unidade = numero // 1 % 10
print('Forma numerica')
print('Milhar: {}'.format(milhar))
print('Centena: {}'.format(centena))
print('Dezena: {}'.format(dezena))
print('Unidade: {}'.format(unidade))
'''

print('\n\nForma String')
numero2 = str(numero)[::-1]+'0000'
print('Milhar: {}'.format(numero2[3]))
print('Centena: {}'.format(numero2[2]))
print('Dezena: {}'.format(numero2[1]))
print('Unidade: {}'.format(numero2[0]))


print('\n\nForma String')
numero3 = str(numero).zfill(4)
print('Milhar: {}'.format(numero3[0]))
print('Centena: {}'.format(numero3[1]))
print('Dezena: {}'.format(numero3[2]))
print('Unidade: {}'.format(numero3[3]))


