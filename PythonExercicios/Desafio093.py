print('=========Desafio 093========')
print('---Dados do Jogador---')
jogador = dict()
jogador['nome'] = str(input('Nome: '))
partidas = int(input('Quatidade de partidas: '))
partidas_gol = list()
soma = 0
for c in range(0, partidas):
    partidas_gol.append(int(input(f'{c+1}ª partida - Quantidade de Gol: ')))
jogador['gols'] = partidas_gol[:]
jogador['total'] = sum(partidas_gol)
print('='*50)
for k, v in jogador.items():
    print(f'{k} = {v} ')
print('='*50)
print(f'Jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for c, v in enumerate(jogador['gols']):
    print(f'  => Na Partida {c+1}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols')
