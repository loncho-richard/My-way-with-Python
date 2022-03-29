from configparser import DuplicateSectionError


for i in range(5):
    print("Numero",i)

print("-----------")

for i in [5,6,7]:
    print("Numero",i)

print("-----------")

for i in (5,6,7):
    print("Numero",i)

print("-----------")

diccionario={"Python":1,"Java":2,"Jacascript":3}

for lenguaje in diccionario:
    print(f"{lenguaje} -> {diccionario[lenguaje]}")

print("-----------")

for clave,valor in {"Python":1,"Java":2,"Jacascript":3}.items():
    print(f"{clave} -> {valor}")

print("-----------")

texto="Loncho"
for nashei in texto:
    print(f"Dame una: {nashei}")
print(f"Como dice: {texto}")