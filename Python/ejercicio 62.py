
from functools import reduce
def Passar_a_Numero(llista):
    return reduce(lambda x, y: x * 10 + y, llista)

llista = [9, 4, 6, 5]
numero = Passar_a_Numero(llista)
print(numero)  