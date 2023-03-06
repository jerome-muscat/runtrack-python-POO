class Livre:
    def __init__(self, titre, auteur, pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages
        self.__disponible = True

    def setTitre(self, titre):
        self.__titre = titre

    def setAuteur(self, auteur):
        self.__auteur = auteur

    def setPages(self, pages):
        if pages > 0:
            self.__pages = pages
        else:
            print("Erreur nombre de pages négatifs")
    
    def getTitre(self):
        print(f"Le titre du livre est {self.__titre}")
    
    def getAuteur(self):
        print(f"L'auteur du livre est {self.__auteur}")
    
    def getPages(self):
        if self.__pages > 0:
            print(f"Le nombre du pages est {self.__pages}")
        else:
            print("Le nombre de pages est impossible")
    
    def verifiaction(self):
        if self.__disponible == True:
            return True
        else:
            return False
    
    def emprunter(self):
        if self.verifiaction() == True:
            self.__disponible = False
            print("Le livre peut être emprunté")
        else:
            print("Le livre a déjà été emprunté")
    
    def rendre(self):
        if self.verifiaction() == False:
            self.__disponible = True
            print("Le livre a bien été rendu")
        else:
            print("Le livre a déjà été rendu")
    
livre1 = Livre("No moi", "Joséphine", 250)
livre1.getAuteur()
livre1.getPages()
livre1.getTitre()

livre1.setTitre("No et moi")
livre1.setAuteur("Delphine de Vigan")
livre1.setPages(256)

livre1.getAuteur()
livre1.getPages()
livre1.getTitre()

livre1.setPages(-256)
livre1.getPages()


print(f"La disponivilité du livre est : {livre1.verifiaction()}")
livre1.rendre()     
livre1.emprunter()     
livre1.emprunter() 
print(f"La disponivilité du livre est : {livre1.verifiaction()}")