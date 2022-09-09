from email.mime import application
from tkinter import *
from tkinter import ttk
import contrataciones
import desvinculaciones

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
   
   def mostrarContratos(self, cuaderno):#antes se llamava mostrarTrabajadores
      pagina = ttk.Frame(cuaderno)
      cuaderno.add(pagina, text = "Contrataciones")
      labelFrame = LabelFrame(pagina, text = "trabajadores", padx = 0, pady = 10)
      
      labelFrame.grid(column=0, row=0, padx=200, pady=100)
      buttonCargarContratos = ttk.Button(pagina, text = "Cargar contratos", command= lambda: self.CargarContratos())

      buttonCargarContratos.grid(column=0, row = 0, padx = 0 , pady = 20)
      buttonCargarContratos.place(x = 10 , y = 10 )
        
   
   def mostrarDesvinculaciones(self, cuaderno):#antes se llamaba mostrarContratos
      pagina = ttk.Frame(cuaderno)
      cuaderno.add(pagina, text = "Desvinculaciones")
      btnCargarDesv = ttk.Button(pagina, text = "Cargar Desvinculaciones", command = lambda:self.CargarDesvinculaciones())
      btnCargarDesv.grid(column = 0, row = 0, padx = 0 , pady = 20)
      btnCargarDesv.place(x = 10 , y = 10)
      

   def CargarContratos(self):
      contrataciones.contrataciones.cargarContrataciones()
   
   def CargarDesvinculaciones(self):
      desvinculaciones.Desvinculaciones.cargarDesvinculaciones()

      

application = app()