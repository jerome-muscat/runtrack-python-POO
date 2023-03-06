class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def afficherLesPoints(self):
        print(f"Le point a pour abscissse : {self.x} et pour ordonnée : {self.y}")
    
    def afficherX(self):
        print(f"Le point a pour abscissse : {self.x}")
    
    def afficherY(self):
        print(f"Le point a pour ordonnée : {self.y}")
    
    def changerX(self, nouveauX):
        ancienX = self.x
        self.x = nouveauX

        print(f"Le point avait pour abscissse : {ancienX}, maintenant son abscisse est : {self.x}")
    
    def changerY(self, nouveauY):
        ancienY = self.y
        self.y = nouveauY
        
        print(f"Le point avait pour ordonnée : {ancienY}, maintenant son ordonnée est : {self.y}")

point1 = Point(100, 200)
point1.afficherLesPoints()
point1.changerX(120)
point1.changerY(300)

point2 = Point(300, 150)
point2.afficherLesPoints()
point2.afficherX()
point2.afficherY()