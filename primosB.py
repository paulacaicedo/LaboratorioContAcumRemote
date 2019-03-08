

#x=int(input("Introduzca un Numero: "))
#cont=0
#y=2
#for i in range(2,x):
#    if x%i==0:
#        cont=cont+1
#        print("Divisor",i)
#if cont>0:
#   print("No son primos")
#else:
#    print("El numero es primo")

x=int(input("Introduzca un Numero: "))
cont=0
y=1
while y<=x:
    if x%y==0:
        print("Divisor",y)
        cont = cont + 1
    y = y + 1

if cont>2:
    print("No son primos")
else:
    print("El numero es primo")
