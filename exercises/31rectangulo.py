class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho=ancho
        self.alto=alto
    
    def area(self):
        area=self.ancho*self.alto
        return area

    def perimetro(self):
        perimetro=(self.ancho*2)+(self.alto*2)
        return perimetro
r1=Rectangulo(4,2)
area=r1.area()
perimetro=r1.perimetro()
print(f"El area es: {area}")
print(f"El perimetro es: {perimetro}")