print('=========Desafio 083========')
expressao = str(input('Expressão: '))
inicio = list()
fim = list()
tudo = list()
copia = list()
for v in expressao:
    if v in '{[(':
        inicio.append(v)
        tudo.append(v)
    elif v in '}])':
        fim.append(v)
        tudo.append(v)
auxi = list()
sim = '0'
bCorreta = True
for c in tudo:
    if c in '{[(':
        if sim != '0':
           auxi.append(sim)
        sim = c
    elif sim == '0':
        bCorreta = False
        break
    elif c in '}])':
        if (sim == '{' and c == '}') or (sim == '(' and c == ')') or (sim == '[' and c == ']'):
            sim = ''
            if len(auxi) > 0:
                sim = auxi.pop()
if (sim != '') or (len(auxi) > 0):
    bCorreta = False
if bCorreta:
    print('Expressão Correta!')
else:
    print('Expressão Incorreta!')

'''
expressao = str(input('Digite a Expressao: '))
pilha = []
for sim in expressao:
    if sim == '(':
        pilha.append('(')
    elif sim == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Expressão está Válida')
else:
    print('Expressão está inválida')
'''
