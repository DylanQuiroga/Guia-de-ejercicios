import unicodedata

texto = "Programación en Python"
conteo = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

def quitar_tildes(texto):
    # Descompone los caracteres acentuados en letra + tilde
    nfd = unicodedata.normalize('NFD', texto)
    # Filtra solo los caracteres que no sean marcas de tilde (Mn)
    sin_diacriticos = [c for c in nfd if unicodedata.category(c) != 'Mn']
    return "".join(sin_diacriticos)

def contar(texto):
    texto = texto.lower()
    texto = quitar_tildes(texto)
    
    for letra in texto:
        if letra in conteo:
            conteo[letra] += 1

    return conteo

print(contar(texto))
