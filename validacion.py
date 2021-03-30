from tkinter import *
from tkinter import messagebox
import os

img = Tk()
img.title("Conexion de la UUT")
img.geometry("974x688+100+0")
img.resizable(0,0)
img.iconbitmap('.\\img\\nokia.ico')
imagen = PhotoImage(file = ".\\img\\logs.png")
Label(img,image = imagen).place(x=0, y=0)

RUTA_CARPETA = "C:\\Users\\testeradmin\\Documents\\RRH_LOGS\\FAULT_Logs"
os.system(f'start {os.path.realpath(RUTA_CARPETA)}')
response=messagebox.askquestion("FAULT_Logs", "Existe un log con numero de serie de la unidad?")
if response == 'yes':
    RUTA_CARPETA = "C:\\Users\\testeradmin\\Documents\\RRH_LOGS\\BBU_ALARM_HISTORY"
    os.system(f'start {os.path.realpath(RUTA_CARPETA)}')
    response2=messagebox.askquestion("BBU_ALARM_HISTORY", "Alarma 'EFaultId_Ethernet Disable  (1197)'")
else:
    messagebox.showerror("ERROR", "Llama a Ingenieria de Prubas")
    # img.destroy()
if response2 == 'yes':
    img.destroy()
    
img.mainloop()