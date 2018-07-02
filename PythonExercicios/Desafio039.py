from datetime import date

print('=========Desafio 039========')
anoNascimento = int(input('Ano de Nascimento: '))
anoAtual = date.today().year
idade = anoAtual - anoNascimento
if idade == 18:
    print('Você tem 18 anos. Hora de se alistar')
elif idade < 18:
    tempo = 18 - idade
    print('Você tem {} anos. Ainda não é hora de se alistar.'.format(idade), end='')
    print('Falta {} ano(s) ({}) para se alistar'.format(tempo, tempo + anoAtual))
else:
    tempo = idade - 18
    print('Você tem {} anos. Já passou da hora de se alistar.'.format(idade), end='')
    print(' Já passou {}({}) ano(s)'.format(tempo, anoNascimento + 18))
