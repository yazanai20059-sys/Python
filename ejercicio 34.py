def nums_que_comencen_per(llista_noms, lletra):
    """
    Compta quants noms de la llista comencen per una lletra específica
    
    Paràmetres:
        llista_noms: llista de strings amb noms
        lletra: caràcter per buscar al començament dels noms
    
    Retorna:
        Enter amb el nombre de noms que comencen per la lletra indicada
    """
    comptador = 0
    for nom in llista_noms:
        if nom[0].lower() == lletra.lower():
            comptador += 1
    return comptador


# Programa principal
noms = ["Anna", "Bernat", "Albert", "Carla", "Arnau", "Berta", "Cecília"]

lletra_usuari = input("Introdueix una lletra: ")
resultat = nums_que_comencen_per(noms, lletra_usuari)

print(f"Nombres de noms que comencen per '{lletra_usuari}': {resultat}")