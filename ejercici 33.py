# FUNCIÓ 1: nums_que_comencen_per()
def nums_que_comencen_per(llista_noms):
    """
    Compta quants noms de la llista comencen per la lletra 'a' (majúscula o minúscula)
    
    Paràmetres:
        llista_noms: llista de strings amb noms
    
    Retorna:
        int: nombre de noms que comencen per 'a'
    """
    comptador = 0
    for nom in llista_noms:
        if nom and nom[0].lower() == 'a':  
            comptador += 1
    return comptador


# FUNCIÓ 2: mostrar_majors_que()
def mostrar_majors_que(tupla_nums, valor_referencia):
    """
    Mostra tots els números de la tupla que són majors que el valor de referència
    
    Paràmetres:
        tupla_nums: tupla de números enters
        valor_referencia: valor enter per comparar
    """
    print(f"Números majors que {valor_referencia}:")
    trobats = False
    for num in tupla_nums:
        if num > valor_referencia:
            print(num)
            trobats = True
    
    if not trobats:
        print("Cap número és major que", valor_referencia)


# PROGRAMA PRINCIPAL PER PROVAR LES FUNCIONS

print("=" * 50)
print("PROVA DE LA FUNCIÓ nums_que_comencen_per()")
print("=" * 50)

# Exemple amb llista de noms
noms = ["Anna", "Berta", "Carles", "Albert", "David", "andrea", "ALEIX"]
resultat = nums_que_comencen_per(noms)
print(f"Llista de noms: {noms}")
print(f"Nombres que comencen per 'a': {resultat}")

print("\n" + "=" * 50)
print("PROVA DE LA FUNCIÓ mostrar_majors_que()")
print("=" * 50)

# Programa per introduir valors i trobar majors de 18
print("\nIntrodueix edats (escriu 'fi' per acabar):")
llista_edats = []

while True:
    entrada = input("Introdueix una edat: ")
    
    if entrada.lower() == 'fi':
        break
    
    try:
        edat = int(entrada)
        llista_edats.append(edat)
    except ValueError:
        print("Si us plau, introdueix un número enter o 'fi' per acabar")

# Convertir la llista a tupla
tupla_edats = tuple(llista_edats)

print(f"\nEdats introduïdes: {tupla_edats}")
print()
mostrar_majors_que(tupla_edats, 18)


# ALTRES EXEMPLES
print("\n" + "=" * 50)
print("ALTRES EXEMPLES")
print("=" * 50)

# Exemple 2 amb nombres
numeros = (5, 12, 18, 25, 30, 8, 15, 22)
print(f"\nTupla de números: {numeros}")
mostrar_majors_que(numeros, 18)

print()
mostrar_majors_que(numeros, 50)