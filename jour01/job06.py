class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""
    
    def vieillir(self):
        print(f"L'ancien âge de l'animal est : {self.age} ans, il a maintenant : {self.age + 1} ans")
    
    def nommer(self, prenom):
        self.prenom = prenom
        print(f"L'animal s'appel {self.prenom}")

animal = Animal()
animal.vieillir()
animal.nommer("Jean-Paul")
animal.age=int(input("Quel age a l'animal ? "))
animal.vieillir()
