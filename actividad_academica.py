from eventos import Evento
class TrabajoPractico(Evento):
  def __init__(self, nombreEvento, fecha, descripcion, materia):
    super().__init__(nombreEvento, fecha, descripcion)
    self.materia= materia

  def __str__(self):
    return f"trabajo practico de{self.materia}:{self.descripcion}fecha:{self.fecha}"

class ReunionEstudio(Evento):
  def __init__(self,nombreEvento,fecha, descripcion,materia):
    super().__init__(nombreEvento,fecha, descripcion)
    self.materia= materia   
  def __str__(self):
    return f"Reunion de estudio {self.materia}:{self.descripcion}fecha:{self.fecha}"

class Examen(Evento):
  def __init__(self,nombreEvento,fecha, descripcion,materia):
    super().__init__(nombreEvento,fecha, descripcion)
    self.materia= materia
    def __str__(self):
        return f"el examen de {self.materia}:{self.descripcion}fecha:{self.fecha}"


