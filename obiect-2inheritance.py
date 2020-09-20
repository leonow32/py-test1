# Klasa bazowa
class Zwierz:

    #Zmienne
    Nazwa = ""
    Wiek  = 0
    Waga  = 0

    # Konstruktor
    def __init__(self, Nazwa, Wiek, Waga):
        print(f"Nowy zwierzak: {Nazwa}, Wiek={Wiek}, Waga={Waga}")
        self.Nazwa = Nazwa
        self.Wiek  = Wiek
        self.Waga  = Waga

    # Destruktor
    def __del__(self):
        print(f"Destruktor {self.Nazwa}")

    # Wyswietl dane
    def Info(self):
        print(f"Zwierzak {self.Nazwa}, {self.Wiek}, {self.Waga}")

    # Metoda, która ma być nadpisana przez klasy pochodne
    def DajGlos(self):
        print("Glos!")

# Klasa pochodna
class Pies(Zwierz):
    
    # Metoda tylko dla klasy pochodnej
    def Szczekaj(self):
        print("Hau hau!")

    # Metoda nadpisująca metode klasy bazowej
    def DajGlos(self):
        print("Nadpisujące: Hau hau!")
    
    pass

# Klasa pochodna
class Kot(Zwierz):

    # Metoda tylko dla kasy pochodnej
    def Miaucz(self):
        print("Miau")

    # Metoda nadpisująca metode klasy bazowej
    def DajGlos(self):
        print("Nadpisujące: Miau!")

# Klasa pochodna
class Krolik(Zwierz):

    # Konstruktor przyjmujący dodatkowy argument
    def __init__(self, Nazwa, Wiek, Waga, Kolor):
        super().__init__(Nazwa, Wiek, Waga)             # Wywołanie konstruktora klasy bazowej
        self.Kolor = Kolor

    # Metoda tylko dla kasy pochodnej
    def Piszcz(self):
        print("Pii")

    # Metoda nadpisująca metode klasy bazowej
    def DajGlos(self):
        super().DajGlos()                               # Wywołanie metody z klasy bazowej


# Funkcja main
def main():
    
    Reksio = Pies("Reksio", 10, 20)
    Reksio.Info()
    Reksio.Szczekaj()
    Reksio.DajGlos()

    Filemon = Kot("Filemon", 5, 10)
    Filemon.Info()
    Filemon.Miaucz()
    Filemon.DajGlos()

    Pulpi = Krolik("Pulpi", 5, 5, "Biały")
    Pulpi.DajGlos()

    

if __name__ == "__main__":
    main()

