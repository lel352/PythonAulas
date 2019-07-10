print('=========Desafio 104========')
def leiaInt(mensagem):
    numero = str(input(mensagem)).strip()
    while not numero.isnumeric():
        print('\033[0;31mErro! Digite um numero Inteiro válido! \033[m')
        numero = str(input(mensagem)).strip()
    return numero


numero = leiaInt('Digite um número: ')
print(f'Você digitou {numero}')
