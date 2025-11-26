def crear_llista_fitxer(nom_fitxer):
    """
    Llegeix un fitxer i transforma cada paraula en un element d'una llista.
    
    Paràmetres:
        nom_fitxer (str): el nom del fitxer a llegir
    
    Retorna:
        list: llista amb totes les paraules del fitxer
    """
    try:
        llista_paraules = []
        
        with open(nom_fitxer, 'r', encoding='utf-8') as fitxer:
            # Llegim tot el contingut del fitxer
            contingut = fitxer.read()
            
            # Separem per paraules (espais, salts de línia, etc.)
            llista_paraules = contingut.split()
        
        return llista_paraules
    
    except FileNotFoundError:
        print(f"Error: El fitxer '{nom_fitxer}' no existeix.")
        return []
    except Exception as e:
        print(f"Error en llegir el fitxer: {e}")
        return []
    
# Primer, creem un fitxer de prova
def crear_fitxer_prova():
    """Crea un fitxer de prova amb text"""
    with open('prova.txt', 'w', encoding='utf-8') as f:
        f.write("Hola món!\n")
        f.write("Això és una prova.\n")
        f.write("Python és genial per programar.")

# Creem el fitxer de prova
crear_fitxer_prova()


print("=== PROVA 1: Funció principal ===")
resultat = crear_llista_fitxer('prova.txt')
print(f"Llista de paraules: {resultat}")
print(f"Nombre total de paraules: {len(resultat)}")


print("\n=== PROVA 2: Versió alternativa ===")
resultat2 = crear_llista_fitxer('prova.txt')
print(f"Llista de paraules: {resultat2}")


print("\n=== PROVA 3: Fitxer inexistent ===")
resultat3 = crear_llista_fitxer('no_existeix.txt')
print(f"Resultat: {resultat3}")

