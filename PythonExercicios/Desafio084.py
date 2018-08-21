print('=========Desafio 084========')
pessoas = list()
pessoa = list()
maior = menor = 0
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    pessoas.append(pessoa[:])
    if len(pessoas) == 1:
       maior = menor = pessoa[1]
    elif maior < pessoa[1]:
        maior = pessoa[1]
    elif menor > pessoa[1]:
        menor = pessoa[1]
    pessoa.clear()
    reposta = str(input('Deseja Continuar? [S/N]')).strip().upper()[0]
    while reposta not in 'SN':
        reposta = str(input('Resposta invlida! Deseja Continuar? [S/N]')).strip().upper()[0]
    if reposta in 'N':
        break
print(f'Foi cadastrado {len(pessoas)} pessoas')
maisPesadas = list()
maisLeves = list()
for p in pessoas:
    if p[1] == maior:
        maisPesadas.append(p[0])
    elif p[1] == menor:
        maisLeves.append(p[0])
print(f'O maior pesso foi de {maior}kg. Peso de {maisPesadas}')
print(f'O menor pesso foi de {menor}kg. Peso de {maisLeves}')
