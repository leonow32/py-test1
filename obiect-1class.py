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


def main():
    
    print(f"Liczba prostokatow: {Prostokat.Count}")
    Prostokat.Count
    Prostokat1 = Prostokat("P", 1, 2)
    Prostokat1.Info()
    print("Pole\t= {}".format(Prostokat1.Area()))
    print("Obwod\t= {}".format(Prostokat1.Circuit()))

    print(f"Liczba prostokatow: {Prostokat.Count}")
    Prostokat2 = Prostokat("P", 10, 20)
    Prostokat2.Info()
    print("Pole\t= {}".format(Prostokat2.Area()))
    print("Obwod\t= {}".format(Prostokat2.Circuit()))

    print(f"Liczba prostokatow: {Prostokat.Count}")
    Prostokat3 = Prostokat("P", 100, 200)
    Prostokat3.Info()
    print("Pole\t= {}".format(Prostokat2.Area()))
    print("Obwod\t= {}".format(Prostokat2.Circuit()))

    print(f"Liczba prostokatow: {Prostokat.Count}")

    print(f"Liczba kół: {Kolo.Count}")
    Kolo1 = Kolo("K", 1)
    Kolo1.Info()
    print("Pole\t= {}".format(Kolo1.Area()))
    print("Obwod\t= {}".format(Kolo1.Circuit()))

    print(f"Liczba kół: {Kolo.Count}")
    Kolo2 = Kolo("K", 10)
    Kolo2.Info()
    print("Pole\t= {}".format(Kolo2.Area()))
    print("Obwod\t= {}".format(Kolo2.Circuit()))

    print(f"Liczba kół: {Kolo.Count}")
    Kolo3 = Kolo("K", 100)
    Kolo3.Info()
    print("Pole\t= {}".format(Kolo3.Area()))
    print("Obwod\t= {}".format(Kolo3.Circuit()))

    print(f"Liczba kół: {Kolo.Count}")

if __name__ == "__main__":
    main()

