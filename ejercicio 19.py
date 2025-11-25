def sumar_llista(lista):
    sumar = 0  
    for numero in lista:
        sumar += numero  
    return sumar

def multiplicar_llista(lista):
    resultado = 1  
    for numero in lista:
        resultado *= numero  
    return resultado

# programa principal
a=[1, 3, 5, 7, 6, 10]
print("La suma dels elements de la llista és {} val {}".format(a, sumar_llista(a))) 
print("La multiplicació dels elements de la llista és {} val {}".format(a, multiplicar_llista(a)))
