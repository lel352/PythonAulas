# Estrutura de Condição
tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')
print('--Fim--')

# Estrutura de Condição simplificada
print('--Estrutura de Condição simplificada--')
print('Carro novo' if tempo <= 3 else 'Carro velho')
print('--Fim--')

nome = str(input('Seu nome: '))
if nome == 'Odin':
    print('Bom dia {}'.format(nome))
else:
    print('Boa Noite {}'.format(nome))

nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
media = (nota1 + nota2)/2
print('Sua media foi {:.2f}'.format(media))
if media >= 6:
    print('Sua media foi boa')
else:
    print('Sua media foi Ruim! Estude mais!')

print('Parabens' if media >= 6 else 'Estude mais!')


