lista=[1,1,2,3]
print(lista)
#cuenta la cantidad de elementos dentro de una lista
print("len(lista)=", len(lista))
#se inserta un elemento al final de la lista
lista.append(4)
print("lista.append(4)=", lista)
#inserta un elemento a la lista donde se le indique
lista.insert(0,0)
print("lista.insert(0,0)=", lista)
#extiende la lista
lista.extend([5,6,7])
print("lista.extend([5,6,7])=", lista)
#suma una lista con otra
lista+=[8,9,10]
print("lista+=[8,9,10]=", lista)
#corrobora si un numero esta dentro de la lista
num=5
if num in lista:
    print(f"El numero {num} si esta dentro de la lista")
else:
    print(f"El numero {num} no esta dentro de lista")
#muestra el elemento que esta en el indicie especificado
print("lista.index(5)=", lista.index(5))
#cuenta cuantas veces
print("lista.count(1)=", lista.count(1))
#elimina un elemento seleccionado por indice de la lista
lista.pop(0)
print("lista.pop(0)=", lista)
#elemian un valor de la lista
lista.remove(5)
print("lista.remove(5)=", lista)
#te muestra la lista alreves 
lista.reverse()
print("lista.reverse()=", lista)
#al contrario del reverse te ordena la lista
lista.sort()
print("lista.sort=", lista)
#formatea la lista
lista.clear()
print("lista.clear()=", lista)