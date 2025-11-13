opcio=int(input("""Introdueix una opcio: 
                1. suma
                2. multiplicacio
                3. divisio
                4. resta
                5. elevacio
                6. raiz
                7. tanto por ciento"""))
x = float(input("Introdueix un nombre: "))
y = float(input("Introdueix un nombre: "))
if opcio==1:
z = x + y
print("La suma de {} i {} és {}".format(x, y, z))
if opcio==2:
q = x * y
print("La multiplicacion de {} i {} és {}".format(x, y, q))
if opcio==3:
w = x / y
print("La division de {} i {} és {}".format(x, y, w))
if opcio==4:
e = x - y
print("La resta de {} i {} és {}".format(x, y, e))
if opcio==5:
r = x ** y
print("La elevacion de {} i {} és {}".format(x, y, r))
if opcio==6:
t = x // y
print("La raiz de {} i {} és {}".format(x, y, t))
if opcio==7:
o = x % y
print("el tanto por ciento de {} i {} és {}".format(x, y, o))