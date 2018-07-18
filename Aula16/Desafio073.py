print('=========Desafio 073========')
colocados = ('Criciúma', 'Atlético', 'Flamengo', 'Corinthians', 'Palmeiras', 'América-MG', 'São Paulo', 'Grêmio', 'Vasco da Gama', 'Internacional', 'Botafogo', 'Sport Recife', 'Cruzeiro', 'EC Vitória', 'Santos', 'Chapecoense', 'Atlético-PR', 'Bahia', 'Ceará SC', 'Paraná')

print('Tabela do Campeonato')
for posicao, time in enumerate(colocados):
    print(f'{posicao+1}ª - {time}')
print('\n')
print(f'a) 5 primeiros: {colocados[:5]}')
print(f'b) 4 Últimos: {colocados[-4:]}')
print(f'c.1) Ordem Alfabetica: {sorted(colocados)}')
print(f'c.2) Ordem Alfabetica:')
for time in sorted(colocados):
    print(time)
print('\n')
print(f'd)Chapecoense está na posicao {colocados.index("Chapecoense")+1} ª')
