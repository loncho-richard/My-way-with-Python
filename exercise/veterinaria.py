databasePerro=[]
databaseGato=[]
class Mascota:
    def __init__(self,name,old,_type):
        self.name=name
        self.old=old
        self._type=_type
    @classmethod
    def entrada_mascota(self,name,_type):
        if _type=="perro":
            databasePerro.append(name)
        elif _type=="gato":
            databaseGato.append(name)

    @classmethod
    def salida_mascota(self,name,_type):
        if _type=="perro":
            databasePerro.remove(name)
        elif _type=="gato":
            databaseGato.remove(name)


perro1=Mascota("Tino",4,"perro")
perro2=Mascota("Ciro",3,"perro")
perro3=Mascota("Choco",5,"perro")
gato1=Mascota("Michi",2,"gato")

print(databasePerro,databaseGato)
Mascota.entrada_mascota(perro1.name,perro1._type)
Mascota.entrada_mascota(perro2.name,perro2._type)
Mascota.entrada_mascota(perro3.name,perro3._type)
Mascota.entrada_mascota(gato1.name,gato1._type)
print("Perros:",databasePerro,"\nGatos:",databaseGato)
Mascota.salida_mascota(gato1.name,gato1._type)
Mascota.salida_mascota(perro2.name,perro2._type)
print("Perros:",databasePerro,"\nGatos:",databaseGato)

