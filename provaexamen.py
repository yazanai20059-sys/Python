"""a = int(input("edad: "))
print ("Hola,tens {} años".format(a))
if a<18:
    print("menor de edad")
else :
    print("major de edad")
if a%2==0:
    print("es parell")
else:
    print("es imparell")
if a%5==0:
    print("es multipla de 5")
else:
    print("no es multipla de 5")
if a>=0 and a<=10:
    print("esta entre 0 y 10 ")
elif a>=11 and a<=20:
    print("esta entre 11 y 20")
else :
    print("major que 20")
nom = input("nom: ")
b = "no"
if "a" in nom or "e" in nom:
    b="si" 
print("Hola {}, tens {} caractars, {} tens vocals".format(nom,len(nom),b))

def vocals():
    a = 0
    for e in nom:
        if e in "aeiou":
            a= a + 1
    return a"""