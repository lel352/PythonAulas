from pip._vendor.distro import cached_property

from Aulas.Desafios.Desafio115.lib.interface import *

def arquivoExiste(nome):
    try:
        arquivo = open(nome, 'rt')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        arquivo = open(nome, 'wt+') #w =  write, + é para caso não exister criar
        arquivo.close()
    except:
        print('Houve um ERRO ao Criar o Arquivo! ')
    else:
        print(f'Aquivo {nome} Criado com Sucesso! ')


def lerArquivo(nome):
    try:
        arquivo = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo! ')
    else:
        cabecalho('Pessoas Cadastradas')
        for linha in arquivo:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        arquivo.close()


def cadastrar(nomeArquivo, nome='desconhecido', idade=0):
    try:
        arquivo = open(nomeArquivo, 'at')
    except:
        print('Erro ao Abrir o arquivo! ')
    else:
        try:
            arquivo.write(f'{nome};{idade}\n')
        except:
           print('Erro na hora de Escrever os Dados! ')
        else:
            print(f'Novo registro de {nome} adicionado! ')
            arquivo.close()





