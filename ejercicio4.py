print ("ingresar numero de partidos ganados:")
PG = int(input("PG:"))
print ("ingresar numero de partidos empatados:")
PE = int(input("PE:"))
print ("ingrese numero de partidos perdidos:")
PP = int(input("PP:"))
PPG=PG*3
PPE=PE*1
PPP=PP*0
PT=PPG+PPE+PPP
print ("puntaje final:", PT)
