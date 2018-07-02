print('=========Desafio 042========')
reta1 = float(input('Reta 1: '))
reta2 = float(input('Reta 2: '))
reta3 = float(input('Reta 3: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Pode formar um triangulo')
    if reta1 == reta2 == reta3: #reta1 == reta2 and reta1 == reta3
        print('É um triangulo Equilátero')
    elif reta1 != reta2 != reta3 != reta1: #reta1 != reta2 and reta1 != reta3 and reta2 != reta3
        print('É um triangulo Escaleno')
    else: #reta1 == reta2 != reta3 or reta1 == reta3 != reta2:
        print('É um triangulo Isósceles')
else:
    print('Não pode formar um triangulo')
