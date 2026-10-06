lista = ["10", "abc", "7", "", "3.5"]

correcto = []
incorrecto = []

def convertirEntero(lista):
    for texto in lista:
        try:
            correcto.append(int(texto))
        except ValueError:
            incorrecto.append(texto)
            
convertirEntero(lista)
print("("+ str(correcto) + ", " + str(incorrecto))