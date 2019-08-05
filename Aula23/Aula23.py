#Tratamento de Erros e Exceções

'''
print(x) Exceçao: NameError: name 'x' is not defined
n = int(input('Número: ')) #Exceçao: ValueError: invalid literal for int() with base 10: 'l'
print(f'Você digitou {n}')


a = int(input('Numerador: '))
b = int(input('Demonimador: '))
r = a / b
print(f'Resultado é {r}')#b=0 #Exceçao: ZeroDivisionError: division by zero

r = 2 / '2' #Exceçao: TypeError

lst = [2, 4, 5]
print(lst[3]) #Excecao: IndexError keyError

import uteis #Se não encontrar o modulo Excesao: moduleNotFoundError

#Algumas Exception Acima
'''

#Tratando as Exception
from builtins import print, KeyboardInterrupt
from typing import Type

try:
    a = int(input('Numerador: '))
    b = int(input('Demonimador: '))
    f = a / b
except (ValueError, TypeError):# Exception especifica
    print(f'Erro: Verifique os valores Informado são Numeros Inteiros !!!')
except ZeroDivisionError:
    print('Não é possível dividir por zero !!!')
except KeyboardInterrupt:
    print('Não foi informado os dados')
except Exception as erro: #Erro #versão generica
    print(f'Infelizmente tivemos um problema :( \n Erro: {erro.__class__}')
else:#opcional Deu certo
    print(f'Resultado é {f}')
finally: #opcional vai acontecer mesmo se der certo ou errad
    print('Volte sempre!!')




