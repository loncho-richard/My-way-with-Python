'''
- Crear una función que muestre una lista de números.
- El resultado debe ser más o menos asi 1 1 2 3 5 8 13 21 34...n
'''
#- Crear una función que pida un número mayor a 1 al humano.
def pideNumero():
    while True:    
        num=int(input("Ingresa un numero que sea mayor a 1: "))
        if num>1:
            return num

#- Crear una función que genere una lista fibonacci desde 1 hasta un número x.
def listaFibonacci(num):
    lista=[]
    for i in range(0,num):
        if i==0 or i==1:
            lista.append(1)
        else:
            lista.append(lista[-2]+lista[-1])
    return lista

#- Crear una función que muestre una lista de números.
def printLista(lista):
    for i in lista:
        if(i!=lista[-1]):
            print(f"{i}", end="+")
        else:
            print(f"{i}")

num=pideNumero()
#genera una sucecion fibonacci
lista=listaFibonacci(num)
printLista(lista)