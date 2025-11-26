def contiene_o(p):
    if 'o' in p:
        return True
    else:
        return False

palabra = input("Ingrese una palabra: ")
if contiene_o(palabra):
    print("La palabra contiene la letra 'o'.")
else:
    print("La palabra no contiene la letra 'o'.")
