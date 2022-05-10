class Person:
    def __init__(self,name,old):
        self.name=name
        self.old=old
    def showname(self):
        print("El nombre de la persona es",self.name)
class Encargado:
    def __init__(self,codeEncargado,departament):
        self.codeEncargado=codeEncargado
        self.departament=departament
class StudentEncargado(Person,Encargado):
    def __init__(self,name,old,password,notes,codeEncargado,departament):
        Person.__init__(self,name,old)
        Encargado.__init__(self,codeEncargado,departament)
        self.password=password
        self.notes=notes
        self.codeEncargado=codeEncargado
        self.departament=departament
    def showname(self):
        print("El nombre del student Encargado es",self.name)
class Student(Person):
    def __init__(self,name,old,password,notes):
        Person.__init__(self,name,old)
        self.password=password
        self.notes=notes

studentEncargado1=StudentEncargado("Juan", 22, "0232", 10, "0233", "Sistemas")
studentEncargado1.showname()
person1=Person("Juan",20)
person1.showname()
#print("Name:",studentEncargado1.name,"Departament:",studentEncargado1.departament)

'''
juan=Person("Juan",22)
print("Juan.old",juan.old)
maria=Student("Maria",23,"2222",10)
print("maria password",maria.password)
'''