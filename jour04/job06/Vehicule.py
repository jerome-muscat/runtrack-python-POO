class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.anne = annee
        self.prix = prix
    
    def informationsVehicule(self):
        print(f"Marque : {self.marque}\
              \nModèle : {self.modele}\
              \nAnnée : {self.anne}\
              \nPrix : {self.prix} €")
    
    def demarrer(self):
        print("Attention, je roule")

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        Vehicule.__init__(self, marque, modele, annee, prix)
        self.portes = 4
    
    def informationsVehicule(self):
        print(f"Marque : {self.marque}\
              \nModèle : {self.modele}\
              \nAnnée : {self.anne}\
              \nPrix : {self.prix} €\
              \nNombre de portes : {self.portes}")
    
    def demarrer(self):
        print("Attention, la voiture roule")


class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        Vehicule.__init__(self, marque, modele, annee, prix)
        self.roue = 2
    
    def informationsVehicule(self):
        print(f"Marque : {self.marque}\
              \nModèle : {self.modele}\
              \nAnnée : {self.anne}\
              \nPrix : {self.prix} €\
              \nNombre de roue : {self.roue}")
    
    def demarrer(self):
        print("Attention, la moto roule")
    
mercedes = Voiture("Mercedes", "Classe A", 2020, 18500)
mercedes.informationsVehicule()
mercedes.demarrer()

print("--------------------------")
yamaha = Moto("Yamaha", "1200 Vmax", 1987, 4500)
yamaha.informationsVehicule()
yamaha.demarrer()