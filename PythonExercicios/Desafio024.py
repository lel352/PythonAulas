print('=========Desafio 024========')
cidade = str(input('Cidade: ')).strip()
print('A cidade começa com a palavra \'Santo\'? {}'.format('SANTO' in cidade[0:5].upper()))

posicao = cidade.upper().find('SANTO')
if posicao == 0:
    print('A cidade começa com a palavra \'Santo\'')
else:
    print('A cidade não começa com a palavra \'Santo\'')
