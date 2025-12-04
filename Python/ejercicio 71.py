def llegir_fitxer(nom_fitxer):
    try:
        # Intentem obrir el fitxer en mode lectura
        with open(nom_fitxer, 'r', encoding='utf-8') as fitxer:
            contingut = fitxer.read()  # Llegim tot el contingut del fitxer
            
            # Comprovem si el fitxer està buit
            if contingut == "":
                print("El fitxer '{}' està buit.".format(nom_fitxer))
                return None  # Retornem None per indicar que el fitxer està buit
            
            return contingut  # Retornem el contingut llegit
    except FileNotFoundError:
        # Captura si el fitxer no existeix
        print("Error: El fitxer '{}' no s'ha trobat.".format(nom_fitxer))
        return None
    except IOError as e:
        # Captura altres errors d'entrada/sortida (per exemple, problemes de permisos)
        print("Error d'entrada/sortida al llegir el fitxer '{}': {}".format(nom_fitxer, e))
        return None
    except Exception as e:
        # Captura qualsevol altre error inesperat
        print("S'ha produït un error inesperat al llegir el fitxer '{}': {}".format(nom_fitxer, e))
        return None

# Exemple d'ús
fitxer_llegit = llegir_fitxer('/home/youssef/AO/Python/prova.txt')
if fitxer_llegit:
    print("Contingut del fitxer:")
    print(fitxer_llegit)
else:
    print("No s'ha pogut llegir el fitxer.")