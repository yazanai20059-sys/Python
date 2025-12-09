def nums_que_comencen_per(llista_noms):
    """
    Compta quants noms comencen per la lletra 'a' (majúscula o minúscula)
    
    Args:
        llista_noms: llista de strings amb noms
    
    Returns:
        int: nombre de noms que comencen per 'a'
    """
    comptador = 0
    for nom in llista_noms:
        if nom and nom[0].lower() == 'a':
            comptador += 1
    return comptador

# Exemples d'ús
noms = ["Anna", "Bernat", "Albert", "Carla", "antonio"]
print(nums_que_comencen_per(noms))  # Sortida: 3