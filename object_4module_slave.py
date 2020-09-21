# Definicja klasy
class Prostokat:

    #Zmienne
    Index   = 0     # Zmienna statyczna wspólna dla wszystkich instancji klasy
    Count   = 0     # Zmienna statyczna wspólna dla wszystkich instancji klasy
    A       = 0
    B       = 0
    Name    = ""

    # Konstruktor
    def __init__(self, Name, BokA, BokB):
        self.Name = Name + str(Prostokat.Index)
        Prostokat.Index += 1
        Prostokat.Count += 1
        self.A = BokA
        self.B = BokB

    # Destruktor
    def __del__(self):
        Prostokat.Count -= 1
        print(f"Destruktor {self.Name}, pozostało obiektów: {Prostokat.Count}")

    # Wyswietl dane
    def Info(self):
        print(f"{self.__class__.__name__}.{self.Name}\tA={self.A}; B={self.B}")

    # Oblicz pole
    def Area(self):
        return self.A * self.B

    # Oblicz obwod
    def Circuit(self):
        return 2 * self.A + 2 * self.B

# Definicja klasy
class Kolo:

    #Zmienne
    Index   = 0     # Zmienna statyczna wspólna dla wszystkich instancji klasy
    Count   = 0     # Zmienna statyczna wspólna dla wszystkich instancji klasy
    R       = 0
    Name    = ""

    # Konstruktor
    def __init__(self, Name, Radius):
        self.Name = Name + str(Kolo.Index)
        Kolo.Index += 1
        Kolo.Count += 1
        self.R = Radius

    # Destruktor
    def __del__(self):
        Kolo.Count -= 1
        print(f"Destruktor {self.Name}, pozostało obiektów: {Kolo.Count}")

    # Wyswietl dane
    def Info(self):
        print(f"{self.__class__.__name__}.{self.Name}\tR={self.R}")

    # Oblicz pole
    def Area(self):
        return 3.14 * self.R**2

    # Oblicz obwod
    def Circuit(self):
        return 2 * 3.14 * self.R
