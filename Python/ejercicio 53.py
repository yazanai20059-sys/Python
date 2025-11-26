def index_paraula(llista_ordenada, paraula):
    """
    Retorna l'índex d'una paraula en una llista.
    Si la paraula no es troba, retorna -1.
    """
    if paraula in llista_ordenada:
        return llista_ordenada.index(paraula)
    else:
        return -1


paraules = ["casa", "cotxe", "gat", "llibre", "ordinador", "taula"]
print(index_paraula(paraules, "gat"))       
print(index_paraula(paraules, "ordinador"))  
print(index_paraula(paraules, "avió"))       


animals = ["elefant", "gos", "lleó", "tigre"]
print(index_paraula(animals, "lleó"))       
print(index_paraula(animals, "cavall"))      