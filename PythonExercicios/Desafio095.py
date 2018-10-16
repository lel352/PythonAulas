from builtins import enumerate

print('=========Desafio 094========')
jogadores = list()
jogador = dict()
while True:
    print('---Dados do Jogador---')
    jogador.clear()
    jogador['nome'] = str(input('Nome: '))
    partidas = int(input('Quatidade de partidas: '))
    partidas_gol = list()
    soma = 0
    for c in range(0, partidas):
        partidas_gol.append(int(input(f'{c+1}ª partida - Quantidade de Gol: ')))
    soma = sum(partidas_gol)
    jogador['gols'] = partidas_gol
    jogador['total'] = soma
    jogadores.append(jogador.copy())
    reposta = str(input('Deseja Continuar? [S/N]')).strip().upper()[0]
    while reposta not in 'SN':
        reposta = str(input('Resposta invlida! Deseja Continuar? [S/N]')).strip().upper()[0]
    print('----------------------')
    if reposta in 'N':
        break
print('==='*20)
print('cod. Nome       total Gols')
print('-'*40)
while True:
    print()
    print('===' * 20)
    print('cod. Nome       total Gols')
    print('-' * 40)
    for p, c in enumerate(jogadores):
        #print(f'{p:<3} {c["nome"]:<10} {c["gols"]:>19} {c["total"]:<5}')
        print(f'{p:<4} {c["nome"]:<10} {c["total"]:<5} {c["gols"]} ')
    print('-'*20)

    numero = int(input('Mostrar notas de qual Jogador (999 - Sair)? '))
    if numero == 999:
        break
    if numero > len(jogadores) - 1:
        print('Numero invalido!')
        continue

    jogador = jogadores[numero].copy()
    print(f'--levantamento do Jogador {jogador["nome"]}')
    for c, v in enumerate(jogador['gols']):
        print(f'  => Na Partida {c+1}, fez {v} gols.')
    jogador.clear()
print('-'*20)
print('Finalizado')
