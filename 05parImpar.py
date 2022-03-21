numero1=int(input("Ingresa un numero par: "))
numero2=int(input("Ingresa otro numero par: "))
numeroPar1=numero1%2
numeroPar2=numero2%2
if numeroPar1==0 and numeroPar2==0:
    print("Bien hecho, los numeros son pares")
else:
    print("Los dos numeros deberian ser pares")
    if numeroPar1!=0:
        print(f"El numero {numero1} no es par")
    else:
        print(f"El numero {numero1} si es par")
    if numeroPar2!=0:
        print(f"El numero {numero2} no es par")
    else:
        print(f"El numero {numero2} si es par")