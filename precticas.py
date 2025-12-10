



"""from functools import reduce
def add(y,x):
    return y+x
ln=[]
sortir="n"
while sortir!="s":
    numero = float(input ("\n posa nomero: "))
    ln.append(numero)
    sortir= input("\n vols sortir (s/n)")

sumap=reduce(add, [n for n in ln if n>0])
suman=reduce(add, [n for n in ln if n<0])
print(""suma positius {}
          suma negatius {} 
          mijana {}"".format(sumap, suman, (sumap+suman)/len(ln)))
sumaposetius=0
sumanegatius=0
nombrenomaro=0
sortir="no"
while sortir!="si":
    numero = float(input("posa un nomero: "))
    if numero>0:
        sumaposetius+=numero
    else:
        sumanegatius+=numero
    sortir=input("\n vols sortir? (si/no)")

print("
      suma de nobres positius {} 
      suma denobres negatius {}
      mitjana".format(sumaposetius, sumanegatius, (sumaposetius+sumanegatius) // nombrenomaro))
def convertir(ns):
    vocales = "aeiou"
    return [
        "".join(l.upper() if l.lower() not in vocales else l
                for l in n)
        for n in ns
    ]

n=["joan","miquel","manu"]
print(convertir(n))


p = [i for i in range (1,11)]
print (p)
s = [i**(i-1) for i in range(20) if i % 2 == 1]
print (s)
m = [2+i +1 for i in range (20)]
print (m)
l = [3, 4, 5, 6]
p = [1, 9, 2, 7, 11]
s = list(zip(l,p))
print(s)"""
