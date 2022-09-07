from tkinter import *
import csv
import sqlite3
from tkinter import filedialog
from typing import List, Tuple 
  
class contrataciones:
    def cargarContrataciones(self):
        filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", 
        filetypes = (("Text files","*.csv*"),("all files","*.*"))) 

        archivo = csv.DictReader(filename, delimiter = ";", skipinitialspace = True)
        conexion = sqlite3.connect("db1.db")
        cursor = conexion.cursor()

        with open(filename) as data:
         reader = csv.DictReader(data, delimiter=";", skipinitialspace = True)
        for n, r in enumerate(reader):
         t = tuple(r.values())
         cursor.execute("INSERT INTO Contrataciones(RUT, DV, NOMBRES, APELLIDO_MATERNO, APELLIDO_PATERNO, JORNADA, PROYECTO, CARGO, INICIO_CONTRATO, TIPO_CONTRATO, DURACION, SUELDO) "+
        "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", t)
         conexion.commit()






