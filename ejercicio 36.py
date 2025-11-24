def es_de_traspas(any):
    """
    Determina si un any és de traspàs o no.
    
    Un any és de traspàs si:
    - És divisible per 4 I
    - NO és divisible per 100, EXCEPTE si també és divisible per 400
    
    Args:
        any (int): L'any a verificar
    
    Returns:
        bool: True si l'any és de traspàs, False en cas contrari
    """
    if any % 400 == 0:
        return True
    elif any % 100 == 0:
        return False
    elif any % 4 == 0:
        return True
    else:
        return False
    

print(f"2024 és de traspàs? {es_de_traspas(2024)}")  
print(f"2023 és de traspàs? {es_de_traspas(2023)}")  
print(f"1900 és de traspàs? {es_de_traspas(1900)}")  
print(f"2000 és de traspàs? {es_de_traspas(2000)}")  
print(f"2100 és de traspàs? {es_de_traspas(2100)}")  
print(f"2020 és de traspàs? {es_de_traspas(2020)}")  