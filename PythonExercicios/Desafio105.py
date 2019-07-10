print('=========Desafio 105========')


def notas(*notas, situacao=False):
    '''
    => Função para Analisar notas e situações de vários alunos
    :param notas: uma ou mais notas do alunos (várias notas)
    :param situacao: (valor opcional) para mostrar ou não a situação da turma
    :return: dicionário com informações sobre a turma
    '''
    dado = dict()
    soma = sum(notas)
    media = soma / len(notas)
    dado['quantidade'] = len(notas)
    dado['maior'] = max(notas)
    dado['menor'] = min(notas)
    dado['media'] = media
    if situacao:
        if media > 9:
            dado['situacao'] = 'Excelente'
        elif 7 <= media < 9:
            dado['situacao'] = 'BOA'
        elif 5 <= media < 7:
            dado['situacao'] = 'RAZOÁVEL'
        else:
            dado['situacao'] = 'RUIM'
    return dado


resposta = notas(3.5, 2, 6.5, situacao=True)
print(resposta)
print()
resposta = notas(3.5, 9, 5, 2, 6.5)
print(resposta)
