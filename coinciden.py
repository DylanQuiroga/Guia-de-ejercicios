def coinciden(texto):
    pila = []
    pares = {')':'(' , ']':'[' , '}':'{'}
    
    for caracter in texto:
        if caracter in pares.values():
            pila.append(caracter)
        elif caracter in pares.keys():
            if not pila or pila.pop() != pares[caracter]:
                return "NO"
    
    return "SI" if not pila else "NO"
    
print(coinciden("[({})]"))
print(coinciden("[({}]]"))