#imput retorna string (str)
numero1 = input('Digite um valor: ')
print(type(numero1))

#tranformando um valor string (str) em inteiro (int)
numero2 = int(input('Digite um valor: '))
print(type(numero2))

numero1 = int(input('Digite um valor: '))
numero2 = int(input('Digite outro valor: '))
soma = numero1 + numero2
print(' A soma vale', soma)
print(' A soma entre', numero1, 'e', numero2, 'vale', soma)
print(' A soma entre {} e {} vale {}'.format(numero1, numero2, soma))
