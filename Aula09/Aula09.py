'''
Cadeia de caracteres - String
'''

frase = 'Curso em Vídeo Python'
print('=========fateamento de String===========')
print(frase)

print('frase[9]= {}'.format(frase[9]))#imprime a posição 9 = V
'''
#imprime da posicao 9 até 13
(ele desconsidera a ultimo valor ou seja o posicao 14) = Vídeo
'''
print('frase[9:13]= {}'.format(frase[9:14]))
'''
#imprime da posicao 9 até 20
(ele desconsidera a ultimo valor ou seja o posicao 21) = Vídeo Python
'''
print('frase[9:21]= {}'.format(frase[9:21]))
'''
#imprime da posicao 9 até 20
(ele desconsidera a ultimo valor ou seja o posicao 21) 
mas pulando em dois em dois(:2 na parte final) = VdoPto
'''
print('frase[9:21:2]= {}'.format(frase[9:21:2]))
'''
#imprime da posicao 0 até 4
se omitir a primeira parte ele 
começa de zero
=Curso
'''
print('frase[:5]= {}'.format(frase[:5]))

'''
#imprime da posicao 15 até o finaç
se omitir a segunda parte ele 
complender que é para ir até ultima posição da String
=Python
'''
print('frase[15:]= '.format(frase[15:]))
'''
#imprime da posicao 9 até final
Segunda parte omitida então vai até o final
e pulando em três em três(:2 na parte final) = VdoPto
=VePh
'''
print('frase[9::3]='.format(frase[9::3]))
print('\n\n=========Analise de String===========')
print('(len)cumprimento da frase = {}'.format(len(frase)))#=21
print('(.count(\'o\')Contar a quantidade da letra \'o\'(minúscula) na frase = {}'.format(frase.count('o')))#=3
print('(.count(\'o\',0,13)Contar a quantidade da letra \'o\'(minúscula) na frase \n mas da posição 0 a 12(posição 13 '
      'é ignorado lembre) = {}'.format(frase.count('o', 0, 13)))#=1
print('(.find(\'deo\'))Posição que começou o \'deo\' onde encontrou na frase = {}'.format((frase.find('deo'))))#=11
print('(.find(\'Android\'))Retorna -1 pois \'Android\' não tem na frase = {}'.format((frase.find('Android'))))
print('(\'Curso\ in frase) Existe \'Curso\' em frase = {} '.format('Curso' in frase)) #true
print('(\'curso\ in frase)Existe \'curso\' em frase = {} '.format('curso' in frase)) #False

print('\n\n=========Transformação de String===========')
'''
Troca um por outro mas não modifica em si a frase dentro da variavel 
so modifica para um retorno da função para:
 replace
 Upper
 Lower
'''
print('(frase.replace(\'Python\',\'Android\')) troca um por outro frase = {}'.format(frase.replace('Python','Android')))
print(frase)
print('upper para Cima {}'.format(frase.upper()))
print(frase)
print('upper para baixo {}'.format(frase.lower()))
print(frase)
print('Capitalize (primeira letra Maiúsculo e o resto minúsculo) {}'.format(frase.capitalize()))
print(frase)
print('Title (Maiúsculo palavra por palavra a primeira letra) {}'.format(frase.title()))
print(frase)
frase2 = '  '+frase+'  '
print(frase2)
print('strip (Remove os espaços inuteis na direira e esquerda) {}'.format(frase2.strip()))
print(frase2)
print('Rstrip (Remove os espaços inuteis a direita (no fim)) {}'.format(frase2.rstrip()))
print(frase2)
print('lstrip (Remove os espaços inuteis a esquerda(no inicio)) {}'.format(frase2.lstrip()))
print(frase2)
print(frase)
'''
Dividi a String conforme o um caracter informado entre parenteses
um delimitador
default é os espaços 
gerando uma lista
'''
print('split() {}'.format(frase.split()))
print('split() {}'.format(frase.split('o')))
dividido = frase.split()
print(dividido[0][1])
'''
juntar uma coisa na outra
junta cada elemento de uma lista 
com um elo de ligação que desejar
no exemplo abaixo é o '-'
'''
print('.join(frase) {}'.format('-'.join(frase.split())))

'''
Saiu o texto conforme eu quero
'''
print('''
A amizade consegue ser tão complexa...
Deixa uns desanimados, outros bem felizes...
É a alimentação dos fracos
É o reino dos fortes

Faz-nos cometer erros
Os fracos deixam se ir abaixo
Os fortes erguem sempre a cabeça
os assim assim assumem-os

Sem pensar conquistamos
O mundo geral
e construímos o nosso pequeno lugar
deixando brilhar cada estrelinha

Estrelinhas...
Doces, sensíveis, frias, ternurentas...
Mas sempre presentes em qualquer parte
Os donos da Amizade...''')

print('contando \'O\' usando upper {}'.format(frase.upper().count('O')))

