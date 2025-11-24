# Demanar un número a l'usuari
num = int(input("Introdueix un número menor de 100: "))

# Verificar que el número sigui menor de 100
if num >= 100:
    print("El número ha de ser menor de 100!")
else:
    suma = 0
    print(f"Números utilitzats per {num}:", end=" ")
    
    # Començar des de num-4 i anar restant de 4 en 4
    i = num - 4
    
    while i > 0:
        print(f"{i}", end=" ")
        suma += i ** 2
        i -= 4
    
    print(f"\n\nSuma dels quadrats: {suma}")
    
    # Mostrar el càlcul detallat
    print("\nCàlcul detallat:")
    i = num - 4
    calcul = []
    while i > 0:
        calcul.append(f"{i}²")
        i -= 4
    print(" + ".join(calcul) + f" = {suma}")