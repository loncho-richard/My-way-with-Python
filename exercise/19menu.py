import os
num1=10
num2=5
while True:
    print(f"Que queres realizar con estos numeros {num1} y {num2}\n\
Presiona m para multiplicar\n\
Presiona d para dividir\n\
Presiona s para sumar\n\
Presiona r para restar\n\
Presiona x para salir")
    opcion=input()
    if opcion=="m":
        print(f"Este es el resultado de tu multiplicacion {num1*num2}")
    elif opcion=="d":
        print(f"Este es el resultado de tu divicion {num1/num2}")
    elif opcion=="s":
        print(f"Este es el resultado de tu suma {num1+num2}")
    elif opcion=="r":
        print(f"Este es el resultado de tu resta {num1-num2}")
    elif opcion=="x":
        break
    input()
    os.system("cls")