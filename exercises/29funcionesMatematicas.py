import os
def pedirNumero():
    a=int(input("Ingresa el primer numero: "))
    b=int(input("Ingresa el segundo numero: "))
    os.system("cls")
    return a,b

def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def menu(a,b):
    while True:
        print(f"Que tipo de operacion deseas realizar con {a} y {b}\n\
s para sumar\n\
r para restar\n\
m para multiplicar\n\
d para dividir\n\
x para salir")
        opcion=input()
        opcion=opcion.lower()
        if opcion=='s':
            print(f"El resultado es {suma(a,b)}")
        if opcion=='r':
            print(f"EL resultado es {resta(a,b)}")
        if opcion=='m':
            print(f"El resultado es {mul(a,b)}")
        if opcion=='d':
            print(f"El resultado es {div(a,b)}")
        if opcion=='x':
            break
        else:
            print("Error, no existe esa funcion")
        input("Presione cualquier tecla")
        os.system("cls")
a,b=pedirNumero()
menu(a,b)