from email.mime import application
from tkinter import *
from tkinter import ttk
import contrataciones
import desvinculaciones
import trabajador
import sqlite3

class app:
   def __init__(self):
      ventana = Tk()
      ventana.title("Sistema de recursos humanos")
      ventana.geometry("850x500")
      cuaderno = ttk.Notebook(ventana)
      cuaderno.pack(fill = "both", expand = "yes")
      cuaderno.grid(column=0, row = 0, padx = 10 , pady = 10)
      self.mostrarContratos(cuaderno)
      self.mostrarDesvinculaciones(cuaderno)
      self.MostrarTrabajadores(cuaderno)
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
      trabajador.exportarTrabajadores()

   def MostrarTrabajadores(self, cuaderno):
      pagina = ttk.Frame(cuaderno)
      cuaderno.add(pagina, text = "Trabajadores")
      marco=LabelFrame(pagina,text="")
      marco.grid(row=0,column=0,columnspan=3,pady=20)

      Label(marco,text="Rut").grid(row=0,column=0)
      self.rut = Entry(marco)
      self.rut.grid(row=0,column=1)
      self.rut.focus()
      
      Label(marco,text="Direccion").grid(row=1,column=0)
      self.direccion = Entry(marco)
      self.direccion.grid(row=1,column=1)

      Label(marco,text="Correo").grid(row=2,column=0)
      self.correo = Entry(marco)
      self.correo.grid(row=2,column=1)

      Label(marco,text="Telefono").grid(row=3,column=0)
      self.telefono = Entry(marco)
      self.telefono.grid(row=3,column=1)

      
      self.editar = ttk.Button(marco,text="Editar",command=self.actualizartrabajador)
      self.editar.grid(row=4,columnspan=2,sticky=W+E)
      

      self.tabla = ttk.Treeview(pagina,columns=("#1","#2","#3"))
      self.tabla.grid()      
      self.tabla.bind("<Double-Button-1>",self.click)
      self.tabla.heading("#0",text="Rut")
      self.tabla.heading("#1",text="Dirección")
      self.tabla.heading("#2",text="Correo")
      self.tabla.heading("#3",text="Teléfono")
      datos = trabajador.Trabajador()
      d1 = datos.MostrarTrabajadores()
      for (rut,direccion,correo,telefono) in d1:
         self.tabla.insert('','end',text=rut,values=[direccion,correo,telefono])
      
   def actualizartrabajador(self):
      conexion = sqlite3.connect("db1.db")
      cursor = conexion.cursor()
      cursor.execute("UPDATE Trabajadores SET direccion = ?, correo = ?, telefono = ? WHERE rut = ?", (self.direccion.get(), self.correo.get(), self.telefono.get(), self.rut.get()))
      print(self.direccion.get())
      conexion.commit()
      conexion.close()
      self.rut.delete(0,END)
      self.direccion.delete(0,END)
      self.correo.delete(0,END)
      self.telefono.delete(0,END)
      datos = trabajador.Trabajador()
      d1 = datos.MostrarTrabajadores()
      for (rut,direccion,correo,telefono) in d1:
         self.tabla.delete('','end',text=rut,values=[self.direccion,self.correo,self.telefono])
      for (rut,direccion,correo,telefono) in d1:
         self.tabla.insert('','end',text=rut,values=[direccion,correo,telefono])


   def click(self,event):
      self.dato = str(self.tabla.item(self.tabla.selection())["values"][0])
      self.d = self.tabla.item(self.tabla.selection())["values"][0]
      self.editar["state"] = "normal"
      self.rut.insert(0,str(self.tabla.item(self.tabla.selection())["text"]))



      
application = app()