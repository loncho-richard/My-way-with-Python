#para difereciar los conjuntos de los diccionarios se tiene que aplicar la funcion "set"
#conjuntos=set{} "conjunto"
diccionario={"python":1,"java":2,"javascript":3}
print(diccionario)
#muestra el tamanio del diccionario
print("len(diccionario)=", len(diccionario))
#indica el lugar que tiene "python"
print("diccionario['python']=",diccionario["python"])
#para agregar un elemento al diccionario
diccionario["C++"]=4
print("diccionario['C++']=4", diccionario)
diccionario["C++"]=5
print("diccionario['C++']=5", diccionario)
#eliminar un elemento
del(diccionario["C++"])
print("del(diccionario['C++'])=", diccionario)