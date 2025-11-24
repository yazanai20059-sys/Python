a = [1, 3 , 5, 7, 9, "a", "Capça", [2, 3, 4]]
for e in a:
    print(e)
for i in range(len(a)):
    print("la posicion {} te el valor {}".format(i,a[i]))
for i,e in enumerate(a):
    print("la psicion {} te el valor {}".format(i,e))
