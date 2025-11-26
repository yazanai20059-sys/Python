def safe_divide(a, b):
    if b == 0:
        return "Error: Divisió per zero no permesa."
    return a / b 

# Exemple d'ús
num1 = int(input("Introdueix un dividend: "))
num2 = int(input("Introdueix un divisor: "))
result = safe_divide(num1, num2)
print(f'Resultat de la divisió: {result}')   