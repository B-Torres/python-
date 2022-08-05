from typing import final
from ejercicio import ENTERO


input ("ingrce las tres notas del alumno Nota1,Nota2,Nota3:")
nota1= int(input("Nota1:"))
nota2= int(input("Nota2:"))
nota3= int(input("Nota3:"))
Promedio = nota1+nota2+nota3/3
final = Promedio / 3
print ("el promedio del alumno es: " , final)
