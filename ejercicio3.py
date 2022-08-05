from ctypes.wintypes import INT
from tkinter import RIDGE
from tkinter.tix import InputOnly


print ("ingresar numero de respuestas correcta:")
RC = INT(input("RC:"))
print ("ingresar numero de respuestas incorrecta:")
RI = INT(input("RI:"))
print ("ingrese numero de respuestas en blanco:")
RB = INT(input("RB:"))
PCR = RC*3
PRI = RI*-1
PRB = RB*0
PF = PCR + PRI + PRB 
print("el puntaje final es:", PF)
