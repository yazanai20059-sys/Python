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