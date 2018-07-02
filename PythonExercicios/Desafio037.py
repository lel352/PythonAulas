print('=========Desafio 037========')
print('=' * 20)
print('{:^20}'.format('Base de conversão'))
print('=' * 20)
print('''1 - Para Base Binária
2 - Para Base Octal
3 - Para Base Hexadecimal''')
print('=' * 20)
opcao = int(input('Digite uma Opção: '))
if str(opcao) not in '1 2 3':
    print('Opção inválida!')
    exit(0)
numero = int(input('Numero para conversão: '))
if opcao == 1:
    print('Numero {} para Binario {}'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('Numero {} para Octal {}'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('Numero {} para Hexadecimal {}'.format(numero, hex(numero)[2:]))
