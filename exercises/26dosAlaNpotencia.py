while True:
    n=int(input("Ingresa un numero meyor a 1: "))
    if n>1:
        break
    else:
        print("Error, intentalo de nuevo")
suma=0
for i in range(1,n+1):
    potencia=pow(2,i)
    suma=suma+potencia
    if i<n:
        print(f"2^{i}({potencia})", end=" + ")
    elif i==n:
        print(f"2^{i}({potencia})", end=" = ")
print(suma)