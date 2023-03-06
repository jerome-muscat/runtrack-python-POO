class Ville:
    def __init__(self, nom, nbHabitants):
        self.__nom = nom
        self.__nbHabitants = nbHabitants
    
    def affichInfos(self):
        print(f"Population de la ville de {self.__nom} : {self.__nbHabitants} habitants")
    
class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
    
    def ajouterPopulation(self):
        self.__ville._Ville__nbHabitants += 1
    


paris = Ville("Paris", 1000000)
paris.affichInfos()

marseille = Ville("Marseille", 861635)
marseille.affichInfos()

john = Personne("John", 45, paris)
john.ajouterPopulation()

myrtille = Personne("Myrtille", 4, paris)
myrtille.ajouterPopulation()

chloe = Personne("Chloé", 18, marseille)
chloe.ajouterPopulation()

paris.affichInfos()
marseille.affichInfos()