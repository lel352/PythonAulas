from random import shuffle
print('=========Desafio 020========')
aluno1 = input('Aluno 1: ')
aluno2 = input('Aluno 2: ')
aluno3 = input('Aluno 3: ')
aluno4 = input('Aluno 4: ')

listaAluno = range(4)
listaAluno = [aluno1, aluno2, aluno3, aluno4]
shuffle(listaAluno)
print('Lista de apresentação é: ')
for i in listaAluno:
    print(i)
print(listaAluno)
