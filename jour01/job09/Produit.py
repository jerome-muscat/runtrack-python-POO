class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA / 100
    
    def CalculerPrixTTC(self):
        return f"Le prix TTC de {self.nom} est {self.prixHT * (1 + self.TVA)}"

    def Aficher(self):
        return f"Le prix HT de {self.nom} est : {self.prixHT} \nSachant que la TVA est à {self.TVA * 100}%, le prix TTC est : {self.prixHT * (1 + self.TVA)}"
    
    def modifnom(self, nouveau_nom):
        self.nom = nouveau_nom
        return self.nom
    
    def modifprix(self, nouveau_prix):
        self.prixHT = nouveau_prix
        return f"{self.prixHT} €"

produit1 = Produit("Lunette rouge", 30, 20)
print(produit1.CalculerPrixTTC())
print(produit1.Aficher())
print(produit1.modifnom("Lunette bleu"))
print(produit1.modifprix(20))

produit2 = Produit("Ecouteur blanc", 10, 10)
print(produit2.CalculerPrixTTC())
print(produit2.Aficher())
print(produit2.modifnom("Ecouteur noir"))
print(produit2.modifprix(15))

produit3 = Produit("Ordinateur HP", 400, 20)
print(produit3.CalculerPrixTTC())
print(produit3.Aficher())
print(produit3.modifnom("Ordinateur Asus"))
print(produit3.modifprix(500))