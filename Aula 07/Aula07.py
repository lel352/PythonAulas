'''
Ordem de precedência no calculo
1º - Parenteses ()
2º - ** Potencia
3º - *(multiplicacao) /(divisão) //(divisão inteira) %(Reste)
4 º- +(Adição) -(Subtração)
'''

print('raiz quadrada 25: {}'.format(25**(1/2))) #raiz quadrada 25
print('raiz Cubica 25: {}'.format(25**(1/3))) #raiz Cubica 25

numero1 = int(input('Numero1: '))
numero2 = int(input('Numero2: '))
soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao =  numero1 * numero2
divisao = numero1 / numero2
divisaoInteira = numero1 / numero2
exponenciacao = numero1 ** numero2

#end = ' ' não quebra a linha, dentro das aspas simples coloca o que deixar mostrar
print('Soma é {}, o produto é {} e a divisao é {:.3f}'.format(soma, multiplicacao, divisao), end=' ')
print('Divisão Inteira {} e potencia {}'.format(divisaoInteira, exponenciacao))
print('Soma é {}, o produto é {} e a divisao é {:.3f}'.format(soma, multiplicacao, divisao), end='>>>')
print('Divisão Inteira {} e potencia {}'.format(divisaoInteira, exponenciacao))
print('Soma vale {}'.format(soma))
print('Subtração vale {}'.format(subtracao))
print('Multiplicação vale {}'.format(multiplicacao))
print('Divisão vale {}'.format(divisao))
print('Divisão Inteira vale {}'.format(divisaoInteira))
#\n quebrar linha - nova linha
print('exponenciação \nvale {}'.format(exponenciacao))

