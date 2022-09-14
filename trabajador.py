from calendar import c
from lib2to3.pgen2.pgen import generate_grammar
import sqlite3
from datetime import date
from random import randint
from tkinter import messagebox as mb
from xlsxwriter.workbook import Workbook

class Trabajador:
    
    def insertarTrabajador(rut, DV, nombre, apellidoPaterno, apellidoMaterno, titulo):
        
        conexion = sqlite3.connect("db1.db")
        cursor = conexion.cursor()
        fechaNacimiento = generarFechaNacimiento()
        cursor.execute("INSERT INTO trabajadores(rut, DV, nombres, apellido_paterno, apellido_materno, fecha_nacimiento, titulo, direccion, correo, telefono) "+
        "VALUES(?,?,?,?,?,?,?,?,?,?)", (rut, DV, nombre, apellidoPaterno, apellidoMaterno, fechaNacimiento, titulo, "", "", ""))
        conexion.commit()
        conexion.close()

    def MostrarTrabajadores(self):
        conexion = sqlite3.connect("db1.db")
        cursor = conexion.execute("SELECT rut , direccion, correo, telefono FROM Trabajadores")
        return cursor.fetchall()


def generarFechaNacimiento():
    fechaInicio = date.today().replace(day = 1, month = 1).toordinal()
    fechaFinal = date.today().toordinal()

    fecha = date.fromordinal(randint(fechaInicio, fechaFinal))

    return fecha

def exportarTrabajadores():
    conexion = sqlite3.connect("db1.db")
    cursor = conexion.cursor()
        
    trabajadores = cursor.execute('select * from trabajadores')
    if trabajadores.rowcount == 0:
        mb.showerror("Trabajadores", "No existen trabajadores en el sistema")
        return

    workbook = Workbook("trabajadores.xlsx")
    worksheet = workbook.add_worksheet()
    for i, row in enumerate(trabajadores):
        for j, value in enumerate(row):
            worksheet.write(i, j, row[j])

    workbook.close()
    
    