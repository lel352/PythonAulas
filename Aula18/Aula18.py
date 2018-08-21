dados = list()
dados.append('Pedro')
dados.append(25)

pessoas = list()
pessoas.append(dados[:])#fazendo uma copia de dados
print(pessoas)

pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
print(pessoas)

pessoas2 = list()
dados2 = ['Pedro', 25, 'Maria', 19, 'João', 32]
pessoas2.append(dados2[:])#fazendo uma copia de dados
print(pessoas2)

print(pessoas[0][0])# sai Pedro
print(pessoas[1][1])# sai 19
print(pessoas[2][0])# sai João
print(pessoas[1])# sai [Maria, 19]
print('-'*20)

teste = list()
teste.append('Gustavao')
teste.append(40)
print(teste)
galera = list()
''' Cria uma ligação
galera.append(teste)
print(galera)
teste[0] = 'Maria'
teste[1] = '22'
print(teste)
galera.append(teste)
print(galera)
'''
galera.append(teste[:])
print(galera)
teste[0] = 'Maria'
teste[1] = '22'
print(teste)
galera.append(teste[:])
print(galera)

galera2 = [['João', 19], ['Ana', 33], ['Joana', 13], ['Marcos', 45]]
print(galera2)
print(galera2[0][0]) #João
print(galera2[2][1]) #13
print()
for p in galera2:
    print(p)
    print(p[0])
    print(f'{p[0]} tem {p[1]} anos de idade.')

print('-'*20)
galera3 = list()
dado = list()
for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera3.append(dados[:])
    dados.clear()

print(galera3)

for p in galera3:
    if p[1] >= 21:
        print(f'{p[0]} tem {p[1]} anos de idade. Maior de idade')
    else:
        print(f'{p[0]} tem {p[1]} anos de idade. Menor de idade')
