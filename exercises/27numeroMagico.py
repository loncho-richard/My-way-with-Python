from ast import Expression
import random
contador=1
aleatorio=int(random.random()*100)
while True:
    numero=int(input("Ingresa el numero que estoy pensando entre el 1 y el 100: "))
    if numero<aleatorio:
        print(f"Ese no es el numero que estoy pensando, el numero {numero} es menor")
    elif numero>aleatorio:
        print(f"Ese no es el numero que estoy pensando, el numero {numero} es mayor")
    if numero==aleatorio:
        print(f"Felicidades, acertaste con el numero: {numero} en {contador} intentos")
        break
    contador=contador+1