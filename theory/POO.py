class Auto:
    #atributos publicos(generales)
    encendido=False
    velocidad=0
    alto="1.5"
    ancho=2.3
    velocidadMax=100
    #metodos
    def __init__(self,llave,color,modelo,marca):
        self.__llave=llave
        self.color=color
        self.modelo=modelo
        self.marca=marca
    def encender(self,llave):
        if self.__llave==llave:
            self.encendido=True
            print("El auto esta encendido")
        else:
            print("Esa no es la llave") 
    def acelera(self):
        if self.encendido==True:
            if self.velocidad<self.velocidadMax:
                self.velocidad=self.velocidad+10
    def frena(self):
        if self.velocidad>0:
            self.velocidad=self.velocidad-10
            self.__enciendeLuzFreno()
    def apaga(self):
        if self.encendido==True:
            self.encendido=False
            self.velocidad=0
            self.corneta(True)
    #metodos privados
    def __enciendeLuzFreno(self):
        print("Luz del freno encendida")
    @staticmethod
    def corneta(precionar=False):
        if precionar==True:
            print("la corneta suena")
        else:
            print("la corneta no suena")
    @classmethod
    def canasta(cls,peso):
        pesoMax=cls.ancho*10
        if peso<pesoMax:
            return True
        else:
            return False
#print("La canasta del auto soporta 20KG?", Auto.canasta(20))

autito=Auto("LL123", "Rojo", "2021", "vocho")
print("La canasta del autito soporta 20KG?", autito.canasta(20))

'''         
print(Auto.alto)
print(Auto.ancho)
print(Auto.velocidadMax)

autito=Auto("LL123", "Rojo", "2021", "vocho")
autito.encender("LL123")
autito.acelera()
autito.acelera()
print("Endendido=",autito.encendido," Velocidad=",autito.velocidad)

'''
'''
vocho1=Auto("LL123", "Blanco", "2010", "Vocho")
vocho1.encender("LL123")
vocho1.acelera()
vocho1.acelera()
vocho1.acelera()
print("Endendido=",vocho1.encendido," Velocidad=",vocho1.velocidad)

vocho2=Auto("LL111", "Azul", "2009", "Vocho")
vocho2.encender("123")
vocho2.acelera()
vocho2.acelera()
vocho2.acelera()
print("Endendido=",vocho2.encendido," Velocidad=",vocho2.velocidad)



vocho1.encender("123456")
print("Endendido=",vocho1.encendido," Velocidad=",vocho1.velocidad)
vocho1.acelera()
vocho1.frena()
'''