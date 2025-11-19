def contiene_o(palabra):
    if 'o' in palabra:
        return True
    else:
        return False

palabra = input("Ingresa una palabra: ")

resultado = contiene_o(palabra)
if resultado:
    print("true")
else:
    print("false")