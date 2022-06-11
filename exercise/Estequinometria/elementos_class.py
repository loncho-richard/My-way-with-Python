import libreris.estequinometria as ass
file = open("exercise\\Estequinometria\\archivos\\Datos_elementos.txt", "r")
lineas = file.readlines()

elementos = []

for linea in lineas:
    campo = linea.replace("\n","").split(";")
    elemento = {"n_atomico":campo[0], "elemento":campo[1], "masa_atomica":campo[2]}
    elementos.append(elemento)

file.close()

class Elementos():
    def __init__(self, atomic_num, atomic_mass, symbol):
        self.atomic_num = atomic_num
        self.atomic_mass = atomic_mass
        self.symbol = symbol

ass.search_elements("O")