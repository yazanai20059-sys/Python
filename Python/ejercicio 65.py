def llista_a_diccionari(llista):
    diccionari = {}
    for e, v in enumerate(llista):
        diccionari[v] = e
    return diccionari


llista = ['casa', 'cotxe', 'cadira', 'taula']
resultat = llista_a_diccionari(llista)
print(resultat)  