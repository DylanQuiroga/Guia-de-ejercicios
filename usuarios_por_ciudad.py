import requests
from collections import defaultdict


url = "https://jsonplaceholder.typicode.com/users"

def ciudad():
    dicc = defaultdict(list)
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        datos = response.json()
        
        for dato in datos:
            dicc[dato["address"]["city"]].append(dato["name"])
            
        return dicc
        
    except requests.exceptions.HTTPError as error:
        print(error.response.status_code)
        
print(ciudad())