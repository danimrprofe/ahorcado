
  

class marcador():
    """
    docstring
    """

    def __init__(self):
        self.puntosBase = 0
        self.puntos = 0
        self.puntosMaximos = 1000

    def suma(self, puntosNuevos):
        if (self.puntos + puntosNuevos) <= self.puntosMaximos:
            self.puntos +=puntosNuevos

    def resta(self, puntosNuevos):
        if self.puntos >= puntosNuevos:
            self.puntos -=puntosNuevos
  
    def getPuntos(self):
        return self.puntos

    def hayPuntos(self, puntos):
        if self.puntos >= puntos:
            return True
        else:
            return False

    def quedanPuntos(self):
        if self.puntos == 0:
            return False
        else:
            return True
