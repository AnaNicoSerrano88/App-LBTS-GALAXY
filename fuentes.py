from tkinter import *
from tkinter import messagebox
import os

img = Tk()
img.title("Conexion de la UUT")
img.geometry("321x287+500+200")
img.resizable(0,0)
img.iconbitmap('.\\img\\nokia.ico')
imagen = PhotoImage(file = ".\\img\\Fuentes.png")
Label(img,image = imagen).place(x=0, y=0)

response=messagebox.askquestion("Encendido de Fuentes", "Encendistes las Fuentes?")
if response == 'yes':
    img.destroy()
    
img.mainloop()