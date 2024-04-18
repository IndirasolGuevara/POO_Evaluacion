from eventos import Evento
from actividad_academica import TrabajoPractico,ReunionEstudio,Examen
from Agenda import Agenda
agenda = Agenda()
evento = Evento()
seleccion= input("ingrese 1 si quiere agregar un evento, 2 para eliminar 3 para mostrar los eventos, 4 salir 4")
while seleccion < "4":
    if seleccion =="1":
        seleccionEvento=input("ingrese 1 si desea agregar a su agenda un examen, 2) agregar un trabajo practico, 3)una reunion de estudio")
        nombreEvento= str(input ("ingrese el nombre que le va a dar a su evento: "))
        materia=str(input("ingrese la materia "))
        fecha= str(input("ingrese la fecha de su examen: "))
        descripcion=str(input("ingrese info de su examen "))
        
        if seleccionEvento =="1":
            evento= Examen(nombreEvento, fecha, descripcion, materia)
            print(evento)
        elif seleccionEvento =="2":
            evento= TrabajoPractico(nombreEvento,fecha,descripcion,materia)
        elif seleccionEvento =="3":
            evento= ReunionEstudio(nombreEvento,fecha,descripcion,materia)
        agenda.añadir_evento(evento)    

    if seleccion =="2":
          opcion=input("ingrese el nombre del evento")
          Agenda.eliminarEvento(opcion)

    if seleccion =="3":
        agenda.mostrar()

    seleccion= input("ingrese 1 si quiere agregar un evento, 2 para eliminar 3 para mostrar los eventos, 4 salir")

