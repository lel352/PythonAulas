from random import choice
print('=========Desafio 019========')
aluno1 = input('Aluno 1: ')
aluno2 = input('Aluno 2: ')
aluno3 = input('Aluno 3: ')
aluno4 = input('Aluno 4: ')
listaAluno = [aluno1, aluno2, aluno3, aluno4]
escolhido = choice(listaAluno)
print('Aluno escolhido foi {}'.format(escolhido))
'''
forma sem lista
escolhido = random.randint(1, 4)
if escolhido == 1:
    print('Aluno escolhido foi {}'.format(aluno1))
elif escolhido == 2:
    print('Aluno escolhido foi {}'.format(aluno2))
elif escolhido == 3:
    print('Aluno escolhido foi {}'.format(aluno3))
elif escolhido == 4:
    print('Aluno escolhido foi {}'.format(aluno4))
'''

