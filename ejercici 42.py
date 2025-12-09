def comptar_digits_string(numero):
    """Compta els dígits d'un número convertint-lo a string"""
    return len(str(abs(numero)))

# Programa principal
while True:
    try:
        numero = int(input("Introdueix un número (entre 1 i 900000): "))
        
        if 1 <= numero <= 900000:
            digits = comptar_digits_string(numero)
            print(f"El número {numero} té {digits} dígits")
            break
        else:
            print("❌ El número ha d'estar entre 1 i 900000")
    except ValueError:
        print("❌ Si us plau, introdueix un número vàlid")