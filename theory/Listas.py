'''
Primer elemento
Último elemento
Un elemento que no está en la lista.
Rango del primero al tercero.
Rango del tercero al último.
'''

lista=[
    "Hola",
    "como",
    "estas",
    1,
    2,
    3.333,
    [
        4,5,6
    ]
]
#print(lista)
print("Primer elemento:", lista[0])
print("Ultimo elemento:", lista[-1])
#print("Un elemento que no este en la lista", lista[9])
print("Rango del primero al tercero:", lista[0:3])
print("Rango del tercero al ultimo:", lista[2:])