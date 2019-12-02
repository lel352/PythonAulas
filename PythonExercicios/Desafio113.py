print('=========Desafio 113========')
def leiaInt(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
        except (ValueError, TypeError):  # Exception especifica
            print('\033[31mErro! Digite um numero Inteiro válido! \033[m')
        except (KeyboardInterrupt):
            print('\033[31m Usuário preferiu não digitar esse número! \033[m')
            return 0
        else:
            return numero
    '''
    Do Desafio 104
    numero = str(input(mensagem)).strip()
    while not numero.isnumeric():
        print('\033[0;31mErro! Digite um numero Inteiro válido! \033[m')
        numero = str(input(mensagem)).strip()
    return numero
    '''


def leiaReal(mensagem):
    while True:
        try:
            numero = float(input(mensagem))
        except (ValueError, TypeError):  # Exception especifica
            print('\033[0;31mErro! Digite um numero Real válido! \033[m')
        except KeyboardInterrupt:
            print('\033[0;31m Usuário preferiu não digitar esse número! \033[m')
            return 0
        else:
            return numero


inteiro = leiaInt('Digite um número Inteiro: ')
#print(f'Você digitou {numero}\n')
print()
real = leiaReal('Digite um número Real: ')
print(f'Numero Inteiro: {inteiro}, numero real: {real}')
