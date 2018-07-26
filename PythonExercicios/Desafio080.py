print('=========Desafio 080========')
valores = list()
for c in range(0, 5):
    valor = int(input(f'Digite o valor {c+1}: '))
    '''if valor in valores:
        posicao = valores.index(valor)
        valores.insert(posicao, valor)
        print(f'Adicionado na posicao {posicao}')
        '''
    if c == 0 or valor > valores[-1]:
        valores.append(valor)
        print('Adicionado na posicao inicial')
    else:
        for p, v in enumerate(valores):
            if v > valor:
                valores.insert(p, valor)
                print(f'Adicionado na posicao {p}')
                break
print(f'Valores em ordem: {valores}')
