def filtrar_paraules(llista_paraules, x):
    """
    Retorna totes les paraules que tinguin més d'x caràcters.
    
    Args:
        llista_paraules: llista de paraules (strings)
        x: número mínim de caràcters
    
    Returns:
        llista amb les paraules que tenen més d'x caràcters
    """
    paraules_filtrades = []
    for paraula in llista_paraules:
        if len(paraula) > x:
            paraules_filtrades.append(paraula)
    return paraules_filtrades


def paraula_mes_llarga(llista_paraules):
    """
    Retorna la paraula amb més caràcters de la llista.
    
    Args:
        llista_paraules: llista de paraules (strings)
    
    Returns:
        la paraula més llarga
    """
    if not llista_paraules:  # Si la llista està buida
        return None
    
    mes_llarga = llista_paraules[0]
    for paraula in llista_paraules:
        if len(paraula) > len(mes_llarga):
            mes_llarga = paraula
    return mes_llarga


# Exemples d'ús:
print("FILTRAR PARAULES")
paraules = ["Hola", "Ramis", "IES", "Paraula", "Python"]
print(f"Paraules originals: {paraules}")
print(f"Paraules amb més de 3 caràcters: {filtrar_paraules(paraules, 3)}")
print(f"Paraules amb més de 5 caràcters: {filtrar_paraules(paraules, 5)}")

print("\nPARAULA MÉS LLARGA")
paraules2 = ["Hola", "Ramis", "IES", "Paraula"]
print(f"Paraules: {paraules2}")
print(f"Paraula més llarga: {paraula_mes_llarga(paraules2)}")