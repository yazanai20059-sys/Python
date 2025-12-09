import random
import statistics
from collections import Counter

def genera_llista_aleatoria(mida, minim, maxim):
    """
    Genera una llista de números aleatoris
    Args:
        mida: nombre d'elements
        minim: valor mínim
        maxim: valor màxim
    Returns:
        llista de números aleatoris
    """
    return [random.randint(minim, maxim) for _ in range(mida)]

def analitza_llista(llista):
    """
    Calcula estadístiques d'una llista de números
    Args:
        llista: llista de números a analitzar
    """
    print("\n" + "="*50)
    print("ANÀLISI ESTADÍSTIC")
    print("="*50)
    
    # Mostrar llista original
    print(f"\n📋 Llista original ({len(llista)} elements):")
    print(llista)
    
    # Estadístiques bàsiques
    print(f"\n📈 Estadístiques bàsiques:")
    print(f"   • Mínim: {min(llista)}")
    print(f"   • Màxim: {max(llista)}")
    print(f"   • Suma: {sum(llista)}")
    print(f"   • Mitjana: {statistics.mean(llista):.2f}")
    print(f"   • Mediana: {statistics.median(llista)}")
    
    # Desviació estàndard només si hi ha més d'un element
    if len(llista) > 1:
        print(f"   • Desviació estàndard: {statistics.stdev(llista):.2f}")
    
    # Freqüències
    freq = Counter(llista)
    print(f"\n🔢 Freqüències:")
    for numero, vegades in sorted(freq.items()):
        barra = "█" * vegades
        print(f"   {numero:3d}: {barra} ({vegades})")
    
    # Llista ordenada
    print(f"\n📊 Llista ordenada:")
    print(sorted(llista))

def genera_combinacio_loteria():
    """
    Genera una combinació de loteria (6 números del 1 al 49)
    Returns:
        llista ordenada de 6 números únics
    """
    return sorted(random.sample(range(1, 50), 6))

def simula_llançaments_daus(num_llançaments):
    """
    Simula llançaments de dos daus i mostra estadístiques
    Args:
        num_llançaments: nombre de llançaments a simular
    """
    resultats = []
    for _ in range(num_llançaments):
        dau1 = random.randint(1, 6)
        dau2 = random.randint(1, 6)
        resultats.append(dau1 + dau2)
    
    print(f"\n🎲 Simulació de {num_llançaments} llançaments de 2 daus:")
    freq = Counter(resultats)
    
    for suma in range(2, 13):
        vegades = freq[suma]
        percentatge = (vegades / num_llançaments) * 100
        barra = "█" * int(percentatge)
        print(f"   {suma:2d}: {barra} {vegades:4d} ({percentatge:.1f}%)")

def menu_estadistiques():
    """Mostra el menú de l'aplicació d'estadístiques"""
    print("\n" + "="*50)
    print("GENERADOR D'ESTADÍSTIQUES")
    print("="*50)
    print("\n1. Generar llista aleatòria i analitzar")
    print("2. Generar combinació de loteria")
    print("3. Simular llançaments de daus")
    print("4. Comparar múltiples llistes")
    print("0. Tornar al menú principal")

def main():
    """Funció principal de l'aplicació 1"""
    while True:
        menu_estadistiques()
        opcio = input("\nSelecciona una opció: ").strip()
        
        if opcio == "1":
            try:
                mida = int(input("\nQuants números vols generar? "))
                minim = int(input("Valor mínim: "))
                maxim = int(input("Valor màxim: "))
                
                llista = genera_llista_aleatoria(mida, minim, maxim)
                analitza_llista(llista)
                
            except ValueError:
                print("❌ Error: Introdueix números vàlids!")
            
            input("\nPrem ENTER per continuar...")
            
        elif opcio == "2":
            print("\n🎰 Generant combinació de loteria...")
            for i in range(5):
                combinacio = genera_combinacio_loteria()
                print(f"   Combinació {i+1}: {combinacio}")
            input("\nPrem ENTER per continuar...")
            
        elif opcio == "3":
            try:
                num = int(input("\nQuants llançaments vols simular? "))
                simula_llançaments_daus(num)
            except ValueError:
                print("❌ Error: Introdueix un número vàlid!")
            input("\nPrem ENTER per continuar...")
            
        elif opcio == "4":
            try:
                num_llistes = int(input("\nQuantes llistes vols comparar? "))
                llistes = []
                
                for i in range(num_llistes):
                    mida = random.randint(10, 20)
                    llista = genera_llista_aleatoria(mida, 1, 100)
                    llistes.append(llista)
                    print(f"\n📋 Llista {i+1}: Mitjana = {statistics.mean(llista):.2f}")
                
                mitjanes = [statistics.mean(l) for l in llistes]
                millor = mitjanes.index(max(mitjanes))
                print(f"\n🏆 La llista {millor+1} té la mitjana més alta!")
                
            except ValueError:
                print("❌ Error!")
            input("\nPrem ENTER per continuar...")
            
        elif opcio == "0":
            break
        else:
            print("❌ Opció no vàlida!")
            input("Prem ENTER per continuar...")

if __name__ == "__main__":
    main()