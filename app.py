from email.mime import application
from tkinter import *
from tkinter import ttk
import contrataciones

class app:
   def __init__(self):
      ventana = Tk()
      ventana.title("Sistema de recursos humanos")
      ventana.geometry("450x250")
      cuaderno = ttk.Notebook(ventana)
      cuaderno.pack(fill = "both", expand = "yes")
      cuaderno.grid(column=0, row = 0, padx = 10 , pady = 10)
      self.mostrarTrabajadores(cuaderno)
      self.mostrarContratos(cuaderno)
      ventana.mainloop()
   
   def mostrarTrabajadores(self, cuaderno):
      pagina = ttk.Frame(cuaderno)
      cuaderno.add(pagina, text = "Contrataciones")
      labelFrame = LabelFrame(pagina, text = "trabajadores", padx = 0, pady = 10)
      
      labelFrame.grid(column=0, row=0, padx=200, pady=100)
      buttonCargarContratos = ttk.Button(pagina, text = "cargar contratos", command= lambda: self.CargarContratos())

      buttonCargarContratos.grid(column=0, row = 0, padx = 0 , pady = 20)
      buttonCargarContratos.place(x = 10 , y = 10 )
      
      #label= ttk.Label(labelFrame, text = "descripcion")
      #barra = Entry(labelFrame, text = "buscas algo").pack()
      #boton = Button(cuaderno, text = "buscar").pack()   
   
   def mostrarContratos(self, cuaderno):
      pagina = ttk.Frame(cuaderno)
      cuaderno.add(pagina, text = "mostrar contratos")
      #labelFrame = ttk.LabelFrame(pagina, text = "trabajadores")
      #labelFrame.grid()
      

   def CargarContratos(self):
      contrataciones.contrataciones.cargarContrataciones()
      

application = app()