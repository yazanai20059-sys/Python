def superposicio(llista1, llista2):
    for element in llista1:
        if element in llista2:
            return True
    return False

# Proves de la funció
print(superposicio([1, 2, 3], [3, 4, 5]))  
print(superposicio([1, 2, 3], [4, 5, 6]))  
print(superposicio(['a', 'b'], ['c', 'a']))  
print(superposicio([], [1, 2, 3]))  
print(superposicio([1, 2], []))  