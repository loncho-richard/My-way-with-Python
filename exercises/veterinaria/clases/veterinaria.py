import os as os
database={
    "Perro":[],
    "Gato":[],
    "Ave":[],
    "Hamster":[]
}
'''
databasePerro=[]
databaseGato=[]
databaseAve=[]
databaseHamster=[]
'''
class Mascota:
    def __init__(self,name,old,_type):
        self.name=name
        self.old=old
        self._type=_type
    @classmethod
    def entrada_mascota(self,name,_type):
        """
        Entrada de la mascota a la lista, dependiendo del tipo animal, va a ser la lista

        Args:
            self: el objeto mismo
            name: nombre del animal
            _type: tipo de animal
        """
        if _type=="perro":
            database['Perro'].append(name)
        elif _type=="gato":
            database['Gato'].append(name)
        elif _type=="ave":
            database['Ave'].append(name)
        elif _type=="hamster":
            database['Hamster'].append(name)

    @classmethod
    def salida_mascota(self,name,_type):
        """
        Salida de la mascota a la lista, dependiendo del tipo animal, sale del al lista en donde esta

        Args:
            self: el objeto mismo
            name: nombre del animal
            _type: tipo de animal
        """
        if _type=="perro":
            database['Perro'].remove(name)
        elif _type=="gato":
            database['Gato'].remove(name)
        elif _type=="ave":
            database['Ave'].remove(name)
        elif _type=="hamster":
            database['Hamster'].remove(name)
        
'''
perro1=Mascota("Tino",4,"perro")
while True:
    #print("______________")
    opcion=int(input("Sistema de adopcion de veterinaria:\n1- Dar una mascota en adopcion.\n2- Adoptar una mascota.\n0- Salir\n"))
    if opcion==1:
        input(Mascota(str(input("Ingresa el nombre:\n")),int(input("Ingresa la edad:\n")),str(input("Ingresa el tipo de animal:"))))
        os.system("cls")
    elif opcion==2:
        Mascota.salida_mascota(input())
        os.system("cls")
    elif opcion==0:
        break  
'''
'''
perro1=Mascota("Tino",4,"perro")
perro2=Mascota("Ciro",3,"perro")
perro3=Mascota("Choco",5,"perro")
hamster1=Mascota("Chewi",1,"hamster")
gato1=Mascota("Michi",2,"gato")
ave1=Mascota("Rio",1,"ave")

Mascota.entrada_mascota(perro1.name,perro1._type)
Mascota.entrada_mascota(perro2.name,perro2._type)
Mascota.entrada_mascota(perro3.name,perro3._type)
Mascota.entrada_mascota(gato1.name,gato1._type)
Mascota.entrada_mascota(hamster1.name,hamster1._type)
Mascota.entrada_mascota(ave1.name,ave1._type)
print("---------")
print("Perros:",database['Perro'],"\nGatos:",database['Gato'],"\nAves:",database['Ave'],"\nHamsters:",database['Hamster'])
Mascota.salida_mascota(gato1.name,gato1._type)
Mascota.salida_mascota(perro2.name,perro2._type)
print("---------")
print("Perros:",database['Perro'],"\nGatos:",database['Gato'],"\nAves:",database['Ave'],"\nHamsters:",database['Hamster'])


perro=Mascota("poli",8,"perro")

Mascota.entrada_mascota("poli","perro")

print(database)

Mascota.salida_mascota("poli","perro")

print(database)

'''