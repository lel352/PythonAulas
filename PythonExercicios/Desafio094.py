print('=========Desafio 094========')
pessoas = list()
total = 0
somaIdades = 0
while True:
    pessoa = dict()
    pessoa['nome'] = str(input('Nome: '))
    sexo = str(input('Sexo M/F: ')).strip().upper()[0]
    while sexo not in 'FM':
        sexo = str(input('Sexo inválido, digite novamente! Sexo M/F: ')).strip().upper()[0]
    pessoa['sexo'] = sexo
    pessoa['idade'] = int(input('Idade: '))
    total += 1
    somaIdades += pessoa['idade']
    pessoas.append(pessoa.copy())
    pessoa.clear()
    reposta = str(input('Deseja Continuar? [S/N]')).strip().upper()[0]
    while reposta not in 'SN':
        reposta = str(input('Resposta invlida! Deseja Continuar? [S/N]')).strip().upper()[0]
    if reposta in 'N':
        break
media = somaIdades / total
print('='*20)
print(f'- O Grupo tem {total} pessoa. ')
print(f'- A média de idade é de {media:.2f} anos ')
print(f'- As mulheres cadastras foram: ',end='')
acima = list()
mulheres = list()
for c in pessoas:
    if c['sexo'] in 'F':
        mulheres.append(c['nome'])
        print(f'{c["nome"]}, ', end='')
    if c['idade'] > media:
        acima.append(c.copy())
print('\n- Lista das Pessoas que estão acima da média: ')
for c in acima:
    for k, v in c.items():
        print(f' - |{k} = {v}', end='')
    print()
