import sqlite3

#try:
 #   conexion = sqlite3.connect("db1.db")

  #  cursor = conexion.execute("select rutt from contrataciones")

   # print("conexion exitosa")
    #for fila in cursor:
     #   print(fila)
    

#except sqlite3.OperationalError:
 #   print("No se pudo conectar a la base de datos")
conexion = sqlite3.connect("db1.db")
cursor = conexion.execute("select rutt from contrataciones")

print("conexion exitosa")
for fila in cursor:
    print(fila)
