def es_palindrom(paraula):
    """
    Retorna True si la paraula és un palíndrom, False en cas contrari.
    """
    paraula = paraula.lower()
    
    
    if len(paraula) <= 1:
        return True
    
    
    if paraula[0] != paraula[-1]:
        return False
    
    
    return es_palindrom(paraula[1:-1])

print(es_palindrom("radar"))    
print(es_palindrom("ara"))      
print(es_palindrom("civic"))    
print(es_palindrom("rallar"))   
print(es_palindrom("tapat"))    
print(es_palindrom("simis"))    
print(es_palindrom("refer"))    
print(es_palindrom("hola"))     
print(es_palindrom("Python"))   
print(es_palindrom("Anna"))     