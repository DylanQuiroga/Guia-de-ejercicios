import requests
import json

def indicadores():
    url = "https://mindicador.cl/api"
    lista = {}
    
    response = requests.get(url)
    data = response.json()
    
    if response.ok:
        lista.update({"dolar": data["dolar"]["valor"], "euro": data["euro"]["valor"], "uf": data["uf"]["valor"]})
        return lista
    else:
        return lista
    
def convertir_clp_a_usb(monto):
    lista = indicadores()
    return round(monto / float(lista["dolar"]), 2)
    

print(convertir_clp_a_usb(100000))