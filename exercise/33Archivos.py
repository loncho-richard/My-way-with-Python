#archivo=open("..\\My-way-with-Python\\theory\\archivo\\personas.txt", encoding="utf8")
archivo=open("..\\My-way-with-Python\\theory\\archivo\\personas.txt", "r+")
#archivo=open("C:\\Users\\carlo\\OneDrive\\workspace\\python\\My-way-with-Python\\theory\\archivo\\personas.txt")
lineas=archivo.readlines()
#archivo.close()
personas=[]

for linea in lineas:
    campo=linea.replace("\n","").split(";")
    persona={"id":campo[0], "nombre":campo[1], "apellido":campo[2], "nacimiento":campo[3]}
    personas.append(persona)

for persona in personas:
    print(f"id={persona['id']} {persona['nombre']} {persona['apellido']} {persona['nacimiento']}")