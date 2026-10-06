personas = {"Juan": 25, "María": 32, "Pedro": 40}
lista = []

def mayores(personas):
    for nombre, edad in personas.items():
        if edad >= 30:
            lista.append(nombre)
            
mayores(personas)
print(lista)