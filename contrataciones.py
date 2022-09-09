from calendar import c
from tkinter import *
import csv
import sqlite3
from tkinter import filedialog
from typing import List, Tuple 
from tkinter import messagebox as mb
import app
  
class contrataciones:

    def cargarContrataciones():
      try:

          filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", 
          filetypes = (("Text files","*.csv*"),("all files","*.*"))) 

          conexion = sqlite3.connect("db1.db")
          cursor = conexion.cursor()

          with open(filename) as data:
           reader = csv.DictReader(data, delimiter=";", skipinitialspace = True)
           for n, r in enumerate(reader):
             t = tuple(r.values())
             cursor.execute("INSERT INTO Contrataciones (RUT, DV, NOMBRES, APELLIDO_MATERNO, APELLIDO_PATERNO, JORNADA, PROYECTO, CARGO, INICIO_CONTRATO, TIPO_CONTRATO, DURACION, SUELDO) VALUES "+
             "(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", t)
             conexion.commit()
             
           mb.showinfo("Contrataciones", "las contrataciones fueron cargadas exitosamente")
        
          conexion.close()
        
      except sqlite3.IntegrityError as e:
          mb.showerror("Contrataciones","Los datos que intenta cargar ya existen en el sistema")

      except sqlite3.ProgrammingError as e:
          mb.showerror("Contrataciones", "Los datos que intenta ingresar no son validos")






