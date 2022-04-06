import Modulos.humano as humano

def busquedaSecuencial(num,lista):
    for i in range(0,len(lista)):
        if num==lista[i]:
            return True
    return False
lista=[1,2,3,4,5]
while True:
    num=humano.pedirNumero(lista)
    encontrado=busquedaSecuencial(num,lista)
    if encontrado==True:
        print("Has encontrado un numero de la lista")
        break
    else:
        print("Intentalo de nuevo")