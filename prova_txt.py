l = [50, 100, 200]
with open("prova111.txt","a") as f:
    f.write(str(l))
with open("prova111.txt","r") as f:
    lineas = f.readlines() 
    lineas = [n[:-1] for n in lineas]
    print(lineas)
 
 
 
"""
with open("prova111.txt","r") as f:
    lineas = f.readlines() 
    lineas = [n[:-1] for n in lineas]
    print(lineas)"""
