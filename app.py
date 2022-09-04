from email.mime import application
from tkinter import *
from tkinter import ttk

class app:
   def __init__(self):
      ventana = Tk()
      ventana.title("Sistema de recursos humanos")
      ventana.geometry("450x450")
      cuaderno = ttk.Notebook(ventana)
      cuaderno.pack(fill = "both", expand = "yes")
      cuaderno.grid(column=0, row = 0, padx = 10, pady = 10)
      self.mostrarTrabajadores(cuaderno)
      self.mostrarContratos(cuaderno)
      ventana.mainloop()
   
   def mostrarTrabajadores(self, cuaderno):
      pagina = ttk.Frame(cuaderno)
      cuaderno.add(pagina, text = "mostrar trabajadores")
   
   def mostrarContratos(self, cuaderno):
      pagina = ttk.Frame(cuaderno)
      cuaderno.add(pagina, text = "mostrar contratos")

application = app()