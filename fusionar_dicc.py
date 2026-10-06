dicc1 = {"a": 10, "b": 5}
dicc2 = {"b": 3, "c": 7}

def fusionar(diccionario1, diccionario2):
    for clave, valor in diccionario2.items():
        if clave in diccionario1:
            diccionario1[clave] += valor
        else:
            diccionario1[clave] = valor
            
    return diccionario1
    
print(fusionar(dicc1, dicc2))