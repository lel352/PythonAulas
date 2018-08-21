print('=========Desafio 089========')
alunosNota = list()
while True:
    aluno = list()
    notas = list()
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/2
    #alunosNota.append([nome, media, [nota1, nota2]])
    notas.append(nota1)
    notas.append(nota2)
    aluno.append(nome)
    aluno.append(media)
    aluno.append(notas[:])
    alunosNota.append(aluno[:])
    aluno.clear()
    notas.clear()
    reposta = str(input('Deseja Continuar? [S/N]')).strip().upper()[0]
    while reposta not in 'SN':
        reposta = str(input('Resposta invlida! Deseja Continuar? [S/N]')).strip().upper()[0]
    if reposta in 'N':
        break
print('-'*20)
print('No. Nome       Média')
for p, c in enumerate(alunosNota):
    print(f'{p:<3} {c[0]:<10} {c[1]:>5.2f}')
print('-'*20)
while True:
    numero = int(input('Mostrar notas de qual aluno? (999 Interrompe): '))
    if numero == 999:
        break
    if numero > len(alunosNota) - 1:
        print('Numero invalido!')
        continue
    print('-' * 20)
    print(f'Notas de {alunosNota[numero][0]} são {alunosNota[numero][2]}')
    print('-' * 20)
print('Finalizado')
