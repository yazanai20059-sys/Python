def validar_capital():
    """Valida que el capital estigui entre 50000€ i 800000€"""
    while True:
        try:
            capital = float(input("Introdueix el capital inicial (mínim 50000€, màxim 800000€): "))
            if 50000 <= capital <= 800000:
                return capital
            else:
                print("❌ Error: El capital ha d'estar entre 50000€ i 800000€")
        except ValueError:
            print("❌ Error: Introdueix un número vàlid")

def validar_interes():
    """Valida que l'interès estigui entre 0.5% i 13%"""
    while True:
        try:
            interes = float(input("Introdueix l'interès anual (mínim 0.5%, màxim 13%): "))
            if 0.5 <= interes <= 13:
                return interes
            else:
                print("❌ Error: L'interès ha d'estar entre 0.5% i 13%")
        except ValueError:
            print("❌ Error: Introdueix un número vàlid")

def validar_anys():
    """Valida que els anys estiguin entre 3 i 40"""
    while True:
        try:
            anys = int(input("Introdueix el número d'anys (mínim 3, màxim 40): "))
            if 3 <= anys <= 40:
                return anys
            else:
                print("❌ Error: Els anys han d'estar entre 3 i 40")
        except ValueError:
            print("❌ Error: Introdueix un número enter vàlid")

def calcular_capital_final(capital_inicial, interes, anys):
    """Calcula el capital final amb la fórmula d'interès compost"""
    capital_final = capital_inicial * (1 + interes / 100) ** anys
    return capital_final

def main():
    print("=" * 60)
    print("CALCULADORA DE CAPITAL FINAL AMB INTERÈS COMPOST")
    print("=" * 60)
    print()
    
    # Demanar dades a l'usuari
    capital_inicial = validar_capital()
    interes = validar_interes()
    anys = validar_anys()
    
    # Calcular capital final
    capital_final = calcular_capital_final(capital_inicial, interes, anys)
    
    # Mostrar resultats
    print()
    print("=" * 60)
    print("RESULTATS")
    print("=" * 60)
    print(f"Capital inicial:  {capital_inicial:,.2f}€")
    print(f"Interès anual:    {interes}%")
    print(f"Període:          {anys} anys")
    print(f"Capital final:    {capital_final:,.2f}€")
    print(f"Benefici total:   {capital_final - capital_inicial:,.2f}€")
    print("=" * 60)

# Executar el programa
if __name__ == "__main__":
    main()