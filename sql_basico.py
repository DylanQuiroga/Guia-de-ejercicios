import sqlite3

conexion = sqlite3.connect(":memory:")
cursor = conexion.cursor()

cursor.execute("CREATE TABLE personas (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, edad INTEGER, ciudad TEXT)")

datos_json = [
    {"nombre": "Ana", "edad": 28, "ciudad": "Coquimbo"},
    {"nombre": "Carlos", "edad": 34, "ciudad": "La Serena"},
    {"nombre": "Juan", "edad": 20, "ciudad": "La Serena"},
    {"nombre": "Sofia", "edad": 40, "ciudad": "Ovalle"},
    {"nombre": "Pedro", "edad": 32, "ciudad": "Coquimbo"},
    {"nombre": "Sebastian", "edad": 54, "ciudad": "Coquimbo"},
]

for item in datos_json:
    cursor.execute("""
    INSERT INTO personas (nombre, edad, ciudad) 
    VALUES (?, ?, ?)""", 
    (item["nombre"], item["edad"], item["ciudad"]),
    )
    
conexion.commit()

# Personas mayores de 30 años
edad_limite = 30
cursor.execute("SELECT * FROM personas WHERE edad >= ? ORDER BY edad ASC", (edad_limite,))
resultados = cursor.fetchall()
for fila in resultados:
    print(fila[1], fila[2])
    
print("------")
    
# Cantidad de personas por ciudad
cursor.execute("SELECT ciudad, COUNT(id) FROM personas GROUP by ciudad")
resultados = cursor.fetchall()
for fila in resultados:
    print(f"{fila[0]} -> {fila[1]}")
    
print("------")

# Edad promedio
cursor.execute("SELECT ROUND(AVG(edad), 2)FROM personas")
resultados = cursor.fetchone()
print(resultados[0])

print("------")

# La persona más joven
cursor.execute("SELECT MIN(edad) from personas")
resultados = cursor.fetchone()
print(resultados[0])
    
conexion.close()    