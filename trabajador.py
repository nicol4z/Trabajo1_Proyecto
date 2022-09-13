from lib2to3.pgen2.pgen import generate_grammar
import sqlite3
from datetime import date
from random import randint


class Trabajador:
    
    def insertarTrabajador(rut, DV, nombre, apellidoPaterno, apellidoMaterno, titulo):
        
        conexion = sqlite3.connect("db1.db")
        cursor = conexion.cursor()
        fechaNacimiento = generarFechaNacimiento()
        cursor.execute("INSERT INTO trabajadores(rut, DV, nombres, apellido_paterno, apellido_materno, fecha_nacimiento, titulo, direccion, correo, telefono) "+
        "VALUES(?,?,?,?,?,?,?,?,?,?)", (rut, DV, nombre, apellidoPaterno, apellidoMaterno, fechaNacimiento, titulo, "", "", ""))
        conexion.commit()
        conexion.close()

def generarFechaNacimiento():
    fechaInicio = date.today().replace(day = 1, month = 1).toordinal()
    fechaFinal = date.today().toordinal()

    fecha = date.fromordinal(randint(fechaInicio, fechaFinal))

    return fecha
