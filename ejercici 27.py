def paraula_mes_llarga(llista_paraules):
    """
    Retorna la paraula més llarga d'una llista de paraules.
    
    Args:
        llista_paraules: Llista de strings
        
    Returns:
        La paraula amb més caràcters
    """
    paraula_llarga = llista_paraules[0]
    
    for paraula in llista_paraules:
        if len(paraula) > len(paraula_llarga):
            paraula_llarga = paraula
    
    return paraula_llarga

print(paraula_mes_llarga(["casa", "cotxe", "bicicleta", "avió"]))  
print(paraula_mes_llarga(["groc", "vermell", "blau", "verd"]))      
print(paraula_mes_llarga(["sol", "lluna", "estrella"]))          
print(paraula_mes_llarga(["a", "ab", "abc", "abcd"]))            