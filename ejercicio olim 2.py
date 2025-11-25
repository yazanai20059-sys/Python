"""llegir el numaro de frases i ses frases
a cada frase substituimos les consonants per una majuscula
imprimir ses frases modificades"""

def llegir_frases(n):
    llista = list()
    for i in range(n):
        llista.append(input(""))
    return llista

def ecriure_frases(llista):
    for e in llista: 
        print(e)

def convertir_frases(s):
    vocals = "aeiouAEIOU"
    llista = list(s)
    for i,e in enumerate(s):
        if e not in vocals:
            llista[i] = e.upper()
    return "".join(llista)


n = int(input(""))
llista=llegir_frases(n)
for i,e in enumerate(llista):
    llista[i]= convertir_frases(e)