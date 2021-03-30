#!/usr/bin/env python
import time
from tkinter import *
import tkinter
from tkinter import messagebox
import os

def conexiones():
    os.system ("conexion.py")
    power.config(state = NORMAL)
    con.config(state = DISABLED)
    prueba.set("ENCIENDE LAS FUENTES")

def source():
    os.system ("F1_ON.py")
    os.system ("F2_ON.py")
    slogan.config(state = NORMAL)
    power.config(state = DISABLED)
    prueba.set("1-ACTUALIZACION DE SOFTWARE")

def Test():
    os.system ("python crono_4m.py")
    # 1. PushSW(ACTUALIZACION DE SOFTWARE)
    if Contador.get() == '0':
        RUTA_CARPETA = "C:\\TEST-GALAXY\\1-PushSW(ACTUALIZACION_DE_SOFTWARE)"
        os.system(f'start {os.path.realpath(RUTA_CARPETA)}')
        response1=messagebox.askquestion("ACTUALIZACION DE SOFTWARE", "Type Exit... ?")
        
        if response1 == 'yes':
            Contador.set(str(int(Contador.get()) + 1))
            os.system ("python crono_4m.py")
        else:
            messagebox.showerror("ERROR", "Llama a Ingenieria de Prubas")
            slogan.config(state = DISABLED)

    # 2. ResetBBU-TDS (HABILITAR MODO DE PRUEBA)
    if Contador.get() == '1':
        prueba.set("2-HABILITAR MODO DE PRUEBA")
        RUTA_CARPETA = "C:\\TEST-GALAXY\\2-ResetBBU-TDS(HABILITAR_MODO_DE_PRUEBA)"
        os.system(f'start {os.path.realpath(RUTA_CARPETA)}')
        response2=messagebox.askquestion("HABILITAR MODO DE PRUEBA", "Type Exit... ?")

        if response2 == 'yes':
            Contador.set(str(int(Contador.get()) + 1))
            os.system ("python crono_4m.py")
        else:
            messagebox.showerror("ERROR", "Llama a Ingenieria de Prubas")
            slogan.config(state = DISABLED)

    # 3. GetBBU_TestingState (CONFIRMAR MODO DE PRUEBA)
    if Contador.get() == '2':
        prueba.set("3-CONFIRMAR MODO DE PRUEBA")
        RUTA_CARPETA = "C:\\TEST-GALAXY\\3-GetBBU_TestingState(CONFIRMAR_MODO_DE_PRUEBA)"
        os.system(f'start {os.path.realpath(RUTA_CARPETA)}')
        response3=messagebox.askquestion("CONFIRMAR MODO DE PRUEBA", "TSTATE=Enabled ?")

        if response3 == 'yes':
            Contador.set(str(int(Contador.get()) + 1))
        else:
            Contador.set(str(int(Contador.get()) - 1))
            prueba.set("2-HABILITAR MODO DE PRUEBA")

    # 4. StartTestModels_TM1 (TRANSMISION MODO 1)
    if Contador.get() == '3':
        prueba.set("4-TRANSMISION MODO 1")
        RUTA_CARPETA = "C:\\TEST-GALAXY\\4-StartTestModels_TM1(TRANSMISION_MODO1)"
        os.system(f'start {os.path.realpath(RUTA_CARPETA)}')
        response4=messagebox.askquestion("TRANSMISION MODO 1", "SUCCESS & Type Exit...?")

        if response4 == 'yes':
            Contador.set(str(int(Contador.get()) + 1))
            os.system ("python crono_10m.py")
        else:
            messagebox.showerror("ERROR", "Llama a Ingenieria de Prubas")
            slogan.config(state = DISABLED)
    
    # 5.-StopTestModels (DETENER TRANSMISION 1)
    if Contador.get() == '4':
        prueba.set("5-DETENER TRANSMISION 1")
        RUTA_CARPETA = "C:\\TEST-GALAXY\\5-StopTestModels(DETENER_TRANSMISION_1)"
        os.system(f'start {os.path.realpath(RUTA_CARPETA)}')
        response4=messagebox.askquestion("DETENER TRANSMISION 1", "SUCCESS & Type Exit...?")

        if response4 == 'yes':
            Contador.set(str(int(Contador.get()) + 1))
            os.system ("python crono_2m.py")
        else:
            messagebox.showerror("ERROR", "Llama a Ingenieria de Prubas")
            slogan.config(state = DISABLED)

    # 6. StartTestModels_TM2 (TRANSMITIR MODO 2)
    if Contador.get() == '5':
        prueba.set("6-TRANSMITIR MODO 2")
        RUTA_CARPETA = "C:\\TEST-GALAXY\\6-StartTestModels_TM2(TRANSMITIR_MODO_2)"
        os.system(f'start {os.path.realpath(RUTA_CARPETA)}')
        response4=messagebox.askquestion("TRANSMITIR MODO 2", "SUCCESS & Type Exit...?")

        if response4 == 'yes':
            Contador.set(str(int(Contador.get()) + 1))
            os.system ("python crono_10m.py")
        else:
            messagebox.showerror("ERROR", "Llama a Ingenieria de Prubas")
            slogan.config(state = DISABLED)

    # 7.-StopTestModels (DETENER TRANSMISION 2)
    if Contador.get() == '6':
        prueba.set("7-DETENER TRANSMISION 2")
        RUTA_CARPETA = "C:\\TEST-GALAXY\\7-StopTestModels(DETENER_TRANSMISION_2)"
        os.system(f'start {os.path.realpath(RUTA_CARPETA)}')
        response4=messagebox.askquestion("DETENER TRANSMISION 2", "SUCCESS & Type Exit...?")

        if response4 == 'yes':
            Contador.set(str(int(Contador.get()) + 1))
            os.system ("python crono_2m.py")
        else:
            messagebox.showerror("ERROR", "Llama a Ingenieria de Prubas")
            slogan.config(state = DISABLED)

    # 8. GetRRH-Faults (OBTENER LOG DE LA UNIDAD)
    if Contador.get() == '7':
        prueba.set("8-OBTENER LOG DE LA UNIDAD")
        RUTA_CARPETA = "C:\\TEST-GALAXY\\8-GetRRH-Faults(OBTENER_LOG_DE_LA_UNIDAD)"
        os.system(f'start {os.path.realpath(RUTA_CARPETA)}')
        response4=messagebox.askquestion("OBTENER LOG DE LA UNIDAD", "SUCCESS & Type Exit...?")

        if response4 == 'yes':
            Contador.set(str(int(Contador.get()) + 1))
        else:
            messagebox.showerror("ERROR", "Llama a Ingenieria de Prubas")
            slogan.config(state = DISABLED)
    
    # 9. GetBBU-FaultHistory (OBTENER LOG DEL SM)
    if Contador.get() == '8':
        prueba.set("9-OBTENER LOG DEL SM")
        RUTA_CARPETA = "C:\\TEST-GALAXY\\9-GetBBU-FaultHistory(OBTENER_LOG_DEL_SM)"
        os.system(f'start {os.path.realpath(RUTA_CARPETA)}')
        response4=messagebox.askquestion("OBTENER LOG DEL SM", "SUCCESS & Type Exit...?")

        if response4 == 'yes':
            Contador.set(str(int(Contador.get()) + 1))
        else:
            messagebox.showerror("ERROR", "Llama a Ingenieria de Prubas")
            slogan.config(state = DISABLED)
    
    # 10. GetRRH-Snapshot (OBTENER SNAPSHOT)
    if Contador.get() == '9':
        prueba.set("10-OBTENER SNAPSHOT")
        RUTA_CARPETA = "C:\\TEST-GALAXY\\10-GetRRH-Snapshot(OBTENER_SNAPSHOT)"
        os.system(f'start {os.path.realpath(RUTA_CARPETA)}')
        response4=messagebox.askquestion("OBTENER SNAPSHOT", "SUCCESS & Type Exit...?")

        if response4 == 'yes':
            Contador.set(str(int(Contador.get()) + 1))
        else:
            messagebox.showerror("ERROR", "Llama a Ingenieria de Prubas")
            slogan.config(state = DISABLED)

    # 11. GetRRH-SW-Version (VERIFICAR VERSION DE SOFTWARE)
    if Contador.get() == '10':
        prueba.set("11-VERIFICAR VERSION DE SOFTWARE")
        RUTA_CARPETA = "C:\\TEST-GALAXY\\11-GetRRH-SW-Version(VERIFICAR_VERSION_DE_SOFTWARE)"
        os.system(f'start {os.path.realpath(RUTA_CARPETA)}')
        response4=messagebox.askquestion("VERIFICAR VERSION DE SOFTWARE", "Termino la prueba?")

        if response4 == 'yes':
            Contador.set(str(int(Contador.get()) + 1))
            prueba.set("PRUEBA TERMINADA")
        else:
            messagebox.showerror("ERROR", "Llama a Ingenieria de Prubas")
            slogan.config(state = DISABLED)

    #Final de la prueba
    if Contador.get() == '11':
        prueba.set("REALIZA LA VALIDACION DE LOGS")
        slogan.config(state = DISABLED)
        validar.config(state = NORMAL)

