from Aulas.Desafios.Desafio115.lib.interface import *
from Aulas.Desafios.Desafio115.lib.arquivo import *
from time import sleep

nomeArquivo = 'arquivonomes.txt'

if not arquivoExiste(nomeArquivo):
   criarArquivo(nomeArquivo)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        # listar o conteúdo de um arquivo
        lerArquivo(nomeArquivo)
    elif resposta == 2:
        cabecalho('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(nomeArquivo, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do Sistema... Até logo!')
        break
    else:
        print('\033[31mErro! Digite uma opção Válida!\033[m' )
    sleep(2)



