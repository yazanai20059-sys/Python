def calcular_pes(t, llista):
    i=0
    j=t-1
    pivan = 0
    ppau = 0
    pmax = 0
    while i<=j+1:
        if pivan<ppau:
            pivan += llista [i]
            i +=1
        elif pivan>ppau:
            ppau += llista [j]
            j -=1
        else:
            pmax = pivan
            pivan += llista [i]
            i +=1
            ppau += llista [j]
            j -=1
    return pmax

n = int(input())
for _ in range(n):
    np= int(input())
    lp= list(map(int,input().split()))
    pm= calcular_pes (np, lp)
    print(pm)