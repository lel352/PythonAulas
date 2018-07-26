print('=========Desafio 072========')
valores = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
          'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze',
          'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
resposta = 'S'
while True:
    numero = int(input('Digite um numero entre 0 e 20: '))
    while (numero < 0) or (numero > 20):
        numero = int(input('Valor inválido, digite novamente! \nDigite um numero entre 0 e 20: '))
    print(f'Você digitou o número {valores[numero]}')
    resposta =  str(input('Deseja Continuar? [s/n]')).upper().strip()[0]
    while resposta not in 'NS':
        resposta = str(input('Resposta inválida. Deseja Continuar? [s/n]')).upper().strip()[0]
    if resposta == 'N':
        break
