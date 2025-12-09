def comptar_majuscules(cadena):
    """
    Compta el nombre de lletres majúscules en una cadena.
    
    Paràmetres:
        cadena (str): La cadena a analitzar
    
    Retorna:
        int: El nombre de lletres majúscules
    """
    comptador = 0
    for caracter in cadena:
        if caracter.isupper():
            comptador += 1
    return comptador



print("\nPROVES DE LA FUNCIÓ")


text1 = "Hola Món!"
print(f"Text: '{text1}'")
print(f"Majúscules: {comptar_majuscules(text1)}")
print()


text2 = "PYTHON"
print(f"Text: '{text2}'")
print(f"Majúscules: {comptar_majuscules(text2)}")
print()


text3 = "programació"
print(f"Text: '{text3}'")
print(f"Majúscules: {comptar_majuscules(text3)}")
print()


text4 = "Codi123 i Símbols@#"
print(f"Text: '{text4}'")
print(f"Majúscules: {comptar_majuscules(text4)}")
print()


text5 = ""
print(f"Text: '{text5}'")
print(f"Majúscules: {comptar_majuscules(text5)}")
print()


text6 = "La Universitat de Barcelona és UB"
print(f"Text: '{text6}'")
print(f"Majúscules: {comptar_majuscules(text6)}")