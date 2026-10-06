import csv
import io
import json

datos_csv = """nombre,edad,email
Ana,25,ana@gmail.com
Luis,abc,luis@gmail.com
Carla,22,carla.gmail.com
"""

dicc = {}
datos_json = []

archivo_virtual = io.StringIO(datos_csv)
lector = csv.DictReader(archivo_virtual)

for fila in lector:
    if "@" in fila["email"] and fila["edad"].isdigit():
        dicc.update({"nombre": fila["nombre"], "edad": fila["edad"], "email": fila["email"]})
        print(f"{fila} -> se guarda")
    else:
        print(f"{fila} -> se omite")
        
datos_json.append(dicc)
print(json.dumps(datos_json, indent=4, ensure_ascii=False))