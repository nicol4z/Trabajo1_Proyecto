from multiprocessing.sharedctypes import Value
from typing import Tuple
import csv
from tkinter import filedialog
import math


filename = filedialog.askopenfilename(initialdir = "/", title = "Seleccionar archivo", 
filetypes = (("Text files","*.csv*"),("all files","*.*")))
with open(filename) as data:
    strPrueba = 23123
    reader = csv.DictReader(data, delimiter=";", skipinitialspace = True)
    for n, r in enumerate(reader):
        
        t = tuple(r.values())
      #  t =  strPrueba + r.values()
        print(t[0])



