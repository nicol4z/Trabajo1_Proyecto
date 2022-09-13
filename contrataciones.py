from calendar import c
from tkinter import *
import csv
import sqlite3
import trabajador
import pandas
from tkinter import filedialog
from typing import List, Tuple 
from tkinter import messagebox as mb
from datetime import datetime
from xlsxwriter.workbook import Workbook

from dateutil.relativedelta import relativedelta


  
class contrataciones:
  def cargarContrataciones():
      try:
          filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", 
          filetypes = (("Text files","*.csv*"),("all files","*.*"))) 
          i = 0
          if filename == '':
            return

          conexion = sqlite3.connect("db1.db")
          cursor = conexion.cursor()

          with open(filename) as data:
           reader = csv.DictReader(data, delimiter=";", skipinitialspace = True)
           for n, r in enumerate(reader):
             t = tuple(r.values())
             rutTrabajador = t[0]
             verificar = verificarTrabajador(rutTrabajador, conexion)
             if verificar == False:
                #print("insertar en trabajador")
                trabajador.Trabajador.insertarTrabajador(t[0], t[1], t[2], t[3], t[4], t[7])
             
             else:
                #print("no insertar en trabajador")
                cursor.execute("INSERT INTO Contrataciones (RUT, DV, NOMBRES, APELLIDO_MATERNO, APELLIDO_PATERNO, JORNADA, PROYECTO, CARGO, INICIO_CONTRATO, TIPO_CONTRATO, DURACION, SUELDO) VALUES "+
                "(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", t)
            
             
             conexion.commit()

          mb.showinfo("Contrataciones", "Las contrataciones fueron cargadas exitosamente") 
          conexion.close()
        
      except sqlite3.IntegrityError as e:
          mb.showerror("Contrataciones","Los datos que intenta cargar ya existen en el sistema")

      except sqlite3.ProgrammingError as e:
          mb.showerror("Contrataciones", "Los datos que intenta ingresar no son validos")

def verificarTrabajador(rutTrabajador, conexion):
     trabajador = conexion.cursor()
     fila = trabajador.execute("SELECT RUT FROM trabajadores WHERE rut = ?", (rutTrabajador,))
     if trabajador.fetchone() == None:
        return False
     else:
        return True
     

def exportarContrataciones():
   #conexion = sqlite3.connect("db1.db")
   #pandas.read_sql_query("SELECT * FROM trabajadores").to_excel("C:\Users\Nicolas\OneDrive\Escritorio\contrataciones(export)")

   conexion = sqlite3.connect("db1.db")
   cursor = conexion.cursor()

   contrataciones = cursor.execute("select * from contrataciones")
   if contrataciones.fetchone() == None:
      mb.showerror("Contrataciones", "No existen contrataciones en el sistema")
      return

   workbook = Workbook("contrataciones.xlsx")
   worksheet = workbook.add_worksheet()
   for i, row in enumerate(contrataciones):
      for j, value in enumerate(row):
         worksheet.write(i, j, row[j])
   
   workbook.close()