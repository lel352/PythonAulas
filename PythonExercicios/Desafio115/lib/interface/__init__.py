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

def linha(tamanho=42):
    return '-' * tamanho


def cabecalho(texto):
    print(linha())
    print(texto.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    contador = 1
    for item in lista:
        print(f'\033[33m{contador}\033[m - \033[34m{item}\033[m')
        contador += 1
    print(linha())
    return leiaInt('\033[32mSua Opção:\033[m')

