def nombre_caractere(chaine_caractere, caractere):
    # print(chaine_caractere)
    n = chaine_caractere[caractere]
   

    if n == chaine_caractere[-1]:
        caractere += 1
        pass
        
    else:
        caractere = nombre_caractere(chaine_caractere, caractere + 1)
    
    return caractere

print(nombre_caractere("Hello", 0))

