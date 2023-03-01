class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    
    def setLongueur(self, longueur):
        self.__longueur = longueur
    
    def setLargeur(self, largeur):
        self.__largeur = largeur
    
    def getLongueur(self):
        print(f"Le rectangle à une longueur de : {self.__longueur}")
        return self.__longueur
    
    def getLargeur(self):
        print(f"Le rectangle à une largeur de : {self.__largeur}")

rect1 = Rectangle(10,7)
rect1.getLongueur()
rect1.getLargeur()
rect1.setLargeur(8)
rect1.getLargeur()
rect1.setLongueur(18)
rect1.getLongueur()