def hi_ha_duplicats(llista):
    return len(llista) != len(set(llista))


print("PROVES DE LA FUNCIÓ hi_ha_duplicats()\n")


llista1 = [1, 2, 3, 4, 2, 5]
print(f"Llista: {llista1}")
print(f"Té duplicats? {hi_ha_duplicats(llista1)}")
print()


llista2 = [1, 2, 3, 4, 5]
print(f"Llista: {llista2}")
print(f"Té duplicats? {hi_ha_duplicats(llista2)}")
print()


llista3 = [5, 5, 5, 5]
print(f"Llista: {llista3}")
print(f"Té duplicats? {hi_ha_duplicats(llista3)}")
print()

llista_original = [1, 2, 3, 2, 4]
print(f"Llista original abans: {llista_original}")
resultat = hi_ha_duplicats(llista_original)
print(f"Resultat: {resultat}")
print(f"Llista original després: {llista_original}")
print(f"La llista s'ha mantingut intacta? {llista_original == [1, 2, 3, 2, 4]}")