import random

def llista_20_elements():
    """Retorna una llista de 20 elements aleatoris entre 1 i 100."""
    return [random.randint(1, 100) for i in range(20)]

def te_duplicats(llista):
    """Retorna True si la llista té duplicats, False si no."""
    return len(llista) != len(set(llista))

# Provar
llista = llista_20_elements()
print(f"Llista: {llista}")
print(f"Té duplicats? {'SÍ' if te_duplicats(llista) else 'NO'}")
print(f"Elements únics: {len(set(llista))}/20")