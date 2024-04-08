def insertarNumero():
    lista=[]
    while True:
        num=int(input("Porfavor ingresa un numero (Presiona 0 para terminar)"))
        if num==0:
            return lista
        else:
            lista.append(num)

def ordenPorInsercion(lista):
    pos=0
    i=0
    aux=0
    for _ in lista:
        pos=i
        aux=lista[i]
        while pos>0 and lista[pos-1]>aux:
            lista[pos]=lista[pos-1]
            pos=pos-1
        lista[pos]=aux
        i=i+1
    return lista

def mostrarLista(lista):
    for numero in lista:
        print(numero)

lista=insertarNumero()
lista=ordenPorInsercion(lista)
print("Aqui esta tu lista ordenada:")
mostrarLista(lista)
