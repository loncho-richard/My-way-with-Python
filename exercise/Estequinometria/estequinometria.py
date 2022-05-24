'''
Paso 1: convertir la masa conocida del reactivo a moles.
Paso 2: utilizar la proporción molar para encontrar los moles del otro reactivo.
Paso 3: convertir moles de otros reactivos a masa.
'''

file=open("C:\\Users\\alfre\\OneDrive\\workspace\\My-way-with-Python\\exercise\\Estequinometria\\Datos_elementos.txt", "r")
lineas=file.readlines()

elementos=[]

for linea in lineas:
    campo=linea.replace("\n","").split(";")
    elemento={"n_atomico":campo[0], "elemento":campo[1], "masa_atomica":campo[2]}
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
        if element==elemento['elemento']:
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
        if element==elemento['elemento']:
            value_element=str(elemento['masa_atomica'])
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
    value_element=search_weight(element)
    weight=value_element*int(amount_element)
    return int(weight)

def sum_of_two_elements():
    '''
    suma todos los elementos en gramos
    '''
    element1=elements_weight(str(input("Ingresa el elemento: ")), int(input("Ingresa la cantidad: ")))
    element2=elements_weight(str(input("Ingresa el elemento: ")), int(input("Ingresa la cantidad: ")))
    return element1+element2


print(sum_of_two_elements())
#read_elements()
#print(search_weight(input("Ingresa un elemento: ")))
#print(elements_weight(input("Ingresa un elemento: "), input("Ingresa la cantidad del elemento: ")))