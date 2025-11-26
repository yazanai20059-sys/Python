# Programa per imprimir la taula de multiplicar d'un número

# Demanar el número a l'usuari
while True:
    try:
        numero = int(input("Introdueix un número (entre 1 i 20): "))
        
        # Validar que el número estigui dins del rang
        if 1 <= numero <= 20:
            break
        else:
            print("Error: El número ha d'estar entre 1 i 20.")
    except ValueError:
        print("Error: Si us plau, introdueix un número vàlid.")

# Imprimir la taula de multiplicar
print(f"\n--- Taula de multiplicar del {numero} ---\n")

for i in range(1, 11):
    resultat = numero * i
    print(f"{numero} x {i:2d} = {resultat:3d}")

print("\n--- Fi de la taula ---")