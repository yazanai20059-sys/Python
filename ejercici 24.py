def crear_punts(llista):
    """
    Funció que pinta per pantalla tants punts com el valor de cada número de la llista.
    Entre els elements de la llista hi ha un salt de línia.
    
    Paràmetre:
        llista: llista de números enters
    """
    for numero in llista:
        print('.' * numero)
crear_punts([2, 3, 4, 1, 5, 6, 2, 7])