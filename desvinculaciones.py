from tkinter import *
import csv
import sqlite3
from tkinter import filedialog
from typing import List, Tuple 
from tkinter import messagebox as mb
from xlsxwriter.workbook import Workbook



class Desvinculaciones:
    def cargarDesvinculaciones():
        try:
             filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", 
             filetypes = (("Text files","*.csv*"),("all files","*.*")))

             conexion = sqlite3.connect("db1.db")
             cursor = conexion.cursor()

             with open(filename) as data:
              reader = csv.DictReader(data, delimiter=";", skipinitialspace = True)
              for n, r in enumerate(reader):
                 t = tuple(r.values())
                 rut = verificarDesvinculaciones(t[5], conexion)
                 if rut == True:
                  cursor.execute("INSERT INTO Desvinculaciones(RUT, DV, NOMBRES, APELLIDO_PATERNO, APELLIDO_MATERNO, NUMERO_CONTRATO, FECHA_DESVINCULACION, CAUSAL) "+
                  "VALUES (?, ?, ?, ?, ?, ?, ?, ?);", t)
                  conexion.commit()
                 else:
                    mb.showerror("Desvinculaciones", "No existen contratos en el sistema que esten anexados a las desvinculaciones")
                    return
             
             row = cursor.execute("select * from Desvinculaciones")
             if row.fetchall() == None:
                mb.showerror("desvinculaciones", "hubo un error al cargar las desvinculaciones")
             else:
                mb.showinfo("Desvinculaciones", "Las desvinculaciones fueron cargadas exitosamente")
                
        except sqlite3.IntegrityError:
            mb.showerror("Desvinculaciones", "Las desvinculaciones que intenta subir ya existen en el sistema")
        except sqlite3.ProgrammingError:
            mb.showerror("Desvinculaciones","Los datos que intenta subir no son validos")


def verificarDesvinculaciones(numeroContrato, conexion):
     trabajador = conexion.cursor()
     fila = trabajador.execute("SELECT NUMERO_CONTRATO FROM contrataciones WHERE NUMERO_CONTRATO = ?", (numeroContrato,))
     if trabajador.fetchone() == None:
        return False
     else:
        return True

def exportarDesvinculaciones():
    conexion = sqlite3.connect("db1.db")
    cursor = conexion.cursor()
    desvinculaciones = cursor.execute("SELECT * FROM Desvinculaciones")
    if desvinculaciones.rowcount == 0:
        mb.showerror("Desvinculaciones", "No existen Desvinculaciones en el sistema")
        return
    
    workbook = Workbook("desvinculaciones.xlsx")
    worksheet = workbook.add_worksheet()
    for i, row in enumerate(desvinculaciones):
        for j, value in enumerate(row):
            worksheet.write(i, j, row[j])

    workbook.close()

    
