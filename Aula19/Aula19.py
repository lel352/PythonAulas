dados = dict()
dados = {'nome': 'Pedro', 'idade': 25}
print(dados['nome'])
print(dados['idade'])
dados['sexo'] = 'M'
print(dados['sexo'])
del dados['idade'] #deleta o elemento a chave Idade, sendo assim o atributo idade não existe mais no dicionario
print()

filme = {
    'titulo': 'Star Wars',
    'ano': 1977,
    'Diretor': 'George Lucas'
}
print(filme.values()) #Retorna os valores do dicionario
print(filme.keys()) #Retorna as chaves do dicionario
print(filme.items()) #Retorna as chaves e valores do dicionario, juntos
print()
for k, v in filme.items():
    print(f'O {k} é {v}')

filme2 = {
    'titulo': 'Avengers',
    'ano': 2012,
    'Diretor': 'Joss Whedon'
}

filme3 = {
    'titulo': 'Matrix',
    'ano': 1999,
    'Diretor': 'Wachowski'
}

print()
locadora = list()
locadora.append(filme)
locadora.append(filme2)
locadora.append(filme3)
print(locadora)
print(locadora[0]['ano'])
print(locadora[2]['ano'])
locadora[2]['ano'] = 1998
print(locadora[2]['ano'])
print(filme3)

print()
print()

pessoa = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoa['nome'])
print(pessoa['idade'])
print(f'O {pessoa["nome"]} tem {pessoa["idade"]} anos!')
print(pessoa.values()) #Retorna os valores do dicionario
print(pessoa.keys()) #Retorna as chaves do dicionario
print(pessoa.items()) #Retorna as chaves e valores do dicionario, juntos
print()
for k, v in pessoa.items():
    print(f'{k} = {v}')

del pessoa['sexo']

print()
for k, v in pessoa.items():
    print(f'{k} = {v}')

pessoa['nome'] = 'Jorge'
pessoa['sexo'] = 'M'
pessoa['peso'] = 98.5
print()
for k, v in pessoa.items():
    print(f'{k} = {v}')

brasil = []
estado1 = {'uf': 'Santa Catarina', 'sigla': 'SC'}
estado2 = {'uf': 'Acre', 'sigla': 'AC'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(estado2)
print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())
print(brasil)
print()
for e in brasil:
    for k, v in e.items():
        print(f'{k} = {v}')


