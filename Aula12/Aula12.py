#Aula 12 Estruturas de Condicionais
nome = str(input('Nome: '))
if nome == 'Jesus':
    print('Que nome bonito !')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil !')
elif nome in 'Ana Cláudia Jêssica Juliana':
    print('Belo nome Feminino!')
else:
    print('Nome é normal')
print('Tenha um bom dia, {}!'.format(nome))