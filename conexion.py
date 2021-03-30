from tkinter import *

img = Tk()
img.title("Conexion de la UUT")
img.geometry("775x569+250+50")
img.resizable(0,0)
img.iconbitmap('.\\img\\nokia.ico')
imagen = PhotoImage(file = ".\\img\\conexion.png")
Label(img,image = imagen).place(x=0, y=0)
img.mainloop()