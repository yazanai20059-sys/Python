from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, especie, edat):
        self.especie = especie
        self.edat = edat
    
    @abstractmethod
    def xerrar(self):
        pass
    
    @abstractmethod
    def mourem(self):
        pass
    
    def quisoc(self):
        print("{} fa un crit de felicitat!".format(self.especie))

class Cavall(Animal):
    def __init__(self, edat):
        super().__init__("Cavall", edat)
    
    def xerrar(self):
        print("El cavall fa 'Iiihaaa!'")
    
    def mourem(self):
        print("El cavall corre ràpidament.")

class Dofí(Animal):
    def __init__(self, edat):
        super().__init__("Dofí", edat)
    
    def xerrar(self):
        print("El dofí fa 'Eeeii!'")
    
    def mourem(self):
        print("El dofí nedant per l'oceà.")
    
class Abella(Animal):
    def __init__(self, edat):
        super().__init__("Abella", edat)
    
    def xerrar(self):
        print("L'abelleta fa 'Bzzzzzzz!'")
    
    def mourem(self):
        print("L'abelleta vola d'una flor a una altra.")
    
    def picar(self):
        print("L'abelleta pica amb el seu agulló!")

class Humà(Animal):
    def __init__(self, edat, nom):
        super().__init__("Humà", edat)
        self.nom = nom
    
    def xerrar(self):
        print("{} diu: 'Hola!'".format(self.nom))
    
    def mourem(self):
        print("{} camina tranquil·lament.".format(self.nom))
    
class Fiet(Humà):
    def __init__(self, edat, nom, pares):
        super().__init__(edat, nom)
        self.pares = pares
    
    def nompares(self):
        print("Els pares de {} són: {}".format(self.nom, ", ".join(self.pares)))

class Centaure(Cavall, Humà):
    def __init__(self, edat, nom):
        Cavall.__init__(self, edat)
        Humà.__init__(self, edat, nom)
    
    def xerrar(self):
        print("{} (Centaure) diu: 'Hola, sóc mig humà, mig cavall!'".format(self.nom))
    
    def mourem(self):
        print("{} (Centaure) galopa i camina.".format(self.nom))

class Xou(Animal):
    def __init__(self, especie, edat):
        super().__init__(especie, edat)
    
    def xerrar(self):
        print("El xou de {} fa soroll!".format(self.especie))
    
    def mourem(self):
        print("El xou de {} es mou de manera espectacular!".format(self.especie))

animals = [
    Cavall(5),
    Dofí(3),
    Abella(1),
    Humà(25, "Joan"),
    Fiet(20, "Anna", ["Marta", "Carles"]),
    Centaure(30, "Orfeu"),
    Xou("Circ", 10)
]

for animal in animals:
    animal.xerrar()
    animal.mourem()
    animal.quisoc()

    if isinstance(animal, Fiet):
        animal.nompares()

    if isinstance(animal, Abella):
        animal.picar()