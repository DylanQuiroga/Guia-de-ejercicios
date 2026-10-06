texto = "Anita lava la tina"

def palindromo(texto):
    texto = texto.lower()
    texto = texto.replace(" ", "")
    
    inicio = 0
    final= len(texto) - 1
    
    while inicio < final:
        if texto[inicio] != texto[final] :
            return False
        
        inicio += 1
        final -= 1
        
    return True
    
print(palindromo(texto))