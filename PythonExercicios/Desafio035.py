print('=========Desafio 035========')
reta1 = float(input('Reta 1: '))
reta2 = float(input('Reta 2: '))
reta3 = float(input('Reta 3: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Pode forma um triangulo')
else:
    print('Não pode forma um triangulo')
'''
if ((reta2 - reta3) < reta1) and ((reta2 + reta3) > reta1):
    if ((reta1 - reta3) < reta2) and ((reta1 + reta3) > reta2):
    if ((reta1 - reta3) < reta2) and ((reta1 + reta3) > reta2):
        if ((reta1 - reta2) < reta3) and ((reta1 + reta2) > reta3):
            print('Pode forma um triangulo')
        else:
            print('Não pode forma um triangulo')
    else:
        print('Não pode forma um triangulo')
else:
    print('Não pode forma um triangulo')
'''
