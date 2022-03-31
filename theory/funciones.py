def suma(n1,n2):
    res=n1+n2
    print(f"El resultado es {res}")

def resta(n1,n2):
    res=n1-n2
    print(f"El resultado es {res}")

num1=10
num2=5

while True:
    print(f"Que deseas hacer con esos dos numeros {num1} y {num2}:\n\
    1.-Sumar\n\
    2.-Restar\n\
    3.-Salir") 
    opcion=input()
    if opcion=='1':
        suma(num1,num2)
    elif opcion=='2':
        resta(num1,num2)
    elif opcion=='3':
        break
    else:
        print("Tarado, eleji algun numero de estas opciones")



