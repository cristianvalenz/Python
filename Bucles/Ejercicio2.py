
lista = list(range(1,11))


for i in lista:
    print(i,end="-")

multi = int(input("\nDigite el numero a Multiplicar : "))

resultado = 0
for i in lista:
    lista[resultado] *= multi
    resultado +=1

print(f"\nLista final con los elementos multiplicados por {multi}")

for i in lista:
    print(i,end="-")