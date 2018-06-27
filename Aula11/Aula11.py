'''
para representar as cores no terminal
deve ser usar
contra barra, 033, colchetes e a letra m
entre conchetes e m, ve os dados para cor
\033[ m

entre [ m
primeira parte: style: da fonte
Segunda parte: text: cor do texto
terceira parte: back: o background cor do fundo

\033[0:33:44m
0-style
33-cor do texto
44-cor de fundo

style
0 -Sem estilo
1 -negrito
4 -sublinhado _underline
7 -Inverte configurações = texto com fundo

text
30 -branco
31 -vermelho
32 -Verde
33 -Amarelo
34 -Azul
35 -Roxo
36 -Azul-Verde
37 -Cinza

background
40 -branco
41 -vermelho
42 -Verde
43 -Amarelo
44 -Azul
45 -Roxo
46 -Azul-Verde
47 -Cinza
'''
print('\033[0;30;41mTeste')
print('\033[4;33;44mTeste')
print('\033[1;35;43mTeste')
print('\033[0;30;42mTeste')
print('\033[30;42mTeste')  # sem estilo pode não colocar nada
print('\033[mTeste')  # configuração padrao
print('\033[7;30mTeste')  # fundo fica branco 7 - faz essa troca

print('\033[1;31;43mOlá, Mundo!\033[m')  # \033[m não final, deixa a formação ir a linha toda
print('\033[4;31;43mOlá, Mundo!\033[m')
print('\033[4;30;45mOlá, Mundo!\033[m')

# para ter fundo branco usa o 7 antes para inverter os valores
print('\033[7;30mOlá, Mundo!\033[m')
# letra amarela, fundo azul
print('\033[0;33:44mOlá, Mundo!\033[m')
# 7 inverte - letra azul, fundo amarela
print('\033[7;33:44mOlá, Mundo!\033[m')

a = 3
b = 5
print('os Valores são \033[32m{}\033[m e \033[31m{}\033[m !!!'.format(a, b))

nome = 'Santos'
print('Olá, {}{}{} !!!'.format('\33[4;31m', nome, '\33[m'))

cores = {'limpa': '\33[m',
         'azul': '\33[34m',
         'amarelo': '\33[33m',
         'pretoebranco': '\33[7;30m'}
print('Olá, {}{}{} !!!'.format(cores['pretoebranco'], nome, cores['limpa']))
print('Olá, {}{}{} !!!'.format(cores['azul'], nome, cores['limpa']))
