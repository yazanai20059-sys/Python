def elements_parells(llista):
    return [llista[i] for i in range(0, len(llista), 2)]
print(elements_parells(["papa", "mama", "germà", "germana", "tieta", "tiet"]))