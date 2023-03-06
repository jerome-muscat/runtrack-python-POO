from math import pi
class Forme:
    def __init__(self):
        pass

    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        Forme.__init__(self)
        self.largeur = largeur
        self.hauteur = hauteur
    
    def aire(self):
        return self.hauteur * self.largeur

class Cercle(Forme):
    def __init__(self, radius):
        Forme.__init__(self)
        self.radius = radius
    
    def aire(self):
        return pi * (self.radius ** 2)
    
rectangle = Rectangle(10, 20)
print(rectangle.aire())

cercle = Cercle(3)
print(cercle.aire())