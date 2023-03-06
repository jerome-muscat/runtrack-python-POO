class Voiture:
    def __init__(self, marque, modele, annee, km):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__km = km
        self.__en_marche = False
        self.__reservoir = 50
    
    def setMarque(self, marque):
        self.__marque = marque
    
    def setModele(self, modele):
        self.__modele = modele
    
    def setAnnee(self, annee):
        self.__annee = annee
    
    def setKilometrage(self, km):
        self.__km = km
    
    def getMarque(self):
        print(f"La marque de la voiture est : {self.__marque}")
        return self.__marque
    
    def getModele(self):
        print(f"Le modèle de la voiture est : {self.__modele}")
        return self.__modele
    
    def getAnnee(self):
        print(f"L'année de sortie de la voiture est : {self.__annee}")
        return self.__annee
    
    def getKilometrage(self):
        print(f"La voiture a roulé {self.__km} km")
        return self.__km
    
    def demarrer(self):
        if self.__verifier_plein() > 5:
            self.__en_marche = True
            print("La voiture a pu démarrer")
        else:
            print("Plus assez d'essence pour démarrer")
    
    def arreter(self):
        self.__en_marche = False
        print("La voiture s'arrete")
    
    def __verifier_plein(self):
        return self.__reservoir

peugeot208 = Voiture("peugeot", "208", 2016, 48000)
peugeot208.getAnnee()
peugeot208.getKilometrage()
peugeot208.getMarque()
peugeot208.getModele()

peugeot208.setMarque("Peugeot")
peugeot208.getMarque()

peugeot208.demarrer()
peugeot208.arreter()