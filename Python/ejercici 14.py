def menu_principal():
    opcio=0
    while opcio<1 or opcio>4:
        opcio=int(input("""Selecciona una operació:
                    1. calculadora decimal
                    2. calculadora real (flotant)
                    3. conversió de bases
                    4. sortir \n"""))
    return opcio
    

def menu_calculador():  
    opcio=0
    while opcio<0 or opcio>7:
        opcio=int(input("""Introdueix una opcio: 
                1. suma
                2. multiplicacio
                3. divisio
                4. resta
                5. elevacio
                6. raiz (divisió entera)
                7. tant per cent (modul)
                0. sortir \n"""))
    return opcio 


def calculadora_decimal(opcio):
    if 1 <= opcio <= 7:
        a = int(input("Introdueix el primer nombre: "))
        b = int(input("Introdueix el segon nombre: "))
    match(opcio):
        case 1:
            print("La suma és:", a + b)
        case 2:
            print("La multiplicació és:", a * b)
        case 3:
            print("La divisió és:", a / b)
        case 4:
            print("La resta és:", a - b)
        case 5:
            print("L'elevació és:", a ** b)
        case 6:
            print("La divisió entera és:", a // b)
        case 7:
            print("El tant per cent és:", a % b)
        case _:
            print("Sortint...")


def calculadora_real(opcio):
    if 1 <= opcio <= 7:
        a = float(input("Introdueix el primer nombre: "))
        b = float(input("Introdueix el segon nombre: "))
    match(opcio):
        case 1:
            print("La suma és:", a + b)
        case 2:
            print("La multiplicació és:", a * b)
        case 3:
            print("La divisió és:", a / b)
        case 4:
            print("La resta és:", a - b)
        case 5:
            print("L'elevació és:", a ** b)
        case 6:
            print("La divisió entera és:", a // b)
        case 7:
            print("El tant per cent és:", a % b)
        case _:
            print("Sortint...")




def menu_bases():
    print("""
Selecciona la base d'origen:
    1. Binari
    2. Octal
    3. Decimal
    4. Hexadecimal
""")
    op = 0
    while op < 1 or op > 4:
        op = int(input("Opció: "))
    return op


def base_to_decimal(valor, base):
    if base == 1:   # binari
        return int(valor, 2)
    elif base == 2: # octal
        return int(valor, 8)
    elif base == 3: # decimal
        return int(valor, 10)
    elif base == 4: # hexadecimal
        return int(valor, 16)


def decimal_to_all(n):
    print("\nConversions:")
    print("Binari:", bin(n)[2:])
    print("Octal:", oct(n)[2:])
    print("Decimal:", n)
    print("Hexadecimal:", hex(n)[2:].upper())
    print()


def conversio_bases():
    origen = menu_bases()
    valor = input("Introdueix el nombre a convertir: ")

    try:
        dec = base_to_decimal(valor, origen)
        decimal_to_all(dec)
    except ValueError:
        print(" Error: el nombre no és vàlid per aquesta base.")




op = 1
while op != 4:
    op = menu_principal()

    if op == 1:
        print("Has seleccionat la calculadora decimal\n")
        calculadora_decimal(menu_calculador())

    elif op == 2:
        print("Has seleccionat la calculadora real (flotant)\n")
        calculadora_real(menu_calculador())

    elif op == 3:
        print("Has seleccionat la conversió de bases\n")
        conversio_bases()

    else:
        print("Adéu!")
