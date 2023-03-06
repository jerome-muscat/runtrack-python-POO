class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    
    def SePresenter(self):
        print(f"Je suis {self.prenom} {self.nom}")

personne1 = Personne("MUSCAT", "Jerome")
personne1.SePresenter()

personne2 = Personne("KYPREOS", "Léa")
personne2.SePresenter()