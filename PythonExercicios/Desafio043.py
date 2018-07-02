print('=========Desafio 043========')
peso = float(input('Peso (Kg): '))
altura = float(input('Altura (m): '))
imc = (peso / (altura ** 2))
print('IMC: {:.2f} '.format(imc))
if imc < 18.5:
    print('Está Abaixo do Peso.')
elif 18.5 <= imc < 25.0:
    print('Peso Ideal.')
elif 25.0 <= imc < 30.0:
    print('SobrePeso.')
elif 30.0 <= imc < 40.0:
    print('Obesidade.')
else:
    print('Obesidade mórbida.')
