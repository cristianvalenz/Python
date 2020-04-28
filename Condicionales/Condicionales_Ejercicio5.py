saldo = 1000

print("\t .:MENU:.")
print("1. Ingresar Dinero a la cuenta")
print("2. Retirar dinero a la cuenta")
print("3. Mostrar dinero disponible")
print("4. Salir")

opcion = int(input("Digite una opcion : "))

print()

if opcion ==1:
    extra = float(input("Cuanto Dinero Ingresara "))
    saldo += extra
    print(f"El dinero de la cuenta es {saldo}")
elif opcion ==2:
    extra = float(input("Cuanto desea retirar "))
    if extra>saldo:
        print("No tiene esa cantidad de dinero")
    else:
        saldo-=extra
        print(f"Su saldo es {saldo}")
elif opcion == 3:
    print(f"Su saldo es {saldo}")
elif opcion == 4:
    print(f"Salio de la transaccion")
else:
    print("error")
