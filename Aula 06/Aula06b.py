numero = float(input("Digite um valor: "))
print(numero) #float

numero = str(input("Digite um valor: "))
print(numero) #string

numero = bool(input("Digite um valor: "))
print(numero) #boolean

numero = input("Digite algo: ")
print(numero) #String
#métodos para teste de tipos
print('Somente numeros: {}'.format(numero.isnumeric()))# Esse metodo diz se o valor dentro da variavel é um valor numerico (só numero)
print('Somente Letras: {}'.format(numero.isalpha()))# Esse metodo diz se o valor dentro da variavel é letra(só letra)
print('Alfanumero(letras e numero): {}'.format(numero.isalnum()))# Esse metodo diz se o valor dentro da variavel é alfanumerico (se tem letra e numero)
print('Tudo upper: {}'.format(numero.isupper()))# Esse metodo diz se o valor dentro da variavel esta somente com letras maiusculas
print('Tudo lower: {}'.format(numero.islower()))# Esse metodo diz se o valor dentro da variavel esta somente com letras minusculas


