import sqlite3
import index
try:
    conexion = sqlite3.connect("db1.db")
    print("conexion exitosa")

    cursor = conexion.execute("select rut from Trabajador")
    for fila in cursor:
        print(fila)
    

except sqlite3.OperationalError:
    print("No se pudo conectar a la base de datos")

index.saludar()
print("wena congpareeeee")