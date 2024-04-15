from eventos import Evento
class Agenda(Evento):
  def __str__(self):
    self.Evento=[]

  def mostrar(self):
    for evento in self.Evento:
      print(evento)

  def añadir_evento(self,tipoDeEvento):
    self.Evento.append(tipoDeEvento)
    #nuevoevento.añadir_evento(examen)
    
  def eliminarEvento(self,evento):
        if evento in self.Evento:
            self.Evento.remove(evento)
            print(evento)