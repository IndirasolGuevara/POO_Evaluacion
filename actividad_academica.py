from eventos import Evento
class TrabajoPractico(Evento):
  def __init__(self,fecha, descripcion,Materia):
    super().__init__(self,fecha, descripcion)
    self.Materia= Materia

  def __str__(self):
    return f"trabajo practico de",{self.Materia},":",{self.descripcion}, "fecha:",{self.fecha} 

class ReunionEstudio(Evento):
  def __init__(self,fecha, descripcion):
    super().__init__(self,fecha, descripcion)   
  def __str__(self):
    return f"Reunion de estudio",{self.Materia},":",{self.descripcion}, "fecha:",{self.fecha} 

class Examen(Evento):
  def __init__(self,fecha, descripcion,Materia):
    super().__init__(self,fecha, descripcion)
    self.Materia= Materia
    def __str__(self):
        return f"el examen de ",{self.Materia},":",{self.descripcion}, "fecha:",{self.fecha}

class Agenda(Evento):
  def __init__(self,fecha, descripcion):
    super().__init__(self,fecha, descripcion)
  def __str__(self):
    self.Evento=[]

  def mostrar(self):
    for evento in self.Evento:
      print(evento)

  def añadir_evento(self,tipoDeEvento):
    nueve = tipoDeEvento(
      input("fecha: "),
      input("Ddescipcion: ")
      )
    self.Evento.append(nueve)
    #nuevoevento.añadir_evento(examen)
    
  def eliminarEvento(self,evento):
      pass