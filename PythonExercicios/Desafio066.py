print('=========Desafio 066========')
numero = soma = contador = 0
while True:
    numero = int(input('Digite um numero[999 para sair]: '))
    if numero == 999:
        break
    soma += numero
    contador += 1
print(f'A soma dos {contador} valores é {soma}')
