# Demanar un número a l'usuari
numero = input("Introdueix un número: ")

# Sumar els dígits
suma = 0
for digit in numero:
    if digit.isdigit():  # Ignorar el signe negatiu si n'hi ha
        suma += int(digit)

# Determinar si és parell o senar
if suma % 2 == 0:
    resultat = "parell"
else:
    resultat = "senar"

# Mostrar el resultat
print(f"La suma dels dígits de {numero} és {suma}")
print(f"El resultat és {resultat}")