print('=========Desafio 040========')
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
media = (nota1 + nota2) / 2
print('Sua media foi de {:.2f}'.format(media))
if media < 5:
    print('Reprovado.')
elif 5 <= media < 7: #forma simplificada  media >= 5 and media <= 6.9
    print('Recuperação.')
else:
    print('Aprovado.')# maior que 7
