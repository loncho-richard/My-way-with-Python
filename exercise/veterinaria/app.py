import clases.veterinaria as vet
import os as os
'''
perro1=vet.Mascota("Tino",5,"perro")

vet.Mascota.entrada_mascota(perro1.name,perro1._type)
print(vet.database)
'''
while True:
    #print("______________")
    opcion=int(input("Sistema de adopcion de veterinaria:\n1- Dar una mascota en adopcion.\n2- Adoptar una mascota.\n0- Salir\n"))
    if opcion==1:
        #hol=vet.Mascota(str(input("Ingresa el nombre:\n")),int(input("Ingresa la edad:\n")),str(input("Ingresa el tipo de animal:")))
        vet.Mascota.entrada_mascota(input("Ingresa el nombre: "),input("Ingresa el tipo: "))
        os.system("cls")
        print(vet.database)
        input()
    elif opcion==2:
        vet.Mascota.salida_mascota(input("Nombre: "),input("Tipo: "))
        os.system("cls")
        print(vet.database)
        input()
    elif opcion==0:
        break