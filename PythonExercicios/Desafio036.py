print('=========Desafio 036========')
valorCasa = float(input('Valor da Casa R$: '))
salario = float(input('Salario R$: '))
quantidadeAnos = int(input('Quantidade Anos: '))
parcelas = quantidadeAnos * 12
valorParcela = valorCasa / parcelas
limiteSalario = (salario * 30) /100
print('\n\n\n--------Reposta--------')
print('Valor Casa R$: {:.2f}'.format(valorCasa))
print('Numero de Parcelas: {} ({} anos)'.format(parcelas, quantidadeAnos))
print('Valor da Parcela R$: {:.2f}'.format(valorParcela))
print('Salario R$: {:.2f}'.format(salario))
print('Limite de 30% do salario R$: {:.2f}'.format(limiteSalario))
if limiteSalario < valorParcela:
    print('Emprestimo para casa Negado!')
    print('Limite de 30% do salario é inferior ao valor da parcela')
else:
    print('Emprestimo da casa Aprovado!')
