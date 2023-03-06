class Tache:
    def __init__(self, titre, description):
        self.titre = titre
        self.description = description
        self.statut = "à faire"
    
class ListeDeTaches:
    def __init__(self):
        self.taches = []
    
    def ajouterTache(self, ajout_tache):
        nouvel_ajout = [ajout_tache.titre, ajout_tache.description, ajout_tache.statut]
        self.taches.append(nouvel_ajout)
        for tache in self.taches:
            ajout_str = f"Tache : {tache[0]} \nDescription : {tache[1]} \nStatut : {tache[2]}\n"
            print(ajout_str)

    
    def supprimerTache(self, suppr_tache):
        suppr_tache = [suppr_tache.titre, suppr_tache.description, suppr_tache.statut]
        taches = self.taches
        self.taches = []
        for tache in taches:
            if tache != suppr_tache:
                self.taches.append(tache)
    
    def marquerCommeFinie(self, modif_tache):
        modif_tache = [modif_tache.titre, modif_tache.description, modif_tache.statut]
        taches = self.taches
        self.taches = []
        for tache in taches:
            if tache == modif_tache:
                modif_tache[2] = "terminer"
                self.taches.append(modif_tache)
                
            else:
                self.taches.append(tache)
    
    def afficherListe(self):
        for tache in self.taches:
            afich = f"Tache : {tache[0]} \nDescription : {tache[1]} \nStatut : {tache[2]}\n"
            # for element in tache:
            #     afich += element + " "
            print(afich)
            
    
    def filterListe(self, statut):
        for tache in self.taches:
            filter_str = f"Tache : {tache[0]} \nDescription : {tache[1]} \nStatut : {tache[2]}\n"
            if tache[2] == statut:
                print(filter_str)

tache1 = Tache("Faire les projets", "Projets de la journée, sur la récursivité")
tache2 = Tache("Aller au kickoff", "Cours sur la récursivité")
tache3 = Tache("Aller au howto", "Corrections des projets de la journée")

listeDeTaches = ListeDeTaches()

listeDeTaches.ajouterTache(tache1)
print("-----------------------------")
listeDeTaches.ajouterTache(tache2)
print("-----------------------------")
listeDeTaches.ajouterTache(tache3)

print("Liste de toutes les tâches:")
listeDeTaches.afficherListe()
print("-----------------------------")

listeDeTaches.supprimerTache(tache2)

print("Liste de toutes les tâches:")
listeDeTaches.afficherListe()
print("-----------------------------")

listeDeTaches.marquerCommeFinie(tache1)

print("Liste de toutes les tâches:")
listeDeTaches.afficherListe()
print("-----------------------------")


print("Liste de toutes les tâches:")
listeDeTaches.afficherListe()

print("Liste des tâches à faire:")
tachesAFaire = listeDeTaches.filterListe("à faire")