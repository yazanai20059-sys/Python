"""
Programa Principal - Menú de selecció d'aplicacions
Autor: [El teu nom]
Data: 2024
Descripció: Menú interactiu que permet accedir a 6 aplicacions diferents
"""

import os
import sys

def neteja_pantalla():
    """Neteja la consola segons el sistema operatiu"""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostra_menu():
    """Mostra el menú principal amb les 6 opcions"""
    neteja_pantalla()
    print("=" * 60)
    print(" " * 15 + "MENÚ PRINCIPAL")
    print("=" * 60)
    print("\n1. Generador d'Estadístiques (Llistes i aleatoris)")
    print("2. Gestor de Notes (Fitxers)")
    print("3. Joc: Endevina la Paraula (Joc)")
    print("4. Biblioteca Virtual (POO)")
    print("5. Consulta Meteorològica (Web Scraping)")
    print("6. API de Tasques (Servei Web)")
    print("0. Sortir")
    print("=" * 60)

def main():
    """Funció principal que controla el flux del programa"""
    while True:
        mostra_menu()
        opcio = input("\nSelecciona una opció (0-6): ").strip()
        
        if opcio == "1":
            # Importar i executar aplicació 1
            try:
                import app1_estadistiques
                app1_estadistiques.main()
            except Exception as e:
                print(f"Error en l'aplicació 1: {e}")
                input("\nPrem ENTER per continuar...")
                
        elif opcio == "2":
            try:
                import app2_notes
                app2_notes.main()
            except Exception as e:
                print(f"Error en l'aplicació 2: {e}")
                input("\nPrem ENTER per continuar...")
                
        elif opcio == "3":
            try:
                import app3_endevina
                app3_endevina.main()
            except Exception as e:
                print(f"Error en l'aplicació 3: {e}")
                input("\nPrem ENTER per continuar...")
                
        elif opcio == "4":
            try:
                import app4_biblioteca
                app4_biblioteca.main()
            except Exception as e:
                print(f"Error en l'aplicació 4: {e}")
                input("\nPrem ENTER per continuar...")
                
        elif opcio == "5":
            try:
                import app5_meteorologia
                app5_meteorologia.main()
            except Exception as e:
                print(f"Error en l'aplicació 5: {e}")
                input("\nPrem ENTER per continuar...")
                
        elif opcio == "6":
            try:
                import app6_api_tasks
                app6_api_tasks.main()
            except Exception as e:
                print(f"Error en l'aplicació 6: {e}")
                input("\nPrem ENTER per continuar...")
                
        elif opcio == "0":
            print("\n👋 Adéu! Fins aviat!")
            sys.exit(0)
        else:
            print("\n❌ Opció no vàlida!")
            input("Prem ENTER per continuar...")

if __name__ == "__main__":
    main()

"""
Aplicació 1: Generador d'Estadístiques
Treballa amb llistes i números aleatoris
Genera dades aleatòries i en calcula estadístiques
"""

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

"""
Aplicació 2: Gestor de Notes
Treballa amb fitxers per guardar i gestionar notes personals
Permet crear, llegir, actualitzar i esborrar notes
"""

import os
import json
from datetime import datetime

# Nom del fitxer on es guardaran les notes
FITXER_NOTES = "notes.json"

