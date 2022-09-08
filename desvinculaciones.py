from tkinter import *
import csv
import sqlite3
from tkinter import filedialog
from typing import List, Tuple 


filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", 
filetypes = (("Text files","*.csv*"),("all files","*.*")))

#archivo = csv.DictReader(filename, delimiter = ";", skipinitialspace = True)
conexion = sqlite3.connect("db1.db")
cursor = conexion.cursor()

with open(filename) as data:
    reader = csv.DictReader(data, delimiter=";", skipinitialspace = True)
    for n, r in enumerate(reader):
        t = tuple(r.values())
        cursor.execute("INSERT INTO Desvinculaciones(RUT, DV, NOMBRES, APELLIDO_PATERNO, APELLIDO_MATERNO, NUMERO_CONTRATO, FECHA_DESVINCULACION, CAUSAL) "+
        "VALUES (?, ?, ?, ?, ?, ?, ?, ?);", t)
        conexion.commit()
        
conexion.close()