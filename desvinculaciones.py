from tkinter import *
import csv
import sqlite3
from tkinter import filedialog
from typing import List, Tuple 
from tkinter import messagebox as mb
import app

from trabajador import Trabajador

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

