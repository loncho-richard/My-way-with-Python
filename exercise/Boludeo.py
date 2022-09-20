print("es es un boluedeo mas que nada para probar como es la experiencia del programado")
print("Viendo que es buena vamos a hacer un programa en que podamos interactuar con las listas")
print("SI queremos agregar a pepito en una lista hay que introducir su nombre")
lista=[]
while True:
    name = str(input("Intoduce el name de pepito: "))
    opcion = str(input("Que quiere hacer con el?, agregarlo a la lista?"))
    if opcion == "si":
        lista.append(name)
    elif opcion == "no":
        break

    print(lista)