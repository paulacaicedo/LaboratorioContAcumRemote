

#PROGRAMA PRIMO



x=int(input("Introduzca un Numero: "))

for i in range(1,x+1,1):
    res=x%i
    print("El residuo entre ",x," y ",i," es: ",res)

