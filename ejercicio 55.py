def mostrar_parells():
    """Mostra tots els números parells fins a 100"""
    print("\n✓ Números PARELLS:")
    parells = [num for num in range(2, 101, 2)]
    print(", ".join(map(str, parells)))
    print(f"\nTotal de números parells: {len(parells)}")

def mostrar_senars():
    """Mostra tots els números senars fins a 100"""
    print("\n✓ Números SENARS:")
    senars = [num for num in range(1, 101, 2)]
    print(", ".join(map(str, senars)))
    print(f"\nTotal de números senars: {len(senars)}")

# Programa principal
print("=" * 50)
print("    PROGRAMA DE NÚMEROS PARELLS I SENARS")
print("=" * 50)

mostrar_parells()
print("\n" + "-" * 50)
mostrar_senars()

print("\n" + "=" * 50)