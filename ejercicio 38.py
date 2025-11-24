import random

def generar_codi():
    """Genera un codi secret de 4 xifres"""
    return [random.randint(0, 9) for _ in range(4)]

def demanar_intent():
    """Demana a l'usuari que introdueixi un codi de 4 xifres"""
    while True:
        entrada = input("Introdueix un codi de 4 xifres: ")
        
        # Validar que siguin 4 dígits
        if len(entrada) == 4 and entrada.isdigit():
            return [int(digit) for digit in entrada]
        else:
            print(" Error! Has d'introduir exactament 4 xifres (0-9)")

def comprovar_intent(codi_secret, intent):
    """
    Comprova l'intent i retorna:
    - encerts: números en la posició correcta
    - coincidencies: números correctes però en posició incorrecta
    """
    encerts = 0
    coincidencies = 0
    
    codi_temp = codi_secret.copy()
    intent_temp = intent.copy()
    
    # Primer, comptem els encerts (posició correcta)
    for i in range(4):
        if intent[i] == codi_secret[i]:
            encerts += 1
            codi_temp[i] = None
            intent_temp[i] = None
    
    # Després, comptem les coincidències (número correcte, posició incorrecta)
    for i in range(4):
        if intent_temp[i] is not None:
            if intent_temp[i] in codi_temp:
                coincidencies += 1
                # Eliminem el número trobat per evitar doble comptatge
                index = codi_temp.index(intent_temp[i])
                codi_temp[index] = None
    
    return encerts, coincidencies

def mostrar_pista(encerts, coincidencies):
    """Mostra una pista visual amb l'estat de l'intent"""
    print(f"   ✓ Encerts (posició correcta): {encerts}")
    print(f"   ○ Coincidències (número correcte): {coincidencies}")

def jugar():
    """Funció principal del joc"""
    print("=" * 50)
    print("  MASTERMIND - Versió Simplificada  🎮")
    print("=" * 50)
    print("\n REGLES:")
    print("   • Has d'endevinar un codi secret de 4 xifres")
    print("   • Cada xifra pot ser del 0 al 9")
    print("   • Després de cada intent, et diré:")
    print("     - Quants números has encertat (posició correcta)")
    print("     - Quants coincideixen però estan mal situats")
    print("\n" + "=" * 50)
    
    codi_secret = generar_codi()
    intents = 0
    max_intents = 10
    
    # Per debug (elimina aquesta línia si vols jugar sense trampes)
    # print(f"[DEBUG] Codi secret: {codi_secret}")
    
    print(f"\n Tens {max_intents} intents per endevinar el codi!")
    print("Que comenci el joc!\n")
    
    while intents < max_intents:
        intents += 1
        print(f"--- Intent {intents}/{max_intents} ---")
        
        intent = demanar_intent()
        encerts, coincidencies = comprovar_intent(codi_secret, intent)
        
        if encerts == 4:
            print("\n" + "=" * 50)
            print(" FELICITATS! Has endevinat el codi! 🎉")
            print(f" Codi secret: {''.join(map(str, codi_secret))}")
            print(f" Nombre d'intents: {intents}")
            print("=" * 50)
            return
        else:
            mostrar_pista(encerts, coincidencies)
            print()
    
    print("\n" + "=" * 50)
    print(" Game Over! Has esgotat tots els intents")
    print(f" El codi secret era: {''.join(map(str, codi_secret))}")
    print("=" * 50)

def main():
    """Funció principal amb opció de jugar més d'una vegada"""
    while True:
        jugar()
        
        resposta = input("\n¿Vols jugar una altra partida? (s/n): ").lower()
        if resposta != 's':
            print("\n Gràcies per jugar! Fins aviat!")
            break
        print("\n" * 2)

if __name__ == "__main__":
    main()