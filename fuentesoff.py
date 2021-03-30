from tkinter import *
from tkinter import messagebox
import os

img = Tk()
img.title("Conexion de la UUT")
img.geometry("520x154+500+200")
img.resizable(0,0)
img.iconbitmap('.\\img\\nokia.ico')
imagen = PhotoImage(file = ".\\img\\Fuentesoff.png")
Label(img,image = imagen).place(x=0, y=0)

response=messagebox.askquestion("Apagado de Fuentes", "Apagaste las Fuentes?")
if response == 'yes':
    img.destroy()
    
img.mainloop()