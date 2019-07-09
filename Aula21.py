help(input)
print('\n\n\n\n')
print()


def contador(i, f, p):
    # docStrings documentação
    '''
    => Faz uma contagem e mostra na tela
    :param i: Valor inicial
    :param f: valor final
    :param p: passo da Contagem
    :return: Sem Retorno
    '''
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('Fim')


contador(2, 10, 2)
help(contador)


# argumentos opcionais

def somar(a=0, b=0, c=0):
    '''
     => Somar Três valores
    :param a: valor 1
    :param b: valor 1
    :param c: valor 2
    :return: Sem retorno
    Caso não for informado um dos paramentos ele recebe por default '0'
    '''
    s = a + b + c
    print(f'A soma vale {s}')


print('\n')
somar()
somar(3, 5, 6)
somar(3, 12)
somar(c=2, a=24)

print('\n')


# escopo de variáveis
def teste():
    n = 6  # assim ele cria uma nova variável local não usa o n global
    # para usar a variavel global dentro de uma função deve se usar o Comando
    # 'global' mas o nome da variável
    x = 8
    print(f'Na função, n vale {n}')
    print(f'Na função, x vale {x}')


# parte principal
n = 2
print(f'Na parte principal, n vale {n}')
teste()
# não funciona, erro devido que o x so existe dentro da função
# print(f'Na parte principal, x vale {x}')
print('\n')


def teste():
    global n  # para usar a variavel global dentro de uma função, assim ele não cria um variável nova na memória
    # n = 2
    x = 8
    print(f'Na função, n vale {n}')
    print(f'Na função, x vale {x}')


# parte principal
n = 4
print(f'Na parte principal, n vale {n}')
teste()
# não funciona, erro devido que o x so existe dentro da função
# print(f'Na parte principal, x vale {x}')
print('\n')


# retorno de valores

def somar(a=0, b=0, c=0):
    '''
     => Somar Três valores
    :param a: valor 1
    :param b: valor 1
    :param c: valor 2
    :return: retorna a soma
    Caso não for informado um dos paramentos ele recebe por default '0'
    '''
    s = a + b + c
    return s


resposta1 = somar(3, 5, 6)
resposta2 = somar(3, 12)
resposta3 = somar(c=2, a=24)
print(f'Meus cálculos deram {resposta1}, {resposta2}, {resposta3}')
print('\n')


def fatorial(numero=1):
    f = 1
    for c in range(numero, 0, -1):
        f *= c
    return f


n = int(input('Digite um numero: '))
print(f'Fatorial de {n} é igual a {fatorial(n)}')
n = 4
print(f'Fatorial de {n} é igual a {fatorial(n)}')
print(f'Fatorial de  é igual a {fatorial()}')
print('\n')


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


n = int(input('Digite um numero: '))
if par(n):
    print(f'é par')
else:
    print(f'é impar')
