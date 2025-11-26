def gran_de_tres(a, b, c):
    a = int(a)
    b = int(b) 
    c = int(c)
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


print(gran_de_tres(input("Dame un numero: "), input("Dame un numero: "), input("Dame un numero: ")))
