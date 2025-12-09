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