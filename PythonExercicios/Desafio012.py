print('=========Desafio 012========')
valor = float(input('Digite o valor do Produto: '))
valorDesconto = valor * (5/100)
novoValor = valor - valorDesconto
print('novo valor com desconto de 5% é {:.2f}'.format(novoValor))
