def esta_ordenada(llista):
    """
    Determina si una llista està ordenada de forma ascendent, descendent o no està ordenada.
    
    Args:
        llista: Llista de números a comprovar
        
    Returns:
        str: Missatge indicant l'estat d'ordenació
    """
    if len(llista) <= 1:
        return "està ordenada de forma ascendent"
    
    # Comprovem si està ordenada ascendent
    ascendent = True
    for i in range(len(llista) - 1):
        if llista[i] > llista[i + 1]:
            ascendent = False
            break
    
    if ascendent:
        return "està ordenada de forma ascendent"
    
    # Comprovem si està ordenada descendent
    descendent = True
    for i in range(len(llista) - 1):
        if llista[i] < llista[i + 1]:
            descendent = False
            break
    
    if descendent:
        return "està ordenada de forma descendent"
    
    return "no està ordenada"

# Proves amb diferents llistes
print("=" * 50)
print("PROVES DE LA FUNCIÓ esta_ordenada()")
print("=" * 50)

# Casos d'ordre descendent
print("\n--- ORDRE DESCENDENT ---")
print(f"esta_ordenada([3, 2, 1]): {esta_ordenada([3, 2, 1])}")
print(f"esta_ordenada([10, 5, 0, -5]): {esta_ordenada([10, 5, 0, -5])}")
print(f"esta_ordenada([100, 50, 25]): {esta_ordenada([100, 50, 25])}")

# Casos d'ordre ascendent
print("\n--- ORDRE ASCENDENT ---")
print(f"esta_ordenada([4, 5, 6]): {esta_ordenada([4, 5, 6])}")
print(f"esta_ordenada([1, 2, 3, 4, 5]): {esta_ordenada([1, 2, 3, 4, 5])}")
print(f"esta_ordenada([-5, 0, 5, 10]): {esta_ordenada([-5, 0, 5, 10])}")

# Casos no ordenats
print("\n--- NO ORDENADA ---")
print(f"esta_ordenada([1, 3, 2]): {esta_ordenada([1, 3, 2])}")
print(f"esta_ordenada([5, 2, 8, 1]): {esta_ordenada([5, 2, 8, 1])}")
print(f"esta_ordenada([3, 3, 1, 5]): {esta_ordenada([3, 3, 1, 5])}")

# Casos especials
print("\n--- CASOS ESPECIALS ---")
print(f"esta_ordenada([5]): {esta_ordenada([5])}")
print(f"esta_ordenada([]): {esta_ordenada([])}")
print(f"esta_ordenada([5, 5, 5]): {esta_ordenada([5, 5, 5])}")
print(f"esta_ordenada([1, 1, 2, 2, 3]): {esta_ordenada([1, 1, 2, 2, 3])}")