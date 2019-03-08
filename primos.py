

#PROGRAMA PRIMO

x=int(input("Introduzca un Numero: "))
cont=0
for i in range(2,x):
    if x%i==0:
        cont=cont+1
        print("Divisor",i)

if cont>0:
    print("No son primos")
else:
    print("El numero es primo")
