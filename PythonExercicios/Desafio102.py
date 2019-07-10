print('=========Desafio 102========')
def fatorial(numero = 1, show = False):
    '''
    => Calcula o fatorial de um número
    :param numero: valor a ser feito o calculo
    :param show: True mostra todo o processo do calculo
    :return: retorna o valor do calculo
    '''
    if show:
        resultado = numero
        print(f'{numero} ', end='')
        for c in range(numero - 1, 0, -1):
            print(f'x {c} ', end='')
            resultado *= c
        print(f'= {resultado}')
    else:
        resultado = 1
        for c in range(numero, 0, -1):
            resultado *= c
        print(f'{resultado}')
    return resultado
    ''' 
    Com if dentro do for
    resultado = 1
    for c in range(numero, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        resultado *= c
    return resultado
    
    '''


print('-' * 20)
print(fatorial(5, False))
print('-' * 20)
fatorial(5, True)
print('-' * 20)
fatorial(5)
print('-' * 20)
fatorial(5, show=False)
print('-' * 20)
help(fatorial)