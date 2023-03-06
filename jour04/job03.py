class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    
    def perimetre(self):
        return (self.__largeur + self.__longueur) * 2
    
    def surface(self):
        return self.__largeur * self.__longueur
    
    def setLongueur(self, longueur):
        self.__longueur = longueur
    
    def setLargeur(self, largeur):
        self.__largeur = largeur
    
    def getLongueur(self):
        return self.__longueur

    def getLargeur(self):
        return self.__largeur

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        Rectangle.__init__(self, longueur, largeur)
        self.hauteur = hauteur
    
    def volume(self):
        return self.hauteur * self.surface()

rectangle = Rectangle(20, 10)
print(rectangle.surface())
print(rectangle.perimetre())
rectangle.setLargeur(10)
rectangle.setLongueur(5)
print(rectangle.surface())
print(rectangle.perimetre())
print(rectangle.getLargeur())

print(rectangle.getLongueur())



print("---------------------")
parallelepipede = Parallelepipede(20, 10,5)
print(parallelepipede.surface())
print(parallelepipede.perimetre())
print(parallelepipede.volume())
parallelepipede.setLargeur(10)
parallelepipede.setLongueur(5)
print(parallelepipede.surface())
print(parallelepipede.perimetre())
print(parallelepipede.volume())
print(parallelepipede.getLargeur())
print(parallelepipede.getLongueur())
