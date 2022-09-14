img_object_li = []
import tkinter
import formularios_tkinter
import pdf_modulo
import PyPDF2 
import time

DIGITIZED_FILE=r"D:\programacion\Python\flask\ingresos superiores.pdf"

def actualizar():
    global v2
    v2.destroy()
    v2 = v1.pdf_view(root,pdf_location = DIGITIZED_FILE,width = 200, height = 100)
    v2.pack()





from tkinter import *
import tkinter as tk
from tkinter.filedialog import *
from tkPDFViewer import tkPDFViewer as pdf

root = Tk()
v1 = pdf.ShowPdf()
v2 = v1.pdf_view(root,pdf_location = DIGITIZED_FILE,width = 200, height = 100)
# root.state('zoomed')
menu_principal=formularios_tkinter.crear_menu_principal(root)
formularios_tkinter.submenu_añadir_item(menu_principal,"Actualizar",actualizar)
v2.pack()

root.mainloop()
