
import math

numero = int(input("Digite un numero: "))

while numero<0:
    print("Error -> Ingrese un numero positivo")
    numero = int(input("Digite un numero: "))

print(f"\nSu raiz Cuadrada es: {(math.sqrt(numero)):.2f}")