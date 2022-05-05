class Auto:
    def __init__(self,matricula):
        self.__matricula=matricula
        
    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self,valor):
        self.__matricula=valor
'''
    def getmatricula(self):
        return self.__matricula
    def setmatricula(self,valor):
        self.__matricula=valor
'''
carro1=Auto("WWW")
print(carro1.matricula)
carro1.matricula="AAA"
print(carro1.matricula)
'''
carro1.setmatricula("AAA")
print(carro1.getmatricula())
'''