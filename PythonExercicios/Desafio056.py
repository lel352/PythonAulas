print('=========Desafio 056========')
somaIdade = 0
idadeHomemVelho = 0
nomeHomemVelho = ''
quatidadeMulheres = 0
for c in range(1, 5):
    print('{:-^20}'.format(str(c)+'ª Pessoa'))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo M/F: ')).strip().upper()
    somaIdade += idade
    if sexo == 'M' and idadeHomemVelho < idade:
        idadeHomemVelho = idade
        nomeHomemVelho = nome
    elif sexo == 'F' and idade < 20:
        quatidadeMulheres += 1

print('-'*20)
media = somaIdade / 4
print('A media de idade do grupo é {:.2f} anos'.format(media))
print('Com a idade de {} anos, {} é o homem mais velho '.format(idadeHomemVelho, nomeHomemVelho))
print('Quantidade de Mulheres menores de 20 anos é de {} mulhere(s)'.format(quatidadeMulheres))
