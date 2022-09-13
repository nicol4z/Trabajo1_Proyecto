from email.mime import application
from tkinter import *
from tkinter import ttk
import contrataciones
import desvinculaciones
from trabajador import Trabajador, exportarTrabajadores

class app:
   def __init__(self):
      ventana = Tk()
      ventana.title("Sistema de recursos humanos")
      ventana.geometry("450x250")
      cuaderno = ttk.Notebook(ventana)
      cuaderno.pack(fill = "both", expand = "yes")
      cuaderno.grid(column=0, row = 0, padx = 10 , pady = 10)
      self.mostrarContratos(cuaderno)
      self.mostrarDesvinculaciones(cuaderno)
      ventana.mainloop()
   
   def mostrarContratos(self, cuaderno):
      pagina = ttk.Frame(cuaderno)
      cuaderno.add(pagina, text = "Contrataciones")
      labelFrame = LabelFrame(pagina, text = "trabajadores", padx = 0, pady = 0)
      
      labelFrame.grid(column=0, row=0, padx=200, pady=100)
      buttonCargarContratos = ttk.Button(pagina, text = "Cargar contratos", command= lambda: self.CargarContratos())
      #buttonMostrarTrabajadores = ttk.Button(pagina, text = "MostrarContratos")
      btnExportarContrataciones = ttk.Button(pagina, text = "Exportar contratos", command= lambda: self.exportarContrataciones())

      buttonCargarContratos.grid(column=0, row = 0, padx = 300 , pady = 100)
      buttonCargarContratos.place(x = 10 , y = 10 )

      btnExportarContrataciones.grid(column = 0, row = 0, padx = 200, pady = 100)
      btnExportarContrataciones.place(x = 10 , y = 60)

      btnExportarTrabajadores = ttk.Button(pagina, text = "Exportar trbajadores", command = lambda: self.exportarTrabajadores())
      btnExportarTrabajadores.grid(column = 0, row = 0, padx = 300 , pady = 100)
      btnExportarTrabajadores.place(x = 120 , y = 10)
      
      
        
   
   def mostrarDesvinculaciones(self, cuaderno):#antes se llamaba mostrarContratos
      pagina = ttk.Frame(cuaderno)
      cuaderno.add(pagina, text = "Desvinculaciones")
      btnCargarDesv = ttk.Button(pagina, text = "Cargar Desvinculaciones", command = lambda:self.CargarDesvinculaciones())
      btnCargarDesv.grid(column = 0, row = 0, padx = 0 , pady = 20)
      btnCargarDesv.place(x = 10 , y = 10)

      btnExportarDesvinculaciones = ttk.Button(pagina, text = "Exportar Desvinculaciones", command = lambda:self.exportarDesvinculaciones())
      btnExportarDesvinculaciones.grid(column= 0, row = 0, padx = 0 , pady = 20)
      btnExportarDesvinculaciones.place(x = 10 , y = 60)

   def CargarContratos(self):
      contrataciones.contrataciones.cargarContrataciones()
   
   def CargarDesvinculaciones(self):
      desvinculaciones.Desvinculaciones.cargarDesvinculaciones()

   def exportarContrataciones(self):
      contrataciones.exportarContrataciones()

   def exportarDesvinculaciones(self):
      desvinculaciones.exportarDesvinculaciones()

   def exportarTrabajadores(self):
      exportarTrabajadores()
      

application = app()