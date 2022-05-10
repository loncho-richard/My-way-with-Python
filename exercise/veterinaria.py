database=[]
class Mascota:
    def __init__(self,name,old,_type):
        self.name=name
        self.old=old
        self._type=_type
    @classmethod
    def entrada_mascota(self,name):
        database.append(name)
    @classmethod
    def salida_mascota(self,name):
        database.remove(name)
perro1=Mascota("Tino",4,"perro")
perro2=Mascota("Ciro",3,"perro")
print(database)
Mascota.entrada_mascota(perro1.name)
Mascota.entrada_mascota(perro2.name)
print(database)
Mascota.salida_mascota(perro2.name)
print(database)
#print(perro.name, perro.old, perro.type)
