from cgi import test
from email.mime import application
from tkinter import *

class Test:
    def __init__(self, ventana):
        print("Test")
        self.ventana = ventana
        self.ventana.title("test title");

if __name__ == "__main__":
    ventana = Tk()
    application = test(ventana)
    ventana.mainloop()