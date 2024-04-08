def suma():
    n1 = int(input("Ingresa el primer numero:"))
    n2 = int(input("Ingresa el segundo numero:"))
    return n1 + n2
def resta():
    n1 = int(input("Ingresa el primer numero:"))
    n2 = int(input("Ingresa el segundo numero:"))
    return n1 - n2
def multi():
    n1 = int(input("Ingresa el primer numero:"))
    n2 = int(input("Ingresa el segundo numero:"))
    return n1 * n2
def div():
    n1 = int(input("Ingresa el primer numero:"))
    n2 = int(input("Ingresa el segundo numero:"))
    return n1 / n2

print("Que deseas hacer?\n\
    1. sumar\n\
    2. restar\n\
    3. multiplicar\n\
    4. dividir")
opcion = int(input())

if opcion == 1:
    print(suma())
elif opcion == 2:
    print(resta())
elif opcion == 3:
    print(multi())
elif opcion == 4:
    print(div())
else:
    print("no existe esa opcion")

'''

n1 = int(input("Ingresa el primer numero:"))
n2 = int(input("Ingresa el segundo numero:"))
print("Que deseas hacer?\n\
    1. sumar\n\
    2. restar\n\
    3. multiplicar\n\
    4. dividir")

opcion = int(input())

if opcion == 1:
    print(n1 + n2)
elif opcion == 2:
    print(n1 - n2)
elif opcion == 3:
    print(n1 * n2)
elif opcion == 4:
    print(n1 / n2)
else:
    print("Esa opcion no es valida")

n1=float(input("ingrese un número: "))
n2=float(input("ingrese un número: "))

operacion= int(input("ingrese una operación \n\
    1. suma\n\
    2. resta\n\
    3. multiplicación\n\
    4. división"))

if(operacion == 1):
    print(n1+n2)
elif(operacion == 2):
    print(n1-n2)
elif(operacion == 3):
    print(n1*n2)
elif(operacion == 4):
    print(n1/n2)
else:
    print("OPERACION INVALIDA")
'''