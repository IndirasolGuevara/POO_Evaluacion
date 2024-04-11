from eventos import Evento
from actividad_academica import TrabajoPractico,ReunionEstudio,Examen,Agenda


seleccion=input("ingrese 1 si desea agregar a su agenda un examen, 2) agregar un trabajo practico, 3)una reunion de estudio")
if seleccion=="1":
    materia=str(input("ingrese la materia "))
    fechaExamen= int(input("ingrese la fecha de su examen: "))
    descripcion_examen=str(input("ingrese info de su examen "))
    mi_examen= Examen(fechaExamen,descripcion_examen,materia)

elif seleccion =="2":
    materia=str(input("ingrese la materia "))
    fechaTP= int(input("ingrese la fecha de su examen: "))
    descripcion_TP=str(input("ingrese info de su examen "))
    mi_TP= TrabajoPractico(fechaTP,descripcion_TP,materia)
    
elif seleccion =="3":
    materia=str(input("ingrese la materia que se va a estudiar "))
    fechaRE= int(input("ingrese la fecha de su examen: "))
    descripcion_RE=str(input("ingrese info de su examen "))
    mi_RE= ReunionEstudio(fechaRE,descripcion_RE,materia)
    



