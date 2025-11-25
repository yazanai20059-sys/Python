def eliminarcapicua(llista):
    """
    Elimina el primer i el darrer element d'una llista.
    
    Paràmetres:
        llista: llista d'elements
    
    Retorna:
        Nova llista sense el primer i darrer element
    """
    if len(llista) <= 2:
        return []
    else:
        return llista[1:-1]
    
llista = ["h", "o", "l", "a"]
print(eliminarcapicua(llista))