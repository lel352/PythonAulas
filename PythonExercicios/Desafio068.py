from random import randint
print('=========Desafio 068========')
print('!!!Par ou Impar!!!')
vitorias = 0
while True:
    numero = int(input('Digite um valor: '))
    print('=' * 20)
    escolha = str(input('Par ou Impar [P/I]: ')).strip().upper()[0]
    while escolha not in 'iIpP':
        escolha = str(input('Opção inválida, digite novamente! Par ou Impar [P/I]: ')).strip().upper()[0]
    aleatorio = randint(0,10)
    if (escolha in 'Pp' and (aleatorio + numero) % 2 == 0) or (escolha in 'iI' and (aleatorio + numero) % 2 != 0):
       print('=' * 20)
       print(f'Você Venceu! Seu numero: {numero} computador: {aleatorio} ')
       print('=' * 20)
       vitorias += 1
    else:
        break;
print(f'Você Perdeu! Seu numero: {numero} computador: {aleatorio} ')
print(f'Sua maior sequencia de vitorias foi de {vitorias}')
