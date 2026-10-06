lista = []

def es_primo(n):
    if n < 2:
        return False
    # Verificamos divisibilidad hasta la raíz cuadrada de n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
    
def primo(numero):
    for num in range(numero):
        if es_primo(num):
            lista.append(num)

primo(10)
print(lista)