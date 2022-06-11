'''
Paso 1: convertir la masa conocida del reactivo a moles.
Paso 2: utilizar la proporción molar para encontrar los moles del otro reactivo.
Paso 3: convertir moles de otros reactivos a masa.
'''

file = open("exercise\\Estequinometria\\archivos\\Datos_elementos.txt", "r")
lineas = file.readlines()

elementos = []

for linea in lineas:
    campo = linea.replace("\n","").split(";")
    elemento = {"n_atomico":campo[0], "elemento":campo[1], "masa_atomica":campo[2]}
    elementos.append(elemento)

file.close()

def read_elements():
    '''
    Lee todos los elementos de la base de datos
    '''
    for elemento in elementos:
        print(f"-Elemento= {elemento['elemento']} -N_Ato= {elemento['n_atomico']} -Masa= {elemento['masa_atomica']}")

def search_elements(element):
    '''
    La funcion busca un elemento dentro de la lista y muestra todas sus caracteristicas
    Args:
        element: elemento a buscar
    Return:
        Imprime los datos del elemento
    '''
    for elemento in elementos:
        if element == elemento['elemento']:
            return (f"-Elemento= {elemento['elemento']} -N_Ato= {elemento['n_atomico']} -Masa= {elemento['masa_atomica']}")

def search_weight(element):
    '''
    Busca el peso atomico de un elemento y lo retorna
    Args:
        element: Elemento a buscar
    Return:
        devuelve el peso del elemento
    '''
    for elemento in elementos:
        if element == elemento['elemento']:
            value_element = str(elemento['masa_atomica'])
            return int(value_element)

def elements_weight(element,amount_element):
    '''
    Multiplica el peso del elemento por la cantidad de ese mismo elemento
    Args;
        element: elemento a buscar
        amount_element: cantidad del elemento
    Return:
        devuelve el peso total en gramos 
    '''
    value_element = search_weight(element)
    weight = value_element * int(amount_element)
    return int(weight)

def sum_of_two_elements():
    '''
    suma todos los elementos en gramos (2)
    '''
    print("-----")
    element1 = elements_weight(str(input("Ingresa primer el elemento: ")), int(input("Ingresa la cantidad: ")))
    print("-----")
    element2 = elements_weight(str(input("Ingresa segundo elemento: ")), int(input("Ingresa la cantidad: ")))
    print("-----")
    return element1 + element2

def sum_of_three_elements():
    '''
    suma todos los elementos en gramos (3)
    '''
    print("-----")
    element1 = elements_weight(str(input("Ingresa el primer elemento: ")), int(input("Ingresa la cantidad: ")))
    print("-----")
    element2 = elements_weight(str(input("Ingresa el segundo elemento: ")), int(input("Ingresa la cantidad: ")))
    print("-----")
    element3 = elements_weight(str(input("Ingresa el tercer elemento: ")), int(input("Ingresa la cantidad: ")))
    print("-----")
    return element1 + element2 + element3

def sum_of_four_elements():
    '''
    suma todos los elementos en gramos (4)
    '''
    print("-----")
    element1 = elements_weight(str(input("Ingresa el primer elemento: ")), int(input("Ingresa la cantidad: ")))
    print("-----")
    element2 = elements_weight(str(input("Ingresa el segundo elemento: ")), int(input("Ingresa la cantidad: ")))
    print("-----")
    element3 = elements_weight(str(input("Ingresa el tercer elemento: ")), int(input("Ingresa la cantidad: ")))
    print("-----")
    element4 = elements_weight(str(input("Ingresa el cuerto elemento: ")), int(input("Ingresa la cantidad: ")))
    print("-----")
    return element1 + element2 + element3 + element4