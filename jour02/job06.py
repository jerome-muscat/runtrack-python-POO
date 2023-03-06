class Commande:
    def __init__(self, num_commande, list_plats):
        self.__num_commande = num_commande
        self.__list_plats = {} 
        self.__statut_commande = "en cours"
        self.__total = 0
        self.__indic_taxe = "HT"
        for plat, prix in list_plats.items():
            self.__list_plats[plat] = {"prix": prix, "statut": "en cours"}
    
    def ajoutPlats(self, plat, prix):
        self.__list_plats[plat] = {"prix": prix, "statut": "en cours"}
    
    def annulCommande(self):
        self.__statut_commande = "annulée"
    
    def __total_commande(self):
        self.__total = 0
        for plat, prix in self.__list_plats.items():
            self.__total += prix['prix']
    
    def afficher_total(self):
        if self.__total == 0:
            self.__total_commande()
        
        self.__statut_commande = "terminée"

        list_plats = [f" {plats} à {prix['prix']} €" for plats, prix in self.__list_plats.items()]
        list_plats = "'" + ",".join(list_plats).strip() + "'"

        print(f"Pour la commande n° {self.__num_commande}, qui contenait {list_plats}, le total a régler {self.__total} € {self.__indic_taxe}")

    def total_commandeTTC(self):
        self.__total_commande()
        self.__total = self.__total * 1.2
        self.__indic_taxe = "TTC"

plats = {"salade haricots verts": 7, "carbonara": 10, "mousse au chocolat": 3}
commande1 = Commande(1, plats)
commande1.afficher_total()

commande1.ajoutPlats("salade de fruits", 5)
commande1.total_commandeTTC()
commande1.afficher_total()
