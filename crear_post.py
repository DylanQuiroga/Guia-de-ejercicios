import requests
import json

def crear_post(titulo, cuerpo, user_id):
    datos = {
        "userId": user_id,
        "title": titulo,
        "body": cuerpo
    }
    
    json_post = json.dumps(datos, indent=4)
    
    url = "https://jsonplaceholder.typicode.com/posts"
    
    respuesta = requests.post(url, data=json_post)
    
    if respuesta.status_code == 201:
        print("Creado ", respuesta.json()["id"])
    else:
        print("Error")
        
crear_post("Hola", "Mi primer post", 1)