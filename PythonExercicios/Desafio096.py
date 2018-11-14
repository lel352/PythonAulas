print('=========Desafio 096========')
def area(largura, comprimeto):
    valor = largura * comprimeto
    print(f' A área de um terreno de {largura}x{comprimeto} é de {valor}m²')

print('=========Controle de Terreno========')
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
area(largura, comprimento)
