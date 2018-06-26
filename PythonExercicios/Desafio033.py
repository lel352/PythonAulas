print('=========Desafio 033========')
numero1 = int(input('Numero 1: '))
numero2 = int(input('Numero 2: '))
numero3 = int(input('Numero 3: '))
maior = numero1
menor = numero1
if maior < numero2 and maior > numero3:
    maior = numero2
elif maior < numero3:
    maior = numero3
if menor > numero2 and menor < numero3:
    menor = numero2
elif menor > numero3:
    menor = numero3
print('Maior Numero: {} \nmenor numero {}'.format(maior, menor))
