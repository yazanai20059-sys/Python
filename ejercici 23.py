def crear_repetits(numero, caracter):
    """
    Retorna el caràcter repetit el número de vegades indicat.
    
    Args:
        numero (int): Nombre de vegades que es repeteix el caràcter
        caracter (str): Caràcter a repetir
    
    Returns:
        str: String amb el caràcter repetit
    """
    return caracter * numero


print(crear_repetits(5, "a"))  


print(crear_repetits(3, "x"))  


print(crear_repetits(7, "*"))  


print(crear_repetits(20, "b")) 


print(crear_repetits(10, "!")) 