#absoluta="C:\\Users\\carlo\\OneDrive\\workspace\\python\\My-way-with-Python\\theory\\archivo\\hola.txt"
relativa="theory\\archivo\\hola.txt"
archivo=open(relativa,"r")
#print(archivo.read())
#print(archivo.readline())
#
#for linea in archivo.readlines():
#    print(linea)

#ESCRITURA

#relativa2="theory\\archivo\\hola2.txt"
#archivo2=open(relativa2, "w")
#archivo2.write("C#\nVB.net\nASP.net")

#ESCRITURA - LECTURA

relativa3 = "theory\\archivo\\hola3.txt"
archivo3 = open(relativa3, "r+")
archivo3.write("Hola\nComo\nEstas")
archivo3.seek(0)
print(archivo3.read())