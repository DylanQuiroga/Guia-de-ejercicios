import sqlite3
import csv
import io

datos_csv = """nombre,precio,stock
Ana,990,5
Luis,1990,10
Carla,5990,20
Pedro,2990,3
"""

archivo_virtual = io.StringIO(datos_csv)
lector = csv.DictReader(archivo_virtual)

conexion = sqlite3.connect(":memory:")
cursor = conexion.cursor()

cursor.execute("""CREATE TABLE productos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT, precio INTEGER,
    stock INTEGER)""")

cursor.executemany("INSERT INTO productos(nombre, precio, stock) VALUES (:nombre, :precio, :stock)", lector)

conexion.commit()

cursor.execute("SELECT nombre, precio * stock AS valor FROM productos ORDER BY valor DESC LIMIT 3")
print(cursor.fetchall())