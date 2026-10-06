import requests

lista = []

def titulos_usuario(numero):
    url= "https://jsonplaceholder.typicode.com/posts?userId=" + str(numero)
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        datos = response.json()
        for data in datos:
            lista.append(data["title"])
        
    except requests.exceptions.HTTPError as error:
        print(error.response.status_code)
    
titulos_usuario(1)
print(lista)