def read_file_safely(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "Error: El fitxer no existeix."
    except IOError:
        return "Error: No s'ha pogut obrir el fitxer."
    
# Exemple d'ús
file_path = input("Introdueix la ruta del fitxer a llegir: ")
file_content = read_file_safely(file_path)
print(file_content)