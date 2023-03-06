class Joueur:
    def __init__(self, nom, num, position, nbr_buts, passes_dec, cartons_j, cartons_r):
        self.nom = nom
        self.num = num
        self.position = position
        self.nbr_buts = nbr_buts
        self.passes_dec = passes_dec
        self.cartons_j = cartons_j
        self.cartons_r = cartons_r
    
    def marUnBut(self):
        self.nbr_buts += 1
    
    def effectuerUnePasseDecisive(self):
        self.passes_dec += 1
    
    def recevoirUnCartonJaune(self):
        self.cartons_j += 1
    
    def recevoirUnCartonRouge(self):
        self.cartons_r += 1
    
    def afficherStatistiques(self):
        print(f"Le joueur {self.nom} n°{self.num} a fait {self.nbr_buts} but, {self.passes_dec} passes décisives, {self.cartons_j} cartons jaune et {self.cartons_r} cartons rouge.")
    
class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.liste_joueurs = []
    
    def ajouterJoueur(self, joueur):
        self.liste_joueurs.append(joueur)
    
    def AfficherStatistiquesJoueurs(self):
        for joueur in self.liste_joueurs:
            joueur.afficherStatistiques()

joueur1 = Joueur("Nicolas", 6, "Milieur", 0, 0, 2, 2)
joueur2 = Joueur("Jerome", 30, "Gardien de but", 0,0,0,0)
joueur3 = Joueur("Sophie", 7, "défense", 0,0,0,0)
joueur4 = Joueur("Lucas", 3, "attaque", 0, 0, 0, 0)

les_jeunes = Equipe("Les_jeunes")
les_moins_jeunes = Equipe("Les moins jeunes")

les_jeunes.ajouterJoueur(joueur2)
les_jeunes.ajouterJoueur(joueur4)

les_moins_jeunes.ajouterJoueur(joueur1)
les_moins_jeunes.ajouterJoueur(joueur3)

les_jeunes.AfficherStatistiquesJoueurs()
les_moins_jeunes.AfficherStatistiquesJoueurs()

joueur2.marUnBut()
joueur4.effectuerUnePasseDecisive()
joueur1.recevoirUnCartonRouge()

les_jeunes.AfficherStatistiquesJoueurs()
les_moins_jeunes.AfficherStatistiquesJoueurs()