def carrega_notes():
    """
    Carrega les notes des del fitxer JSON
    Returns:
        diccionari amb les notes o diccionari buit si no existeix
    """
    if os.path.exists(FITXER_NOTES):
        try:
            with open(FITXER_NOTES, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("⚠️  Fitxer corrupte, creant-ne un de nou...")
            return {}
    return {}

def guarda_notes(notes):
    """
    Guarda les notes al fitxer JSON
    Args:
        notes: diccionari amb totes les notes
    """
    with open(FITXER_NOTES, 'w', encoding='utf-8') as f:
        json.dump(notes, f, ensure_ascii=False, indent=4)

def crea_nota(notes):
    """
    Crea una nova nota
    Args:
        notes: diccionari de notes existent
    """
    print("\n" + "="*50)
    print("CREAR NOVA NOTA")
    print("="*50)
    
    titol = input("\n📌 Títol de la nota: ").strip()
    
    if not titol:
        print("❌ El títol no pot estar buit!")
        return
    
    if titol in notes:
        resposta = input("⚠️  Ja existeix una nota amb aquest títol. Sobreescriure? (s/n): ")
        if resposta.lower() != 's':
            return
    
    print("\n📝 Contingut (escriu 'FI' en una línia per acabar):")
    linies = []
    while True:
        linia = input()
        if linia.strip().upper() == 'FI':
            break
        linies.append(linia)
    
    contingut = '\n'.join(linies)
    
    # Guardar nota amb timestamp
    notes[titol] = {
        'contingut': contingut,
        'data_creacio': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'data_modificacio': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    guarda_notes(notes)
    print("\n✅ Nota guardada correctament!")

def llista_notes(notes):
    """
    Mostra totes les notes disponibles
    Args:
        notes: diccionari de notes
    """
    if not notes:
        print("\n📭 No hi ha notes guardades.")
        return
    
    print("\n" + "="*50)
    print(f"LLISTA DE NOTES ({len(notes)})")
    print("="*50)
    
    for i, (titol, dades) in enumerate(notes.items(), 1):
        print(f"\n{i}. 📌 {titol}")
        print(f"   📅 Creat: {dades['data_creacio']}")
        print(f"   ✏️  Modificat: {dades['data_modificacio']}")
        
        # Mostrar preview del contingut (primeres 50 caràcters)
        preview = dades['contingut'][:50]
        if len(dades['contingut']) > 50:
            preview += "..."
        print(f"   📄 {preview}")

def llegeix_nota(notes):
    """
    Mostra el contingut complet d'una nota
    Args:
        notes: diccionari de notes
    """
    if not notes:
        print("\n📭 No hi ha notes guardades.")
        return
    
    llista_notes(notes)
    
    titol = input("\n📖 Títol de la nota a llegir: ").strip()
    
    if titol not in notes:
        print("❌ Nota no trobada!")
        return
    
    print("\n" + "="*50)
    print(f"📌 {titol}")
    print("="*50)
    print(f"📅 Creat: {notes[titol]['data_creacio']}")
    print(f"✏️  Modificat: {notes[titol]['data_modificacio']}")
    print("\n" + "-"*50)
    print(notes[titol]['contingut'])
    print("-"*50)

def actualitza_nota(notes):
    """
    Actualitza el contingut d'una nota existent
    Args:
        notes: diccionari de notes
    """
    if not notes:
        print("\n📭 No hi ha notes guardades.")
        return
    
    llista_notes(notes)
    
    titol = input("\n✏️  Títol de la nota a actualitzar: ").strip()
    
    if titol not in notes:
        print("❌ Nota no trobada!")
        return
    
    print("\n📄 Contingut actual:")
    print(notes[titol]['contingut'])
    
    print("\n📝 Nou contingut (escriu 'FI' en una línia per acabar):")
    linies = []
    while True:
        linia = input()
        if linia.strip().upper() == 'FI':
            break
        linies.append(linia)
    
    nou_contingut = '\n'.join(linies)
    
    notes[titol]['contingut'] = nou_contingut
    notes[titol]['data_modificacio'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    guarda_notes(notes)
    print("\n✅ Nota actualitzada correctament!")

def esborra_nota(notes):
    """
    Esborra una nota
    Args:
        notes: diccionari de notes
    """
    if not notes:
        print("\n📭 No hi ha notes guardades.")
        return
    
    llista_notes(notes)
    
    titol = input("\n🗑️  Títol de la nota a esborrar: ").strip()
    
    if titol not in notes:
        print("❌ Nota no trobada!")
        return
    
    confirmacio = input(f"⚠️  Segur que vols esborrar '{titol}'? (s/n): ")
    
    if confirmacio.lower() == 's':
        del notes[titol]
        guarda_notes(notes)
        print("\n✅ Nota esborrada correctament!")
    else:
        print("\n❌ Operació cancel·lada.")

def cerca_notes(notes):
    """
    Cerca notes per paraula clau
    Args:
        notes: diccionari de notes
    """
    if not notes:
        print("\n📭 No hi ha notes guardades.")
        return
    
    paraula = input("\n🔍 Paraula a cercar: ").strip().lower()
    
    trobades = []
    for titol, dades in notes.items():
        if (paraula in titol.lower() or 
            paraula in dades['contingut'].lower()):
            trobades.append(titol)
    
    if not trobades:
        print(f"\n❌ No s'han trobat notes amb '{paraula}'")
    else:
        print(f"\n✅ S'han trobat {len(trobades)} note(s):")
        for titol in trobades:
            print(f"\n📌 {titol}")
            print(f"   {notes[titol]['contingut'][:100]}...")

def menu_notes():
    """Mostra el menú del gestor de notes"""
    print("\n" + "="*50)
    print("GESTOR DE NOTES")
    print("="*50)
    print("\n1. Crear nova nota")
    print("2. Llistar totes les notes")
    print("3. Llegir una nota")
    print("4. Actualitzar una nota")
    print("5. Esborrar una nota")
    print("6. Cercar notes")
    print("0. Tornar al menú principal")

def main():
    """Funció principal de l'aplicació 2"""
    notes = carrega_notes()
    
    while True:
        menu_notes()
        opcio = input("\nSelecciona una opció: ").strip()
        
        if opcio == "1":
            crea_nota(notes)
            input("\nPrem ENTER per continuar...")
            
        elif opcio == "2":
            llista_notes(notes)
            input("\nPrem ENTER per continuar...")
            
        elif opcio == "3":
            llegeix_nota(notes)
            input("\nPrem ENTER per continuar...")
            
        elif opcio == "4":
            actualitza_nota(notes)
            input("\nPrem ENTER per continuar...")
            
        elif opcio == "5":
            esborra_nota(notes)
            input("\nPrem ENTER per continuar...")
            
        elif opcio == "6":
            cerca_notes(notes)
            input("\nPrem ENTER per continuar...")
            
        elif opcio == "0":
            break
        else:
            print("❌ Opció no vàlida!")
            input("Prem ENTER per continuar...")

if __name__ == "__main__":
    main()

"""
Aplicació 3: Joc d'Endevinar Paraules
Similar al Wordle però amb lògica pròpia
El jugador ha d'endevinar una paraula en 6 intents
"""

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

"""
Aplicació 4: Sistema de Biblioteca Virtual
Utilitza POO amb classes, herència i polimorfisme
Gestiona diferents tipus de materials: llibres, revistes, DVDs
"""

from datetime import datetime, timedelta
from abc import ABC, abstractmethod

class Material(ABC):
    """
    Classe abstracta base per a tots els materials de la biblioteca
    Defineix la interfície comuna per a tots els materials
    """
    
    def __init__(self, titol, autor, any_publicacio, codi):
        """
        Constructor de la classe Material
        Args:
            titol: títol del material
            autor: autor/creador del material
            any_publicacio: any de publicació
            codi: codi únic identificador
        """
        self.titol = titol
        self.autor = autor
        self.any_publicacio = any_publicacio
        self.codi = codi
        self.prestat = False
        self.data_prestec = None
        self.usuari_prestec = None
    
    @abstractmethod
    def mostra_informacio(self):
        """Mètode abstracte que cada subclasse ha d'implementar"""
        pass
    
    @abstractmethod
    def dies_prestec(self):
        """Retorna el nombre de dies màxim de préstec segons el tipus de material"""
        pass
    
    def presta(self, usuari):
        """
        Presta el material a un usuari
        Args:
            usuari: objecte Usuari que fa el préstec
        Returns:
            True si s'ha pogut prestar, False altrament
        """
        if self.prestat:
            print(f"❌ '{self.titol}' ja està prestat!")
            return False
        
        self.prestat = True
        self.data_prestec = datetime.now()
        self.usuari_prestec = usuari
        usuari.afegeix_prestec(self)
        print(f"✅ '{self.titol}' prestat a {usuari.nom}")
        print(f"📅 Data de devolució: {self.data_devolucio().strftime('%d/%m/%Y')}")
        return True
    
    def retorna(self):
        """
        Retorna el material a la biblioteca
        Returns:
            True si s'ha pogut retornar, False altrament
        """
        if not self.prestat:
            print(f"❌ '{self.titol}' no està prestat!")
            return False
        
        # Comprovar si hi ha retard
        dies_retard = (datetime.now() - self.data_devolucio()).days
        
        if dies_retard > 0:
            multa = dies_retard * 0.50  # 0.50€ per dia de retard
            print(f"⚠️  Retard de {dies_retard} dies. Multa: {multa:.2f}€")
        
        self.usuari_prestec.elimina_prestec(self)
        self.prestat = False
        self.data_prestec = None
        self.usuari_prestec = None
        print(f"✅ '{self.titol}' retornat correctament")
        return True
    
    def data_devolucio(self):
        """
        Calcula la data límit de devolució
        Returns:
            datetime amb la data de devolució
        """
        if not self.data_prestec:
            return None
        return self.data_prestec + timedelta(days=self.dies_prestec())
    
    def __str__(self):
        """Representació en string del material"""
        estat = "🔴 Prestat" if self.prestat else "🟢 Disponible"
        return f"[{self.codi}] {self.titol} - {self.autor} ({self.any_publicacio}) {estat}"


class Llibre(Material):
    """Classe per representar un llibre"""
    
    def __init__(self, titol, autor, any_publicacio, codi, pagines, isbn):
        super().__init__(titol, autor, any_publicacio, codi)
        self.pagines = pagines
        self.isbn = isbn
    
    def mostra_informacio(self):
        """Mostra informació detallada del llibre"""
        print("\n" + "="*50)
        print("📖 LLIBRE")
        print("="*50)
        print(f"Títol: {self.titol}")
        print(f"Autor: {self.autor}")
        print(f"Any: {self.any_publicacio}")
        print(f"Pàgines: {self.pagines}")
        print(f"ISBN: {self.isbn}")
        print(f"Codi: {self.codi}")
        print(f"Estat: {'🔴 Prestat' if self.prestat else '🟢 Disponible'}")
        if self.prestat:
            print(f"Prestat a: {self.usuari_prestec.nom}")
            print(f"Data devolució: {self.data_devolucio().strftime('%d/%m/%Y')}")
    
    def dies_prestec(self):
        """Llibres es poden prestar durant 21 dies"""
        return 21


class Revista(Material):
    """Classe per representar una revista"""
    
    def __init__(self, titol, autor, any_publicacio, codi, numero, mes):
        super().__init__(titol, autor, any_publicacio, codi)
        self.numero = numero
        self.mes = mes
    
    def mostra_informacio(self):
        """Mostra informació detallada de la revista"""
        print("\n" + "="*50)
        print("📰 REVISTA")
        print("="*50)
        print(f"Títol: {self.titol}")
        print(f"Editorial: {self.autor}")
        print(f"Any: {self.any_publicacio}")
        print(f"Número: {self.numero}")
        print(f"Mes: {self.mes}")
        print(f"Codi: {self.codi}")
        print(f"Estat: {'🔴 Prestat' if self.prestat else '🟢 Disponible'}")
        if self.prestat:
            print(f"Prestat a: {self.usuari_prestec.nom}")
            print(f"Data devolució: {self.data_devolucio().strftime('%d/%m/%Y')}")
    
    def dies_prestec(self):
        """Revistes es poden prestar durant 7 dies"""
        return 7


class DVD(Material):
    """Classe per representar un DVD"""
    
    def __init__(self, titol, autor, any_publicacio, codi, duracio, genere):
        super().__init__(titol, autor, any_publicacio, codi)
        self.duracio = duracio  # en minuts
        self.genere = genere
    
    def mostra_informacio(self):
        """Mostra informació detallada del DVD"""
        print("\n" + "="*50)
        print("💿 DVD")
        print("="*50)
        print(f"Títol: {self.titol}")
        print(f"Director: {self.autor}")
        print(f"Any: {self.any_publicacio}")
        print(f"Duració: {self.duracio} minuts")
        print(f"Gènere: {self.genere}")
        print(f"Codi: {self.codi}")
        print(f"Estat: {'🔴 Prestat' if self.prestat else '🟢 Disponible'}")
        if self.prestat:
            print(f"Prestat a: {self.usuari_prestec.nom}")
            print(f"Data devolució: {self.data_devolucio().strftime('%d/%m/%Y')}")
    
    def dies_prestec(self):
        """DVDs es poden prestar durant 3 dies"""
        return 3


class Usuari:
    """Classe per representar un usuari de la biblioteca"""
    
    def __init__(self, nom, cognoms, dni):
        """
        Constructor de la classe Usuari
        Args:
            nom: nom de l'usuari
            cognoms: cognoms de l'usuari
            dni: DNI de l'usuari
        """
        self.nom = nom
        self.cognoms = cognoms
        self.dni = dni
        self.prestecs = []  # Llista de materials prestats
    
    def afegeix_prestec(self, material):
        """Afegeix un material a la llista de préstecs"""
        self.prestecs.append(material)
    
    def elimina_prestec(self, material):
        """Elimina un material de la llista de préstecs"""
        if material in self.prestecs:
            self.prestecs.remove(material)
    
    def mostra_prestecs(self):
        """Mostra tots els materials prestats per l'usuari"""
        if not self.prestecs:
            print(f"\n{self.nom} no té cap material prestat.")
            return
        
        print(f"\n📚 Materials prestats per {self.nom}:")
        print("-" * 50)
        for material in self.prestecs:
            dies_restants = (material.data_devolucio() - datetime.now()).days
            if dies_restants < 0:
                print(f"⚠️  {material.titol} - RETARD de {abs(dies_restants)} dies")
            else:
                print(f"✅ {material.titol} - {dies_restants} dies restants")
    
    def __str__(self):
        """Representació en string de l'usuari"""
        return f"{self.nom} {self.cognoms} ({self.dni}) - {len(self.prestecs)} préstecs actius"


class Biblioteca:
    """Classe per gestionar la biblioteca"""
    
    def __init__(self, nom):
        """
        Constructor de la classe Biblioteca
        Args:
            nom: nom de la biblioteca
        """
        self.nom = nom
        self.materials = []
        self.usuaris = []
    
    def afegeix_material(self, material):
        """Afegeix un material al catàleg"""
        self.materials.append(material)
        print(f"✅ Material '{material.titol}' afegit al catàleg")
    
    def afegeix_usuari(self, usuari):
        """Registra un nou usuari"""
        self.usuaris.append(usuari)
        print(f"✅ Usuari '{usuari.nom}' registrat")
    
    def cerca_material(self, criteri):
        """
        Cerca materials per títol o autor
        Args:
            criteri: text a cercar
        Returns:
            llista de materials trobats
        """
        criteri = criteri.lower()
        trobats = [m for m in self.materials 
                   if criteri in m.titol.lower() or criteri in m.autor.lower()]
        return trobats
    
    def cerca_usuari(self, dni):
        """
        Cerca un usuari pel DNI
        Args:
            dni: DNI de l'usuari
        Returns:
            objecte Usuari o None si no es troba
        """
        for usuari in self.usuaris:
            if usuari.dni == dni:
                return usuari
        return None
    
    def llista_materials_disponibles(self):
        """Mostra tots els materials disponibles"""
        disponibles = [m for m in self.materials if not m.prestat]
        
        if not disponibles:
            print("\n❌ No hi ha materials disponibles")
            return
        
        print(f"\n📚 Materials disponibles ({len(disponibles)}):")
        print("="*60)
        for material in disponibles:
            print(material)
    
    def llista_tots_materials(self):
        """Mostra tots els materials del catàleg"""
        if not self.materials:
            print("\n❌ El catàleg està buit")
            return
        
        print(f"\n📚 Catàleg complet ({len(self.materials)} materials):")
        print("="*60)
        
        # Agrupar per tipus
        llibres = [m for m in self.materials if isinstance(m, Llibre)]
        revistes = [m for m in self.materials if isinstance(m, Revista)]
        dvds = [m for m in self.materials if isinstance(m, DVD)]
        
        if llibres:
            print("\n📖 LLIBRES:")
            for llibre in llibres:
                print(f"  {llibre}")
        
        if revistes:
            print("\n📰 REVISTES:")
            for revista in revistes:
                print(f"  {revista}")
        
        if dvds:
            print("\n💿 DVDS:")
            for dvd in dvds:
                print(f"  {dvd}")
    
    def estadistiques(self):
        """Mostra estadístiques de la biblioteca"""
        total = len(self.materials)
        prestats = len([m for m in self.materials if m.prestat])
        disponibles = total - prestats
        
        print("\n" + "="*50)
        print(f"📊 ESTADÍSTIQUES - {self.nom}")
        print("="*50)
        print(f"📚 Total materials: {total}")
        print(f"🟢 Disponibles: {disponibles}")
        print(f"🔴 Prestats: {prestats}")
        print(f"👥 Usuaris registrats: {len(self.usuaris)}")
        
        # Materials més prestats (en aquest cas, només els que estan prestats ara)
        if prestats > 0:
            print(f"\n🔥 Materials actualment prestats:")
            for material in self.materials:
                if material.prestat:
                    print(f"   • {material.titol} ({material.usuari_prestec.nom})")


def crea_dades_exemple(biblioteca):
    """Crea dades d'exemple per provar el sistema"""
    
    # Crear materials
    biblioteca.afegeix_material(Llibre(
        "1984", "George Orwell", 1949, "L001", 328, "978-0451524935"
    ))
    biblioteca.afegeix_material(Llibre(
        "El Quixot", "Miguel de Cervantes", 1605, "L002", 863, "978-8420633510"
    ))
    biblioteca.afegeix_material(Llibre(
        "Cien años de soledad", "Gabriel García Márquez", 1967, "L003", 417, "978-0307474728"
    ))
    
    biblioteca.afegeix_material(Revista(
        "National Geographic", "National Geographic Society", 2024, "R001", 245, "Gener"
    ))
    biblioteca.afegeix_material(Revista(
        "Time", "Time Inc.", 2024, "R002", 12, "Febrer"
    ))
    
    biblioteca.afegeix_material(DVD(
        "El Padrino", "Francis Ford Coppola", 1972, "D001", 175, "Drama"
    ))
    biblioteca.afegeix_material(DVD(
        "Pulp Fiction", "Quentin Tarantino", 1994, "D002", 154, "Thriller"
    ))
    
    # Crear usuaris
    biblioteca.afegeix_usuari(Usuari("Joan", "García López", "12345678A"))
    biblioteca.afegeix_usuari(Usuari("Maria", "Martínez Sánchez", "87654321B"))
    biblioteca.afegeix_usuari(Usuari("Pere", "Fernández Vila", "11111111C"))
    
    print("\n✅ Dades d'exemple creades!")


def menu_biblioteca():
    """Mostra el menú de la biblioteca"""
    print("\n" + "="*50)
    print("SISTEMA DE BIBLIOTECA")
    print("="*50)
    print("\n📚 MATERIALS")
    print("  1. Afegir material")
    print("  2. Llistar tots els materials")
    print("  3. Llistar materials disponibles")
    print("  4. Cercar material")
    print("  5. Informació detallada d'un material")
    print("\n👥 USUARIS")
    print("  6. Registrar usuari")
    print("  7. Llistar usuaris")
    print("  8. Préstecs d'un usuari")
    print("\n🔄 OPERACIONS")
    print("  9. Prestar material")
    print(" 10. Retornar material")
    print("\n📊 INFORMACIÓ")
    print(" 11. Estadístiques")
    print(" 12. Crear dades d'exemple")
    print("\n 0. Tornar al menú principal")


def main():
    """Funció principal de l'aplicació 4"""
    biblioteca = Biblioteca("Biblioteca Municipal")
    
    while True:
        menu_biblioteca()
        opcio = input("\nSelecciona una opció: ").strip()
        
        if opcio == "1":
            # Afegir material
            print("\nTipus de material:")
            print("1. Llibre")
            print("2. Revista")
            print("3. DVD")
            tipus = input("Selecciona tipus: ").strip()
            
            titol = input("Títol: ").strip()
            autor = input("Autor/Director/Editorial: ").strip()
            any_publicacio = int(input("Any de publicació: "))
            codi = input("Codi: ").strip()
            
            if tipus == "1":
                pagines = int(input("Nombre de pàgines: "))
                isbn = input("ISBN: ").strip()
                material = Llibre(titol, autor, any_publicacio, codi, pagines, isbn)
            elif tipus == "2":
                numero = int(input("Número: "))
                mes = input("Mes: ").strip()
                material = Revista(titol, autor, any_publicacio, codi, numero, mes)
            elif tipus == "3":
                duracio = int(input("Duració (minuts): "))
                genere = input("Gènere: ").strip()
                material = DVD(titol, autor, any_publicacio, codi, duracio, genere)
            else:
                print("❌ Tipus no vàlid!")
                input("\nPrem ENTER per continuar...")
                continue
            
            biblioteca.afegeix_material(material)
            input("\nPrem ENTER per continuar...")
        
        elif opcio == "2":
            # Llistar tots els materials
            biblioteca.llista_tots_materials()
            input("\nPrem ENTER per continuar...")
        
        elif opcio == "3":
            # Llistar materials disponibles
            biblioteca.llista_materials_disponibles()
            input("\nPrem ENTER per continuar...")
        
        elif opcio == "4":
            # Cercar material
            criteri = input("\n🔍 Cerca per títol o autor: ").strip()
            resultats = biblioteca.cerca_material(criteri)
            
            if not resultats:
                print("❌ No s'han trobat resultats")
            else:
                print(f"\n✅ S'han trobat {len(resultats)} materials:")
                for material in resultats:
                    print(f"  {material}")
            
            input("\nPrem ENTER per continuar...")
        
        elif opcio == "5":
            # Informació detallada
            codi = input("\nCodi del material: ").strip()
            material = next((m for m in biblioteca.materials if m.codi == codi), None)
            
            if material:
                material.mostra_informacio()
            else:
                print("❌ Material no trobat!")
            
            input("\nPrem ENTER per continuar...")
        
        elif opcio == "6":
            # Registrar usuari
            nom = input("\nNom: ").strip()
            cognoms = input("Cognoms: ").strip()
            dni = input("DNI: ").strip()
            
            usuari = Usuari(nom, cognoms, dni)
            biblioteca.afegeix_usuari(usuari)
            input("\nPrem ENTER per continuar...")
        
        elif opcio == "7":
            # Llistar usuaris
            if not biblioteca.usuaris:
                print("\n❌ No hi ha usuaris registrats")
            else:
                print(f"\n👥 Usuaris registrats ({len(biblioteca.usuaris)}):")
                print("="*60)
                for usuari in biblioteca.usuaris:
                    print(f"  {usuari}")
            
            input("\nPrem ENTER per continuar...")
        
        elif opcio == "8":
            # Préstecs d'un usuari
            dni = input("\nDNI de l'usuari: ").strip()
            usuari = biblioteca.cerca_usuari(dni)
            
            if usuari:
                usuari.mostra_prestecs()
            else:
                print("❌ Usuari no trobat!")
            
            input("\nPrem ENTER per continuar...")
        
        elif opcio == "9":
            # Prestar material
            codi = input("\nCodi del material: ").strip()
            material = next((m for m in biblioteca.materials if m.codi == codi), None)
            
            if not material:
                print("❌ Material no trobat!")
                input("\nPrem ENTER per continuar...")
                continue
            
            dni = input("DNI de l'usuari: ").strip()
            usuari = biblioteca.cerca_usuari(dni)
            
            if not usuari:
                print("❌ Usuari no trobat!")
                input("\nPrem ENTER per continuar...")
                continue
            
            material.presta(usuari)
            input("\nPrem ENTER per continuar...")
        
        elif opcio == "10":
            # Retornar material
            codi = input("\nCodi del material: ").strip()
            material = next((m for m in biblioteca.materials if m.codi == codi), None)
            
            if material:
                material.retorna()
            else:
                print("❌ Material no trobat!")
            
            input("\nPrem ENTER per continuar...")
        
        elif opcio == "11":
            # Estadístiques
            biblioteca.estadistiques()
            input("\nPrem ENTER per continuar...")
        
        elif opcio == "12":
            # Crear dades d'exemple
            crea_dades_exemple(biblioteca)
            input("\nPrem ENTER per continuar...")
        
        elif opcio == "0":
            break
        else:
            print("❌ Opció no vàlida!")
            input("Prem ENTER per continuar...")


if __name__ == "__main__":
    main()

"""
Aplicació 5: Consulta Meteorològica
Utilitza web scraping per obtenir informació del temps
Nota: Per a un exemple real, es pot utilitzar una API gratuïta
"""

import requests
import json
from datetime import datetime

# Nota: Aquesta aplicació utilitzarà una API gratuïta en lloc de web scraping directe
# perquè és més fiable i legal. API utilitzada: Open-Meteo (sense necessitat de clau)

def obte_coordenades_ciutat(ciutat):
    """
    Obté les coordenades geogràfiques d'una ciutat
    Args:
        ciutat: nom de la ciutat
    Returns:
        tuple (latitud, longitud, nom_complet) o None si no es troba
    """
    try:
        url = f"https://geocoding-api.open-meteo.com/v1/search?name={ciutat}&count=1&language=ca&format=json"
        resposta = requests.get(url, timeout=10)
        dades = resposta.json()
        
        if 'results' in dades and len(dades['results']) > 0:
            resultat = dades['results'][0]
            return (resultat['latitude'], resultat['longitude'], resultat['name'])
        return None
    except Exception as e:
        print(f"❌ Error obtenint coordenades: {e}")
        return None

def obte_temps_actual(latitud, longitud):
    """
    Obté informació meteorològica actual
    Args:
        latitud: latitud de la localització
        longitud: longitud de la localització
    Returns:
        diccionari amb dades meteorològiques o None si hi ha error
    """
    try:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={latitud}&longitude={longitud}&current=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,weather_code,wind_speed_10m&timezone=Europe/Madrid"
        resposta = requests.get(url, timeout=10)
        dades = resposta.json()
        
        return dades['current'] if 'current' in dades else None
    except Exception as e:
        print(f"❌ Error obtenint dades meteorològiques: {e}")
        return None

def obte_previsions(latitud, longitud, dies=7):
    """
    Obté previsions meteorològiques
    Args:
        latitud: latitud de la localització
        longitud: longitud de la localització
        dies: nombre de dies de previsió (màxim 16)
    Returns:
        diccionari amb previsions o None si hi ha error
    """
    try:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={latitud}&longitude={longitud}&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,weather_code&timezone=Europe/Madrid&forecast_days={dies}"
        resposta = requests.get(url, timeout=10)
        dades = resposta.json()
        
        return dades['daily'] if 'daily' in dades else None
    except Exception as e:
        print(f"❌ Error obtenint previsions: {e}")
        return None

def interpreta_codi_temps(codi):
    """
    Interpreta el codi WMO del temps
    Args:
        codi: codi WMO (0-99)
    Returns:
        tuple (descripció, emoji)
    """
    codis = {
        0: ("Cel clar", "☀️"),
        1: ("Majoritàriament clar", "🌤️"),
        2: ("Parcialment ennuvolat", "⛅"),
        3: ("Ennuvolat", "☁️"),
        45: ("Boira", "🌫️"),
        48: ("Boira amb gelada", "🌫️"),
        51: ("Plugim lleuger", "🌦️"),
        53: ("Plugim moderat", "🌦️"),
        55: ("Plugim intens", "🌧️"),
        61: ("Pluja lleugera", "🌧️"),
        63: ("Pluja moderada", "🌧️"),
        65: ("Pluja intensa", "🌧️"),
        71: ("Neu lleugera", "🌨️"),
        73: ("Neu moderada", "🌨️"),
        75: ("Neu intensa", "❄️"),
        77: ("Granissos", "🌨️"),
        80: ("Ruixats lleugers", "🌦️"),
        81: ("Ruixats moderats", "🌧️"),
        82: ("Ruixats intensos", "⛈️"),
        85: ("Ruixats de neu lleugers", "🌨️"),
        86: ("Ruixats de neu intensos", "❄️"),
        95: ("Tempesta", "⛈️"),
        96: ("Tempesta amb calamarsa", "⛈️"),
        99: ("Tempesta amb calamarsa intensa", "⛈️")
    }
    
    return codis.get(codi, ("Desconegut", "❓"))

def mostra_temps_actual(ciutat, dades):
    """
    Mostra la informació meteorològica actual de forma visual
    Args:
        ciutat: nom de la ciutat
        dades: diccionari amb dades meteorològiques
    """
    descripcio, emoji = interpreta_codi_temps(dades.get('weather_code', 0))
    
    print("\n" + "="*60)
    print(f"🌍 TEMPS ACTUAL A {ciutat.upper()}")
    print("="*60)
    print(f"\n{emoji} {descripcio}")
    print(f"\n🌡️  Temperatura: {dades.get('temperature_2m', 'N/A')}°C")
    print(f"🌡️  Sensació tèrmica: {dades.get('apparent_temperature', 'N/A')}°C")
    print(f"💧 Humitat: {dades.get('relative_humidity_2m', 'N/A')}%")
    print(f"🌧️  Precipitació: {dades.get('precipitation', 'N/A')} mm")
    print(f"💨 Vent: {dades.get('wind_speed_10m', 'N/A')} km/h")
    print(f"\n🕐 Actualitzat: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    print("="*60)

def mostra_previsions(ciutat, dades, dies=7):
    """
    Mostra les previsions meteorològiques
    Args:
        ciutat: nom de la ciutat
        dades: diccionari amb previsions
        dies: nombre de dies a mostrar
    """
    print("\n" + "="*60)
    print(f"📅 PREVISIÓ PER A {ciutat.upper()} ({dies} dies)")
    print("="*60)
    
    for i in range(min(dies, len(dades['time']))):
        data = dades['time'][i]
        temp_max = dades['temperature_2m_max'][i]
        temp_min = dades['temperature_2m_min'][i]
        precipitacio = dades['precipitation_sum'][i]
        codi = dades['weather_code'][i]
        
        descripcio, emoji = interpreta_codi_temps(codi)
        
        # Formatear la data
        data_obj = datetime.strptime(data, '%Y-%m-%d')
        dia_setmana = ['Dl', 'Dt', 'Dc', 'Dj', 'Dv', 'Ds', 'Dg'][data_obj.weekday()]
        data_format = data_obj.strftime('%d/%m')
        
        print(f"\n{emoji} {dia_setmana} {data_format} - {descripcio}")
        print(f"   🌡️  Màx: {temp_max}°C | Mín: {temp_min}°C")
        if precipitacio > 0:
            print(f"   🌧️  Precipitació: {precipitacio} mm")

def compara_ciutats(ciutats):
    """
    Compara el temps de múltiples ciutats
    Args:
        ciutats: llista de noms de ciutats
    """
    print("\n" + "="*60)
    print("📊 COMPARACIÓ DE CIUTATS")
    print("="*60)
    
    dades_ciutats = []
    
    for ciutat in ciutats:
        coordenades = obte_coordenades_ciutat(ciutat)
        if coordenades:
            lat, lon, nom_complet = coordenades
            temps = obte_temps_actual(lat, lon)
            if temps:
                dades_ciutats.append({
                    'nom': nom_complet,
                    'temperatura': temps.get('temperature_2m', 0),
                    'temps': interpreta_codi_temps(temps.get('weather_code', 0))
                })
    
    if not dades_ciutats:
        print("❌ No s'han pogut obtenir dades")
        return
    
    # Ordenar per temperatura
    dades_ciutats.sort(key=lambda x: x['temperatura'], reverse=True)
    
    print("\n🔥 Més càlides:")
    for i, ciutat in enumerate(dades_ciutats[:3], 1):
        emoji = ciutat['temps'][1]
        print(f"   {i}. {ciutat['nom']}: {ciutat['temperatura']}°C {emoji}")
    
    print("\n❄️  Més fredes:")
    for i, ciutat in enumerate(reversed(dades_ciutats[-3:]), 1):
        emoji = ciutat['temps'][1]
        print(f"   {i}. {ciutat['nom']}: {ciutat['temperatura']}°C {emoji}")

def historial_consultes(ciutat):
    """
    Simula un historial de consultes (guardant en fitxer)
    Args:
        ciutat: nom de la ciutat consultada
    """
    try:
        # Intentar carregar l'historial existent
        try:
            with open('historial_temps.json', 'r', encoding='utf-8') as f:
                historial = json.load(f)
        except FileNotFoundError:
            historial = []
        
        # Afegir nova consulta
        historial.append({
            'ciutat': ciutat,
            'data': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })
        
        # Mantenir només les últimes 20 consultes
        historial = historial[-20:]
        
        # Guardar historial
        with open('historial_temps.json', 'w', encoding='utf-8') as f:
            json.dump(historial, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"⚠️  No s'ha pogut guardar l'historial: {e}")

def mostra_historial():
    """Mostra l'historial de consultes"""
    try:
        with open('historial_temps.json', 'r', encoding='utf-8') as f:
            historial = json.load(f)
        
        if not historial:
            print("\n📭 No hi ha consultes en l'historial")
            return
        
        print("\n" + "="*60)
        print("📜 HISTORIAL DE CONSULTES")
        print("="*60)
        
        for consulta in reversed(historial[-10:]):  # Últimes 10
            print(f"🌍 {consulta['ciutat']}")
            print(f"   📅 {consulta['data']}")
    except FileNotFoundError:
        print("\n📭 No hi ha consultes en l'historial")
    except Exception as e:
        print(f"❌ Error llegint l'historial: {e}")

def menu_meteorologia():
    """Mostra el menú de meteorologia"""
    print("\n" + "="*60)
    print("CONSULTA METEOROLÒGICA")
    print("="*60)
    print("\n1. Consultar temps actual d'una ciutat")
    print("2. Consultar previsió (7 dies)")
    print("3. Consultar previsió (14 dies)")
    print("4. Comparar múltiples ciutats")
    print("5. Veure historial de consultes")
    print("0. Tornar al menú principal")

def main():
    """Funció principal de l'aplicació 5"""
    
    print("\n⚠️  NOTA: Aquesta aplicació requereix connexió a Internet")
    print("Utilitza l'API gratuïta Open-Meteo per obtenir dades meteorològiques")
    
    while True:
        menu_meteorologia()
        opcio = input("\nSelecciona una opció: ").strip()
        
        if opcio == "1":
            ciutat = input("\n🌍 Nom de la ciutat: ").strip()
            if not ciutat:
                print("❌ Has d'introduir una ciutat!")
                input("\nPrem ENTER per continuar...")
                continue
            
            print("\n🔍 Cercant informació...")
            coordenades = obte_coordenades_ciutat(ciutat)
            
            if not coordenades:
                print(f"❌ No s'ha pogut trobar '{ciutat}'")
                input("\nPrem ENTER per continuar...")
                continue
            
            lat, lon, nom_complet = coordenades
            temps = obte_temps_actual(lat, lon)
            
            if temps:
                mostra_temps_actual(nom_complet, temps)
                historial_consultes(nom_complet)
            else:
                print("❌ No s'han pogut obtenir les dades meteorològiques")
            
            input("\nPrem ENTER per continuar...")
        
        elif opcio == "2" or opcio == "3":
            dies = 7 if opcio == "2" else 14
            ciutat = input("\n🌍 Nom de la ciutat: ").strip()
            
            if not ciutat:
                print("❌ Has d'introduir una ciutat!")
                input("\nPrem ENTER per continuar...")
                continue
            
            print("\n🔍 Cercant informació...")
            coordenades = obte_coordenades_ciutat(ciutat)
            
            if not coordenades:
                print(f"❌ No s'ha pogut trobar '{ciutat}'")
                input("\nPrem ENTER per continuar...")
                continue
            
            lat, lon, nom_complet = coordenades
            previsions = obte_previsions(lat, lon, dies)
            
            if previsions:
                mostra_previsions(nom_complet, previsions, dies)
                historial_consultes(nom_complet)
            else:
                print("❌ No s'han pogut obtenir les previsions")
            
            input("\nPrem ENTER per continuar...")
        
        elif opcio == "4":
            print("\n🌍 Introdueix ciutats per comparar (separades per comes)")
            print("Exemple: Barcelona, Madrid, València, Sevilla")
            entrada = input("\nCiutats: ").strip()
            
            if not entrada:
                print("❌ Has d'introduir almenys una ciutat!")
                input("\nPrem ENTER per continuar...")
                continue
            
            ciutats = [c.strip() for c in entrada.split(',')]
            print("\n🔍 Obtenint informació...")
            compara_ciutats(ciutats)
            
            input("\nPrem ENTER per continuar...")
        
        elif opcio == "5":
            mostra_historial()
            input("\nPrem ENTER per continuar...")
        
        elif opcio == "0":
            break
        else:
            print("❌ Opció no vàlida!")
            input("Prem ENTER per continuar...")

if __name__ == "__main__":
    main()

"""
Aplicació 6: API REST de Gestió de Tasques
Crea un servei web senzill amb Flask per gestionar tasques
"""

try:
    from flask import Flask, jsonify, request
    FLASK_DISPONIBLE = True
except ImportError:
    FLASK_DISPONIBLE = False
    print("⚠️  Flask no està instal·lat!")

import json
import os
from datetime import datetime
import threading
import webbrowser
import time

# Base de dades simulada (en memòria)
tasques = []
comptador_id = 1

def carrega_tasques():
    """Carrega les tasques des d'un fitxer JSON"""
    global tasques, comptador_id
    
    if os.path.exists('tasques_api.json'):
        try:
            with open('tasques_api.json', 'r', encoding='utf-8') as f:
                dades = json.load(f)
                tasques = dades.get('tasques', [])
                comptador_id = dades.get('comptador_id', 1)
        except:
            pass

def guarda_tasques():
    """Guarda les tasques en un fitxer JSON"""
    try:
        with open('tasques_api.json', 'w', encoding='utf-8') as f:
            json.dump({
                'tasques': tasques,
                'comptador_id': comptador_id
            }, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Error guardant tasques: {e}")

if FLASK_DISPONIBLE:
    # Crear aplicació Flask
    app = Flask(__name__)
    
    @app.route('/')
    def index():
        """Pàgina principal amb documentació de l'API"""
        html = """
        <!DOCTYPE html>
        <html lang="ca">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>API de Tasques</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    max-width: 1000px;
                    margin: 0 auto;
                    padding: 20px;
                    background-color: #f5f5f5;
                }
                h1 {
                    color: #333;
                    border-bottom: 3px solid #4CAF50;
                    padding-bottom: 10px;
                }
                .endpoint {
                    background: white;
                    padding: 15px;
                    margin: 10px 0;
                    border-left: 4px solid #4CAF50;
                    border-radius: 4px;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                }
                .method {
                    display: inline-block;
                    padding: 4px 8px;
                    border-radius: 3px;
                    font-weight: bold;
                    color: white;
                    margin-right: 10px;
                }
                .get { background-color: #61affe; }
                .post { background-color: #49cc90; }
                .put { background-color: #fca130; }
                .delete { background-color: #f93e3e; }
                code {
                    background-color: #f4f4f4;
                    padding: 2px 6px;
                    border-radius: 3px;
                    font-family: monospace;
                }
                .exemple {
                    background-color: #f9f9f9;
                    padding: 10px;
                    border-radius: 4px;
                    margin-top: 10px;
                    font-family: monospace;
                    font-size: 14px;
                }
            </style>
        </head>
        <body>
            <h1>🚀 API de Gestió de Tasques</h1>
            <p>API REST per gestionar tasques amb operacions CRUD completes.</p>
            
            <div class="endpoint">
                <span class="method get">GET</span>
                <code>/api/tasques</code>
                <p>Obté totes les tasques</p>
                <div class="exemple">
                    Resposta: [{"id": 1, "titol": "Comprar pa", "completada": false, ...}, ...]
                </div>
            </div>
            
            <div class="endpoint">
                <span class="method get">GET</span>
                <code>/api/tasques/&lt;id&gt;</code>
                <p>Obté una tasca específica per ID</p>
            </div>
            
            <div class="endpoint">
                <span class="method post">POST</span>
                <code>/api/tasques</code>
                <p>Crea una nova tasca</p>
                <div class="exemple">
                    Body: {"titol": "Nova tasca", "descripcio": "Descripció opcional"}
                </div>
            </div>
            
            <div class="endpoint">
                <span class="method put">PUT</span>
                <code>/api/tasques/&lt;id&gt;</code>
                <p>Actualitza una tasca existent</p>
                <div class="exemple">
                    Body: {"titol": "Títol actualitzat", "completada": true}
                </div>
            </div>
            
            <div class="endpoint">
                <span class="method delete">DELETE</span>
                <code>/api/tasques/&lt;id&gt;</code>
                <p>Esborra una tasca</p>
            </div>
            
            <div class="endpoint">
                <span class="method get">GET</span>
                <code>/api/estadistiques</code>
                <p>Obté estadístiques de les tasques</p>
            </div>
            
            <h2>📝 Exemples amb cURL</h2>
            <div class="endpoint">
                <p><strong>Crear tasca:</strong></p>
                <div class="exemple">
curl -X POST http://localhost:5000/api/tasques \\<br>
  -H "Content-Type: application/json" \\<br>
  -d '{"titol":"Comprar llet","descripcio":"Al supermercat"}'
                </div>
            </div>
        </body>
        </html>
        """
        return html
    
    @app.route('/api/tasques', methods=['GET'])
    def obte_tasques():
        """GET - Obté totes les tasques"""
        return jsonify(tasques)
    
    @app.route('/api/tasques/<int:id>', methods=['GET'])
    def obte_tasca(id):
        """GET - Obté una tasca específica"""
        tasca = next((t for t in tasques if t['id'] == id), None)
        if tasca:
            return jsonify(tasca)
        return jsonify({'error': 'Tasca no trobada'}), 404
    
    @app.route('/api/tasques', methods=['POST'])
    def crea_tasca():
        """POST - Crea una nova tasca"""
        global comptador_id
        
        if not request.json or 'titol' not in request.json:
            return jsonify({'error': 'El títol és obligatori'}), 400
        
        nova_tasca = {
            'id': comptador_id,
            'titol': request.json['titol'],
            'descripcio': request.json.get('descripcio', ''),
            'completada': False,
            'data_creacio': datetime.now().isoformat()
        }
        tasques.append(nova_tasca)
        comptador_id += 1
        guarda_tasques()
        return jsonify(nova_tasca), 201
    @app.route('/api/tasques/<int:id>', methods=['PUT'])
    def actualitza_tasca(id):
        """PUT - Actualitza una tasca existent"""
        tasca = next((t for t in tasques if t['id'] == id), None)
        if not tasca:
            return jsonify({'error': 'Tasca no trobada'}), 404
        
        if not request.json:
            return jsonify({'error': 'Dades no vàlides'}), 400
        
        tasca['titol'] = request.json.get('titol', tasca['titol'])
        tasca['descripcio'] = request.json.get('descripcio', tasca['descripcio'])
        tasca['completada'] = request.json.get('completada', tasca['completada'])
        guarda_tasques()
        return jsonify(tasca)
    