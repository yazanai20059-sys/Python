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

print(sumar_llista([5, 6, 7, 8])) 


print(multiplicar_llista([1, 2, 3, 4]))  
