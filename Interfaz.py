from tkinter import Frame,Label,Button,Checkbutton,Scale,StringVar,IntVar,Tk,Entry
import serial
import time
import threading

raiz =Tk()

raiz.title("Controladores y registro de variables")
#raiz.geometry("650x350")
raiz.config(bg="light blue")
miFrame=Frame()
miFrame.pack(fill="both", expand="True")
miFrame.config(bg="light blue")
miFrame.config(width="900", height="350")


miFrame.arduino = serial.Serial("COM5",9600, timeout=1.0)
time.sleep(1)

miFrame.Sp1cont1=StringVar()
miFrame.Sp2cont1=StringVar()
miFrame.Tcont1=StringVar()

miFrame.Sp1cont2=StringVar()
miFrame.Sp2cont2=StringVar()
miFrame.Tcont2=StringVar()

miFrame.Sp1cont3=StringVar()
miFrame.Sp2cont3=StringVar()
miFrame.Tcont3=StringVar()
miFrame.isRun=True

#--------------------Funcion Para traer valores desde Arduino---------------

def ValoresArduino():
    while miFrame.isRun:
        cad = miFrame.arduino.readline().decode("ascii").strip()
        if cad:
            pos= cad.index(":")
            label=cad[:pos]
            value=cad[pos+1:]
        print(cad)
        
miFrame.hilo1 = threading.Thread(target=ValoresArduino,daemon=True)

#----------------- CONTROLADOR 1 -------------------------

miLabel1= Label(miFrame, text="CONTROLADOR 1", bg="light blue", font=(12)).place(x=20, y=10)

def myClick1():
    miFrame.Sp1cont11 = miFrame.Sp1cont1.get()
    
    miFrame.Sp2cont11 = miFrame.Sp2cont1.get()
      
    miFrame.Tcont11 = miFrame.Tcont1.get()
    
    cadena1 = "1" + "," + miFrame.Sp1cont11 + ":" + miFrame.Sp2cont11 + "-" + miFrame.Tcont11
    cadena1 = str(cadena1)
        
    miFrame.arduino.write(cadena1.encode('ascii'))

miLabel= Label(miFrame, text="Ingrese setpoint 1", bg="light blue", font=(10)).place(x=20, y=40)

cuadroTexto1 =Entry(miFrame,textvariable = miFrame.Sp1cont1).place(x=150,y=40)

miLabel2= Label(miFrame, text="Ingrese setpoint 2", bg="light blue", font=(10)).place(x=20, y=65)

cuadroTexto2=Entry(miFrame, textvariable = miFrame.Sp2cont1).place(x=150,y=65)


miLabel3= Label(miFrame, text="Tiempo setpoint 2", bg="light blue", font=(10)).place(x=20, y=90)


cuadroTexto3=Entry(miFrame, textvariable = miFrame.Tcont1).place(x=150,y=90)

botonEnvio1=Button(raiz, text="Enviar", command = myClick1).place(x =120,y=120)

#----------------- CONTROLADOR 2 -------------------------

miLabel3= Label(miFrame, text="CONTROLADOR 2", bg="light blue", font=(12))
miLabel3.place(x=300, y=10)

def myClick2():
    miFrame.Sp1cont22 = miFrame.Sp1cont2.get()
    
    miFrame.Sp2cont22 = miFrame.Sp2cont2.get()
      
    miFrame.Tcont22 = miFrame.Tcont2.get()
    
    cadena2 = "2" + "," + miFrame.Sp1cont22 + ":" + miFrame.Sp2cont22 + "-" + miFrame.Tcont22
    cadena2 = str(cadena2)
        
    miFrame.arduino.write(cadena2.encode('ascii'))

miLabel4= Label(miFrame, text="Ingrese setpoint 1", bg="light blue", font=(10)).place(x=300, y=40)

cuadroTexto4=Entry(miFrame, textvariable = miFrame.Sp1cont2).place(x=430,y=40)

miLabel5= Label(miFrame, text="Ingrese setpoint 2", bg="light blue", font=(10)).place(x=300, y=65)

cuadroTexto5=Entry(miFrame, textvariable = miFrame.Sp2cont2).place(x=430,y=65)

miLabel6= Label(miFrame, text="Tiempo setpoint 2", bg="light blue", font=(10)).place(x=300, y=90)

cuadroTexto6=Entry(miFrame, textvariable = miFrame.Tcont2).place(x=430,y=90)

botonEnvio2=Button(raiz, text="Enviar", command = myClick2).place(x =410,y=120)

#----------------- CONTROLADOR 3 -------------------------

miLabel3= Label(miFrame, text="CONTROLADOR 3", bg="light blue", font=(12))
miLabel3.place(x=580, y=10)

def myClick3():
    miFrame.Sp1cont33 = miFrame.Sp1cont3.get()
        
    miFrame.Sp2cont33 = miFrame.Sp2cont3.get()
        
    miFrame.Tcont33 = miFrame.Tcont3.get()
        
    cadena3 = "3" + "," + miFrame.Sp1cont33 + ":" + miFrame.Sp2cont33 + "-" + miFrame.Tcont33
    cadena3 = str(cadena3)
        
    miFrame.arduino.write(cadena3.encode('ascii'))

    
    

miLabel4= Label(miFrame, text="Ingrese setpoint 1", bg="light blue", font=(10)).place(x=580, y=40)

cuadroTexto7=Entry(miFrame, textvariable =miFrame.Sp1cont3).place(x=710,y=40)

miLabel5= Label(miFrame, text="Ingrese setpoint 2", bg="light blue", font=(10)).place(x=580, y=65)

cuadroTexto8=Entry(miFrame, textvariable = miFrame.Sp2cont3).place(x=710,y=65)

miLabel8= Label(miFrame, text="Tiempo setpoint 2", bg="light blue", font=(10)).place(x=580, y=90)

cuadroTexto9=Entry(miFrame,textvariable = miFrame.Tcont3).place(x=710,y=90)

botonEnvio2=Button(raiz, text="Enviar", command=myClick3).place(x =670,y=120)

miFrame.hilo1.start()

raiz.mainloop()