def log():
    os.system ("validacion.py")
    validar.config(state = DISABLED)
    poweroff.config(state = NORMAL)
    prueba.set("APAGA LAS FUENTES")

def sourceoff():
    os.system ("F1_OFF.py")
    os.system ("F2_OFF.py")
    poweroff.config(state = DISABLED)
    prueba.set("PRUEBA TERMINADA")

def ask_quit():
    if messagebox.askokcancel("Cerrar la aplicación", "¿Seguro que quieres cerrar la prueba?"):
        ventana.destroy()

# Primera ventana con valores positivos
ventana = tkinter.Tk()
ventana.title(" LBTS GALAXY ")
ventana.geometry("300x300+500+200")
ventana.resizable(0,0)
ventana.iconbitmap('.\\img\\nokia.ico')

# Variables
Contador=tkinter.StringVar(ventana, "0")
prueba=tkinter.StringVar()
prueba.set("REALIZA LAS CONEXIONES")
minute=StringVar()
second=StringVar()
# Espacio en blanco
etiqueta = tkinter.Label(ventana, textvariable=prueba, width=100, height=3, anchor="center")
etiqueta.pack()
# Boton de conexiones
con = tkinter.Button(ventana,text="CONEXIONES",command=conexiones, width=25, height=2, anchor="center")
con.config(state = NORMAL)
con.pack()
# Boton de encender Fuentes de Poder
power = tkinter.Button(ventana,text="ENCENDER FUENTES",command=source, width=25, height=2, anchor="center")
power.config(state = DISABLED)
power.pack()
# Boton de inicio de prueba
slogan = tkinter.Button(ventana, text="INICIAR PRUEBA", command=Test, width=25, height=2, anchor="center")
slogan.config(state = DISABLED)
slogan.pack()
# Boton para validar la unidad
validar = tkinter.Button(ventana, text="VALIDAR LOG", command=log, width=25, height=2, anchor="center")
validar.config(state = DISABLED)
validar.pack()
# Boton de encender Fuentes de Poder
poweroff = tkinter.Button(ventana,text="APAGA LAS FUENTES",command=sourceoff, width=25, height=2, anchor="center")
poweroff.config(state = DISABLED)
poweroff.pack()
# Label del contador
etiqueta2 = tkinter.Label(ventana, textvariable=Contador, anchor="center")
#etiqueta2.pack()
#etiqueta2.config(fg="black", bg="green", font=("Verdana",24)) 

ventana.protocol("WM_DELETE_WINDOW", ask_quit)
ventana.mainloop()