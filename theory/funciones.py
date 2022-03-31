def suma(n1,n2):
    res=n1+n2
    return float(res)

def resta(n1,n2):
    res=n1-n2
    return str(res)

num1=10
num2=5

while True:
    print(f"Que deseas hacer con esos dos numeros {num1} y {num2}:\n\
    1.-Sumar\n\
    2.-Restar\n\
    3.-Salir") 
    opcion=input()
    if opcion=='1':
        res=suma(num1,num2)
        print(f"El resultado es {res} tipo: {type(res)}")
    elif opcion=='2':
        res=resta(num1,num2)
        print(f"El resultado es {res} tipo: {type(res)}")
    elif opcion=='3':
        break
    else:
        print("Tarado, eleji algun numero de estas opciones")