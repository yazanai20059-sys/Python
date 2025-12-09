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