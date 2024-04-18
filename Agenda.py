from eventos import Evento
class Agenda(Evento):
  def __init__(self):
    
    self.ListaEvento=[]

  def mostrar(self):
    for evento in self.ListaEvento:
      print(evento)

  def añadir_evento(self,tipoDeEvento):
         self.listaEvento.append(tipoDeEvento)
    
  def eliminarEvento(self,evento):
        if evento in self.ListEvento:
            self.listEvento.remove(evento)
            print(evento)