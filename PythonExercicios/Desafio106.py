print('=========Desafio 106========')

cores = ('\033[m',         # 0-Sem cores
         '\033[0;30;41m',  # 1-Vermelho
         '\033[0;30;42m',  # 2-Verde
         '\033[0;30;43m',  # 3-Amarelo
         '\033[0;30;44m',  # 4-Azul
         '\033[0;30;45m',  # 5-Roxo
         '\033[7;30m'      # 6-Branco
         )

def escreva(mensagem, cor=0, quadros=True):
    print(cores[cor], end='')
    if quadros:
        tamanho = len(mensagem) + 4
        print('=' * tamanho)
        print(f'  {mensagem}')
        print('=' * tamanho)
    else:
        print(f'{mensagem}')
    print(cores[0], end='')


def pegaDadoUsuario(mensagem):
    comando = str(input(mensagem)).strip()
    return comando


def mostrarDados(dado):
    from time import sleep
    escreva(f'Acessando o manual do comando \'{dado}\'', 4)
    sleep(2)
    print(cores[6], end='')
    help(dado)
    print(cores[0], end='')
    sleep(1)


def iniciarProgamaHelp():
    while True:
        escreva('SISTEMA DE AJUDA PYHELP', 2)
        comando = pegaDadoUsuario('Função ou Biblioteca > ')
        if comando.upper() == 'FIM':
            break
        mostrarDados(comando)


iniciarProgamaHelp()
escreva('Até Logo!', 1, True)
