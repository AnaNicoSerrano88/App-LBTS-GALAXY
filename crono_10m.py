from tkinter import Tk,Label,Button,Frame,messagebox

def iniciar(h=0, m=0, s=0):
    if s >= 60:
        s=0
        m=m+1
        if m >= 60:
            m=0
            h=h+1
            if h >= 24:
                h=0
 
    #etiqueta que muestra el cronometro en pantalla
    time['text'] = str(h)+":"+str(m)+":"+str(s)
 
    # iniciamos la cuenta progresiva de los segundos
    time.after(1000, iniciar, (h), (m), (s+1))
    
    #if s == 10:
    if m == 10:
        root.destroy() 
 
root = Tk()
root.title('Espera 10 Minutos')
root.geometry("300x300+500+200")
root.attributes("-toolwindow",-1)
root.resizable(0,0)
root.iconbitmap('.\\img\\nokia.ico')
etiqueta1 = Label(root, text="    ", width=50, height=5, anchor="center")
etiqueta1.pack()
time = Label(root, fg='red', width=20, font=("","48"))
time.pack()

# si queremos que se autoejecuta al iniciar el programa hay que desomentar
# esta linea y comentar los botones
#iniciar()
 
# Generamos un frame para poner los botones de iniciar y parar
frame=Frame(root)
# Espacio en blanco

iniciar()

frame.pack()
 
root.mainloop()