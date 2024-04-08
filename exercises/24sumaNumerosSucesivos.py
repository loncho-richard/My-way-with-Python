while True:
    n=int(input("Ingresa un numero que sea mayor a 1: "))
    if n>1:
        break
    else:
        print("Te dije que ingresaras un numero mayor a 1")
suma=0
strResultado=""
for i in range(1,n+1):
    suma=suma+i
    #print(f"{i}",end="+")
    strResultado=strResultado+str(i)+"+"
strResultado=strResultado[:-1]
strResultado=strResultado+"="
print(strResultado)
print(f"Aqui esta tu suma: {suma}")