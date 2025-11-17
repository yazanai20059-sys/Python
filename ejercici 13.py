def menu_principal():
    opcio=0
    while opcio<1 or opcio>3:
        opcio=int(input("""Selecciona una operació:
                    1. calculadora decimal
                    2. calculadora real(flotant)
                    3. sortir \n"""))
    if opcio>0 and opcio<4:
       return opcio 
    else:
       print("Opcio no correcta, torna a intentar-ho! \n")
       
    
def menu_calculador():  
    opcio=0
    while opcio<1 or opcio>7:
        opcio=int(input("""Introdueix una opcio: 
                1. suma
                2. multiplicacio
                3. divisio
                4. resta
                5. elevacio
                6. raiz
                7. tanto por ciento
                0. sortir \n"""))
    if opcio>0 and opcio<8:
       return opcio 
    else:
       print("Opcio no correcta, torna a intentar-ho! \n")

def calculadora_decimal(opcio):
    if opcio>0 and opcio<8:
        a = int(input("Introdueix el premer nombre: "))
        b = int(input("Introdueix el segon nombre: "))
    match(opcio):
        case 1:
            # suma
            print("estic fent la suma \n")
            c = a + b
            print("La suma de {} i {} és {}".format(a, b, c))
        case 2:
            # multiplicacio
            print("estic fent la multiplicacio \n")
            c = a * b
            print("La multiplicacion de {} i {} és {}".format(a, b, c))
        case 3:
            # divisio
            print("estic fent la divisio \n")
            c = a // b
            print("La division de {} i {} és {}".format(a, b, c))
        case 4:
            # resta
            print("estic fent la resta \n")
            c = a - b
            print("La resta de {} i {} és {}".format(a, b, c))
        case 5:
            # elevacio
            print("estic fent la elevacio \n")
            c = a ** b4 days ago
            print("La elevacion de {} i {} és {}".format(a, b, c))
        case 6:
            # raiz
            print("estic fent la raiz \n")
            c = a // b
            print("La raiz de {} i {} és {}".format(a, b, c))
        case 7:
            # tanto por ciento
            print("estic fent el tanto por ciento \n")
            c = a % b
            print("el tanto por ciento4 days ago de {} i {} és {}".format(a, b, c))
        case _:
            # opcio no valida
            print("gracias , fins aviat \n")
        
def calculadora_real(opcio):
    if opcio>0 and opcio<8:
        a = float(input("Introdueix el premer nombre: "))
        b = float(input("Introdueix el segon nombre: "))
    match(opcio):
        case 1:
            # suma
            print("estic fent la suma \n")
            c = a + b
            print("La suma de {} i {} és {}".format(a, b, c))
        case 2:
            # multiplicacio
            print("estic fent la multiplicacio \n")
            c = a * b
            print("La multiplicacion de {} i {} és {}".format(a, b, c))
        case 3:
            # divisio
            print("estic fent la divisio \n")
            c = a / b
            print("La division de {} i {} és {}".format(a, b, c))
        case 4:
            # resta
            print("estic fent la resta \n")
            c = a - b
            print("La resta de {} i {} és {}".format(a, b, c))
        case 5:
            # elevacio
            print("estic fent la elevacio \n")
            c = a ** b
            print("La elevacion de {} i {} és {}".format(a, b, c))
        case 6:
            # raiz
            print("estic fent la raiz \n")
            c = a // b
            print("La raiz de {} i {} és {}".format(a, b, c))
        case 7:
            # tanto por ciento
            print("estic fent el tanto por ciento \n")
            c = a % b
            print("el tanto por ciento de {} i {} és {}".format(a, b, c))
        case _:
            # opcio no valida
            print("gracias , fins aviat \n")

# Programa principal
op = 1
while op!= 0:
    op = menu_principal()
    if op==1:
        # calculadora decimal
        print("Has seleccionat la calculadora decimal \n")
        calculadora_decimal(menu_calculador())
    elif op==2:
        # calculadora real(flotant)
        print("Has seleccionat la calculadora real(flotant) \n")
        calculadora_real(menu_calculador())
    else:
        print("adios! \n")
        op=0

    print("Canvi fet a posta per a poder pujar-ho al repositori")