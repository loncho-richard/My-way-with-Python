while True:
    n=int(input("Ingresa un numero mayor a 1: "))
    if n>1:
        break
    else:
        print("Te pedi que ingresaras un numero mayor a 1")
factorial=1
strResultado=""
for i in range(1,n+1):
    factorial=factorial*i
    strResultado=strResultado+str(i)+"*"
strResultado=strResultado[:-1]
strResultado=strResultado+"="
print(f"{strResultado} {factorial}")
print(f"Aqui esta tu factorial {factorial}")