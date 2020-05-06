

lista = []

#Agregamos en la lista los elementos del 1 al 50
i = 1

while i<=50:
    lista.append(i)
    i+=1
for i in lista:
    print(i,end="-")


#Seguna forma

lista = list(range(1,51))

for i in lista:
    print(i,end="-")