print('=========Desafio 044========')
print('{:=^40}'.format('Lojas da Vida'))
preco = float(input('Preço Normal: '))
print('=' * 20)
print('{:^20}'.format('Condição de Pagamento'))
print('=' * 20)
print('''1 - À vista dinheiro/Cheque'
2 - À vista no Cartão'
3 - Até 2x no Cartão '
4 - Até 3x  ou mais no Cartão''')
print('=' * 20)
opcao = int(input('Digite uma Opção: '))
#if str(opcao) not in '1 2 3 4':
if opcao == 1:
    desconto = (preco * 10) / 100
    print('Preço R${:.2f} \nDesconto R${:.2f} \nNovo Preço R${:.2f}'.format(preco, desconto, (preco - desconto)))
elif opcao == 2:
    desconto = (preco * 5) / 100
    print('Preço R${:.2f} \nDesconto R${:.2f} \nNovo Preço R${:.2f}'.format(preco, desconto, (preco - desconto)))
elif opcao == 3:
    parcela = preco / 2
    print('Sua compra será parcelada em 2x de R${:.2f} '.format(parcela))
    print('Preço Total R${:.2f} '.format(preco))
elif opcao == 4:
    aumento = (preco * 20) / 100
    totalParcelas = int(input('Quantas Parcelas: '))
    parcela = (aumento + preco)/totalParcelas
    print('Sua compra será parcelada em {}x de R${:.2f} '.format(totalParcelas, parcela))
    print('Preço {:.2f} \nAumento {:.2f} \nNovo Preço {:.2f}'.format(preco, aumento, (preco + aumento)))
else:
    print('Opção inválida!')

