print('=========Desafio 069========')
pessoa18 = homem = mulher20 = 0
while True:
    print('-' * 20)
    print(' Cadastre uma Pessoa')
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo M/F: ')).strip().upper()[0]
    while sexo not in 'FM':
        sexo = str(input('Sexo inválido, digite novamente! Sexo M/F: ')).strip().upper()[0]

    if idade > 18:
        pessoa18 += 1
    if sexo == 'M':
        homem += 1
    elif sexo == 'F' and idade < 20:
        mulher20 += 1

    resposta = str(input('Deseja Continuar? S/N: ')).strip().upper()[0]
    while resposta not in 'SN':
        resposta = str(input('Opção inválido, digite novamente! Deseja Continuar? S/N: ')).strip().upper()[0]
    if resposta in 'N':
        break

print('='*20)
print(f'{pessoa18} pessoa acima dos 18 anos')
print(f'{homem} homens foram cadastrados')
print(f'{mulher20} mulheres menores de 20 anos')
print('='*20)
