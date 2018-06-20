print('=========Desafio 025========')
nome = str(input('Digite seu nome: ')).strip()
print('Existe \'Silva\'? {}'.format('SILVA' in nome.upper()))

posicao = nome.upper().find('SILVA')
if posicao > -1:
    print('A Nome tem a palavra \'Silva\'')
else:
    print('A Nome não tem a palavra \'Silva\'')
