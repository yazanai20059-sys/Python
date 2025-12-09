# a = [1, 3 , 5, 7, 9, "a", "Capça", [2, 3, 4]]
a = [5, 3, 8, 1, 4, 11]
for i in range(len(a)):
    a[i]= str(a[i])
print(" ".join(a))




"""
b = a.copy()
b[0]=1000000
print(a)
print(a[::-1]) # imprime la llista invertida sense modificar la llista original
print(a)
print(a.reverse()) # modifica la llista original, pero no retorna res
print(a)
a.sort()
print(a)
for i in range(len(a)):
    a[i]= str(a[i])
a.sort()
print(a)
a = [1, 3 , 5, 7, 9, "a", "Capça", [2, 3, 4]]
for e in a:
    if a.count(e) > 1:
        print(e)
        c = set(a)
for e in a:
    print(e)
for i in range(len(a)):
    print("la posicion {} te el valor {}".format(i,a[i]))
for i,e in enumerate(a):
    print("la psicion {} te el valor {}".format(i,e))
a.append("final")
a.append([10, 20, 30])
a.extend([83, "cadena nova", [1, 2, 3]])
print(a)"""
