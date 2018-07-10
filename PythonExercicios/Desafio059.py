print('=========Desafio 059========')
resposta = -1
while resposta != 5:
    if resposta != -1:
        print('='*20)
        print('[1] - Somar')
        print('[2] - Mulplilicar')
        print('[3] - Maior')
        print('[4] - Novos Números')
        print('[5] - Sair do Programa')
        print('='*20)
        resposta = int(input('Digite uma opção: '))
        if resposta > 0 and resposta > 5:
            print('opção Inválida! Digite novamente!')
        print('=' * 20)
    if resposta == -1 or resposta == 4:
        print('{:-^20}'.format('Informe os valores'))
        numero1 = int(input('Numero 1: '))
        numero2 = int(input('Numero 2: '))
        resposta = 4
    elif resposta == 1:
        print('Soma: {} + {} = {}'.format(numero1, numero2, (numero1 + numero2)))
        input('aperte qualquer tecla para continuar...')
    elif resposta == 2:
        print('Multiplicação: {} * {} = {}'.format(numero1, numero2, (numero1 * numero2)))
        input('aperte qualquer tecla para continuar...')
    elif resposta == 3:
        if numero1 > numero2:
            print('Maior numero é {} '.format(numero1))
        else:
            print('Maior numero é {} '.format(numero2))
        input('aperte qualquer tecla para continuar...')
    elif resposta == 5:
        print('Saindo do Programa!')
print('Fim do Programa!')
