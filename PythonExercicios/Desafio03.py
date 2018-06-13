print('=========Desafio 03========')
print('Somar Nuemros')
'''
 python 2 
 'eval' faz usar o 'input' da versão antiga
 que na verdade so retorna valores inteiros,
 python 3 o 'input' so retorna string; 
'''
numero1 = eval(input('Numero 1: '))
numero2 = eval(input('Numero 2: '))
soma = numero1 + numero2
print('Soma de', numero1, '+', numero2, 'é', soma)

numero3 = input('Numero 1: ')
numero4 = input('Numero 2: ')
'''
 python 3 o 'input' so retorna uma string
 precisa converter o valor de string para inteiro
 por isso o uso do 'int'
'''
soma = int(numero3) + int(numero4)
print('Soma de', numero3, '+', numero4, 'é', soma)
