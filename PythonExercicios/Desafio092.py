from datetime import date
print('=========Desafio 092========')
print('---Dados da Pessoa---')
pessoa = dict()
pessoa['nome'] = str(input('Nome: '))
ano_Nascimento = int(input('Ano de Nascimento: '))
pessoa['idade'] = date.today().year - ano_Nascimento
pessoa['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoa['ctps'] > 0:
    pessoa['contratação'] = int(input('Ano de Contratação: '))
    pessoa['salário'] = float(input('Salário: '))
    pessoa['aposentadoria'] = (pessoa['contratação'] - ano_Nascimento) + 35

print('='*20)
print(f'{pessoa}')

for k, v in pessoa.items():
    print(f'{k} = {v}')
