print('=========Desafio 057========')
sexo = 'A'
sexo = str(input('Digite seu sexo [F/M]:')).strip().upper()[0]#pegar somente a primeira letra
while sexo not in 'FM':
      print('Sexo inválido! Digite novamente!')
      sexo = str(input('Digite seu sexo [F/M]:')).strip().upper()[0]  # pegar somente a primeira letra
if sexo == 'F':
    print('Seu sexo é Feminino')
else:
    print('Seu sexo é Masculino')
