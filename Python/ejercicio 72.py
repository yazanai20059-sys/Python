fitxer_path = '/home/hola/Insti/AO/Prova/Ex12.txt'


try:
    with open(fitxer_path, 'r') as file:
        noms = file.readlines()

    noms = [nom.strip() for nom in noms]

    print(noms)
except FileNotFoundError:
    print("Error: El fitxer {} no s'ha trobat.".format(fitxer_path))