'''
Ordem de precedência no calculo
1º - Parenteses ()
2º - ** Potencia
3º - *(multiplicacao) /(divisão) //(divisão inteira) %(Reste)
4 º- +(Adição) -(Subtração)
'''

nome = input('Qual seu nome: ')
print('Prazer em te conhecer {}!'.format(nome))
#vai imprimir 20 espaços para o nome
print('Prazer em te conhecer {:20}!'.format(nome))
#vai imprimir 20 espaços para o nome alinhando a direita
print('Prazer em te conhecer {:>20}!'.format(nome))
#vai imprimir 20 espaços para o nome alinhando a esquerda
print('Prazer em te conhecer {:<20}!'.format(nome))
#vai imprimir 20 espaços para o nome alinhando Centralizado
print('Prazer em te conhecer {:^20}!'.format(nome))
#vai imprimir 20 espaços para o nome alinhando Centralizado
#onde os espaços em branco vai ser preenxido por '='
print('Prazer em te conhecer {:=^20}!'.format(nome))

#vai imprimir o nome *5 vezes
print('Prazer em te conhecer {}!'.format(nome*5))
