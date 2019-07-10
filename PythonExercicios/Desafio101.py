print('=========Desafio 101========')


def voto(ano_Nascimento):
    from datetime import date
    idade = date.today().year - ano_Nascimento
    if idade < 16:
        return f'Com {idade} anos voto é NEGADO'
    elif 18 <= idade < 65:
        return f'Com {idade} anos voto é OBRIGATÓRIO'
    else:
        return f'Com {idade} anos voto é OPCIONAL'


ano = int(input('Digite seu ano de Nascimento: '))
print(voto(ano))
