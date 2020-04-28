numero1 = int(input("Ingrese un numero : "))
numero2 = int(input("Ingrese el segundo numero : "))

if numero1%2==0 and numero2%2==0:
    print("Ambos numeros son pares")
elif numero1%2==0 and numero2%2!=0:
    print(f"{numero1} es par")
elif numero1%2!=0 and numero2%2==0:
    print(f"{numero2} es par")
else:
    print("Ambos numeros impares")
    
