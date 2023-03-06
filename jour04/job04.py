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

rectangle = Rectangle(10, 20)
print(rectangle.aire())