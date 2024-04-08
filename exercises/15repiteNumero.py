'''
En este ejercicio le mostraremos una lista de números al humano y pediremos que ingrese un 
número y la cantidad de veces que ese número se repite.
Crearemos una tupla con números al azar y  se la mostraremos al humano.
Pediremos al humano que ingrese un numero de la tupla y nos diga cuantas veces se repite.
Si le atina felicitamos al humano.
En caso contrario reprendemos al humano.
'''

tupla=(1,2,4,2,5,6,7,8,15,2,3)
print(tupla)
numero=int(input("Ingresa un numero que este dentro de la tupla:"))
if numero in tupla:
    print(f"Cuantas veces se repite {numero} en la tupla?")
    repite=int(input())
    seRepiteEnLaTupla=tupla.count(numero)
    if repite==seRepiteEnLaTupla:
        print("Barbaro, esta bien")
    else:
        print(f"Erorr, el numero {numero} se repite {seRepiteEnLaTupla} en la tupla")
else:
    print(f"Salamin, el numero {numero} no esta dentro de la tupla")