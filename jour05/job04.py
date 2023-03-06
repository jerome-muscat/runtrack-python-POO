def recherche_valeur_max(list_valeurs, nombre_valeur, valeur_max):
    n = list_valeurs[nombre_valeur]
    
    if nombre_valeur == len(list_valeurs) - 1:
        if list_valeurs[-1] > list_valeurs[-2]:
            if list_valeurs[-1] > valeur_max:
                valeur_max = list_valeurs[-1]

        else:
            if list_valeurs[-2] > valeur_max:
                valeur_max = list_valeurs[-2]
                
        print(valeur_max)
    else:
        if n > list_valeurs[nombre_valeur + 1]:
            if n > valeur_max:
                valeur_max = n

            nombre_valeur = recherche_valeur_max(list_valeurs, nombre_valeur + 1, valeur_max)
        
        else:
            if list_valeurs[nombre_valeur + 1] > valeur_max:
                valeur_max = list_valeurs[nombre_valeur + 1]

            nombre_valeur = recherche_valeur_max(list_valeurs, nombre_valeur + 1, valeur_max)
    

recherche_valeur_max([4, 9, 3, 4, 5, 6, 7, 6, 5, 4], 0, 0)