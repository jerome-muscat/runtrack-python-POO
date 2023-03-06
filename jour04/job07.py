import random

class Jeu:
    def __init__(self):
        self.list_carte = []
        self.valeur = {}
        self.couleur = []
    
    def jeu_carte(self):
        self.valeur = {"As": 11, "Roi": 10, "Dame": 10, "Valet": 10, "10": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}
        self.couleur = ["coeur", "carreau", "pique", "trèfle"]
        for couleur in self.couleur:
            for valeur in self.valeur:
                self.list_carte.append((valeur, couleur))
        
    
    def pioche_carte(self):
        choix_pioche = input("Voulez-vous pioché une carte ? (oui/non) ")
        if choix_pioche.lower() == "non":
            pass
        else:
            self.jeu_carte()
            random_choix = random.choice(self.list_carte)
            print(f"Vous avez piocher la carte {random_choix[0]} qui a la couleur {random_choix[1]}, sa valeur est {self.valeur[random_choix[0]]}")
            self.pioche_carte()

jeu = Jeu()
jeu.pioche_carte()