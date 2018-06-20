print('=========Desafio 026========')
frase = str(input('Digite uma frase: ')).upper().strip()
print('Quantidade de A: {}'.format(frase.count('A')))
print('Primeira vez de A: {}'.format(frase.find('A')+1))
print('Ultima vez de A: {}'.format(frase.rfind('A')+1))


