import random

# Llista de paraules possibles (totes de 5 lletres)
PARAULES = [
    "CASES", "GATOS", "LLIBR", "TAULA", "CADIRA", "LLAPIS",
    "PAPEL", "AIGUA", "FULLA", "ARBRE", "FLORS", "PLATJ",
    "MONTA", "CIELO", "TERRA", "FUSTA", "PEDRA", "METRO",
    "TENDA", "PORTA", "CAIXA", "PLATA", "LLUNA", "ESTIU"
]

def selecciona_paraula():
    """
    Selecciona una paraula aleatòria de la llista
    Returns:
        paraula en majúscules
    """
    return random.choice(PARAULES).upper()

def comprova_lletra(paraula_secreta, intent, posicio):
    """
    Comprova l'estat d'una lletra en una posició
    Args:
        paraula_secreta: la paraula a endevinar
        intent: la paraula intentada
        posicio: posició de la lletra a comprovar
    Returns:
        '🟩' si la lletra és correcta i en posició correcta
        '🟨' si la lletra existeix però en altra posició
        '⬜' si la lletra no existeix
    """
    lletra_intent = intent[posicio]
    lletra_secreta = paraula_secreta[posicio]
    
    if lletra_intent == lletra_secreta:
        return '🟩'  # Correcta i en posició correcta
    elif lletra_intent in paraula_secreta:
        return '🟨'  # Existeix però en altra posició
    else:
        return '⬜'  # No existeix

def mostra_resultat(paraula_secreta, intent):
    """
    Mostra el resultat visual d'un intent
    Args:
        paraula_secreta: la paraula a endevinar
        intent: la paraula intentada
    Returns:
        String amb els quadrats de colors
    """
    resultat = ""
    for i in range(len(intent)):
        resultat += comprova_lletra(paraula_secreta, intent, posicio=i)
    return resultat

def es_valid_intent(intent):
    """
    Comprova si l'intent és vàlid
    Args:
        intent: paraula intentada
    Returns:
        True si és vàlid, False altrament
    """
    if len(intent) != 5:
        print("❌ La paraula ha de tenir 5 lletres!")
        return False
    
    if not intent.isalpha():
        print("❌ Només es permeten lletres!")
        return False
    
    return True

def mostra_historial(historial):
    """
    Mostra tots els intents anteriors
    Args:
        historial: llista de tuples (intent, resultat)
    """
    print("\n📜 Historial d'intents:")
    print("-" * 30)
    for i, (intent, resultat) in enumerate(historial, 1):
        print(f"{i}. {intent}  {resultat}")
    print("-" * 30)

def mostra_estadistiques(partides_jugades, partides_guanyades, intents_totals):
    """
    Mostra estadístiques del jugador
    """
    if partides_jugades == 0:
        print("\n📊 Encara no has jugat cap partida!")
        return
    
    percentatge = (partides_guanyades / partides_jugades) * 100
    mitjana_intents = intents_totals / partides_guanyades if partides_guanyades > 0 else 0
    
    print("\n" + "="*40)
    print("📊 ESTADÍSTIQUES")
    print("="*40)
    print(f"🎮 Partides jugades: {partides_jugades}")
    print(f"🏆 Partides guanyades: {partides_guanyades}")
    print(f"💔 Partides perdudes: {partides_jugades - partides_guanyades}")
    print(f"📈 Percentatge d'èxit: {percentatge:.1f}%")
    if partides_guanyades > 0:
        print(f"🎯 Mitjana d'intents: {mitjana_intents:.1f}")
    print("="*40)

def juga_partida():
    """
    Executa una partida completa del joc
    Returns:
        tuple (ha_guanyat, nombre_intents)
    """
    paraula_secreta = selecciona_paraula()
    intents_restants = 6
    historial = []
    ha_guanyat = False
    
    print("\n" + "="*50)
    print("🎮 JOC D'ENDEVINAR PARAULES")
    print("="*50)
    print("\n📋 Instruccions:")
    print("   🟩 = Lletra correcta en posició correcta")
    print("   🟨 = Lletra correcta en posició incorrecta")
    print("   ⬜ = Lletra no existeix")
    print("\n🎯 Tens 6 intents per endevinar una paraula de 5 lletres")
    
    while intents_restants > 0:
        print(f"\n💪 Intents restants: {intents_restants}")
        
        if historial:
            mostra_historial(historial)
        
        intent = input("\n✍️  Escriu la teva paraula: ").strip().upper()
        
        if not es_valid_intent(intent):
            continue
        
        # Comprovar l'intent
        resultat = mostra_resultat(paraula_secreta, intent)
        historial.append((intent, resultat))
        
        print(f"\n{intent}  {resultat}")
        
        # Comprovar si ha guanyat
        if intent == paraula_secreta:
            ha_guanyat = True
            print("\n" + "🎉" * 20)
            print("🏆 FELICITATS! Has endevinat la paraula!")
            print("🎉" * 20)
            break
        
        intents_restants -= 1
    
    # Si s'han acabat els intents
    if not ha_guanyat:
        print("\n" + "💔" * 20)
        print(f"😢 Ho sento! La paraula era: {paraula_secreta}")
        print("💔" * 20)
    
    return ha_guanyat, 6 - intents_restants

def menu_joc():
    """Mostra el menú del joc"""
    print("\n" + "="*50)
    print("JOC D'ENDEVINAR PARAULES")
    print("="*50)
    print("\n1. Jugar una partida")
    print("2. Veure estadístiques")
    print("3. Reiniciar estadístiques")
    print("0. Tornar al menú principal")

def main():
    """Funció principal de l'aplicació 3"""
    partides_jugades = 0
    partides_guanyades = 0
    intents_totals = 0
    
    while True:
        menu_joc()
        opcio = input("\nSelecciona una opció: ").strip()
        
        if opcio == "1":
            ha_guanyat, intents = juga_partida()
            partides_jugades += 1
            if ha_guanyat:
                partides_guanyades += 1
                intents_totals += intents
            
            input("\n\nPrem ENTER per continuar...")
            
        elif opcio == "2":
            mostra_estadistiques(partides_jugades, partides_guanyades, intents_totals)
            input("\nPrem ENTER per continuar...")
            
        elif opcio == "3":
            confirmacio = input("\n⚠️  Segur que vols reiniciar les estadístiques? (s/n): ")
            if confirmacio.lower() == 's':
                partides_jugades = 0
                partides_guanyades = 0
                intents_totals = 0
                print("✅ Estadístiques reiniciades!")
            input("\nPrem ENTER per continuar...")
            
        elif opcio == "0":
            break
        else:
            print("❌ Opció no vàlida!")
            input("Prem ENTER per continuar...")

if __name__ == "__main__":
    main()