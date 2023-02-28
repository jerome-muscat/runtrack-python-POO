from math import *
class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon
    
    def changerRayon(self, nouveau_rayon):
        self.rayon = nouveau_rayon
    
    def afficherInfos(self):
        print(f"Le rayon est {self.rayon}, la circonférence est : {self.circonference()}, l'aire est {self.aire()} et pour diamètre {self.diametre()}")
    
    def circonference(self):
        return self.rayon * 2 * pi
    
    def aire(self):
        return self.rayon ** 2 * pi
    
    def diametre(self):
        return self.rayon * 2

cercle1 = Cercle(4)
cercle1.afficherInfos()
cercle1.changerRayon(8)
print(cercle1.aire())
print(cercle1.circonference())
print(cercle1.diametre())

cercle1 = Cercle(7)
cercle1.afficherInfos()
print(cercle1.aire())
print(cercle1.circonference())
print(cercle1.diametre())