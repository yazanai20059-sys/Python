def comptar_vocals(paraula):
    # Inicialitzem el comptador de vocals
    vocals = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    # Convertim la paraula a minúscules per comptar vocals majúscules i minúscules
    paraula = paraula.lower()
    
    # Recorrem cada lletra de la paraula
    for lletra in paraula:
        if lletra in vocals:
            vocals[lletra] += 1
    
    # Mostrem el resultat
    print(f"Hi ha {vocals['a']} a's, {vocals['e']} e's, {vocals['i']} i's, {vocals['o']} o's i {vocals['u']} u's.")
    
    return vocals

# Exemple d'ús
comptar_vocals("Ratatouille")