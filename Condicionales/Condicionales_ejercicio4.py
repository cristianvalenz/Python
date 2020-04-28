numero1 = float(input("Digite un numero : "))
numero2 = float(input("Digite un numero : "))

operacion = input("Digite la operacion : ").upper()

if operacion=='S':
    suma = numero1 + numero2
    print(f"La suma es {suma}")
elif operacion=='R':
    resta = numero1 - numero2
    print(f"La resta es {resta}")
elif operacion =='M' or operacion =='P':
    multi = numero1 * numero2
    print(f"La Multiplicacion es {multi:.2f}")
elif operacion =='D':
    div = numero1/numero2
    print(f"La Divicion es {div:.2f}")
else:
    print("No es ua operacion")