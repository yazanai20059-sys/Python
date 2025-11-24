# Demanem dues paraules a l'usuari
paraula1 = input("Introdueix la primera paraula: ").lower()
paraula2 = input("Introdueix la segona paraula: ").lower()

# Comprovem si tenen almenys 3 lletres per evitar errors
if len(paraula1) >= 3 and len(paraula2) >= 3:
    # Comprovem si coincideixen les 3 últimes lletres
    if paraula1[-3:] == paraula2[-3:]:
        print("Les paraules rimen!")
    # Comprovem si coincideixen les 2 últimes lletres
    elif paraula1[-2:] == paraula2[-2:]:
        print("Les paraules rimen una mica.")
    else:
        print("Les paraules no rimen.")
elif len(paraula1) >= 2 and len(paraula2) >= 2:
    # Si tenen menys de 3 lletres però almenys 2, només comprovem 2 lletres
    if paraula1[-2:] == paraula2[-2:]:
        print("Les paraules rimen una mica.")
    else:
        print("Les paraules no rimen.")
else:
    print("Les paraules són massa curtes per comparar.")

