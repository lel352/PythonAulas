from random import randint
print('=========Desafio 045========')
print('{:^20}'.format('Jo ken pô'))
print('=' * 20)
print('{:20}'.format('1 - Pedra'))
print('{:20}'.format('2 - Papel'))
print('{:20}'.format('3 - Tesoura '))
print('=' * 20)
opcao = int(input('Digite uma Opção: '))
if str(opcao) not in '1 2 3':
    print('Opção inválida!')
    exit(0)
computador = randint(1, 3)
jokenpo = {1: 'Pedra', 2: 'Papel', 3: 'Tesoura'}

print('=' * 20)
print('Você escolheu {} !'.format(jokenpo[opcao]))
print('Maquina escolheu {} !'.format(jokenpo[computador]))
print('=' * 20)
if (computador == 1) and (opcao == 1) or (computador == 2) and (opcao == 2) or (computador == 3) and (opcao == 3):
    print('\033[0;34mEmpate !\33[m')
elif (computador == 1) and (opcao == 2) or (computador == 2) and (opcao == 3) or (computador == 3) and (opcao == 1):
    print('\033[0;33mVocê Venceu !\33[m')
elif (computador == 1) and (opcao == 3) or (computador == 2) and (opcao == 1) or (computador == 3) and (opcao == 2):
    print('\033[0;31mComputador Venceu !\33[m')
print('=' * 20)
