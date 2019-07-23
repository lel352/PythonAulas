# Aula  Módulos e Pacotes

# Modulos
import Uteis

numero = int(input("Digite um valor: "))
fatorial = Uteis.fatorial(numero)
print(f"O fatorial de {numero} é {fatorial}")
print(f"O dobro de {numero} é {Uteis.dobro(numero)}")
print(f"O Triplo de {numero} é {Uteis.triplo(numero)}")


# Pacotes
from uteispacote import numeros

numero = int(input("Digite um valor: "))
numeros.fatorial = numeros.fatorial(numero)
print(f"O fatorial de {numero} é {fatorial}")
print(f"O dobro de {numero} é {numeros.dobro(numero)}")
print(f"O Triplo de {numero} é {numeros.triplo(numero)}")



