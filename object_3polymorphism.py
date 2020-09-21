# Klasa bazowa
class Figura:

    # Zmienne
    Index   = 0     # Zmienna statyczna wspólna dla wszystkich instancji klasy
    Count   = 0     # Zmienna statyczna wspólna dla wszystkich instancji klasy
    Name = ""

    # Konstruktor
    def __init__(self, Name):
        Figura.Index += 1                               # Zmienna statyczna
        Figura.Count += 1                               # Zmienna statyczna
        self.Name = Name + str(Figura.Index)
        print(f"Konstruktor {self.Name}")
        

    # Destruktor
    def __del__(self):
        Figura.Count -= 1                            # Zmienna statyczna
        print(f"Destruktor {self.Name}, pozostało obiektów: {Prostokat.Count}")
        return

    # Info
    def Info(self):
        print(f"Figura: {self.Name}")

    # Obliczanie powierzchni
    def GetArea(self):
        raise NotImplemented

    # Obliczanie obwodu
    def GetCircuit(self):
        raise NotImplemented

# Klasa pochodna
class Prostokat(Figura):

    # Zmienne
    A       = 0
    B       = 0

    # Konstruktor
    def __init__(self, Name, BokA, BokB):
        super().__init__(Name)
        self.A = BokA
        self.B = BokB

    # Info
    def Info(self):
        print(f"Prostokat: {self.Name}\ta={self.A}, b={self.B}")

    # Obliczanie powierzchni
    def GetArea(self):
        return self.A * self.B

    # Obliczanie obwodu
    def GetCircuit(self):
        return 2 * self.A + 2 * self.B

# Klasa pochodna
class Kolo(Figura):

    # Zmienne
    R       = 0

    # Konstruktor
    def __init__(self, Name, Radius):
        super().__init__(Name)
        self.R = Radius

    # Info
    def Info(self):
        print(f"Kolo: {self.Name}\tr={self.R}")

    # Obliczanie powierzchni
    def GetArea(self):
        return 3.14 * self.R**2

    # Obliczanie obwodu
    def GetCircuit(self):
        return 2 * 3.14 * self.R

def PrintAllFigures(InputList):
    Index = 0
    for Item in InputList:
        print(str(Index) + "\t" + Item.Name + "\t" + str(type(Item)))
        Index += 1

def main():
    
    List = []
    List.append(Prostokat("P", 1, 2))
    List.append(Prostokat("P", 10, 20))
    List.append(Prostokat("P", 100, 200))
    List.append(Kolo("K", 1))
    List.append(Kolo("K", 10))
    List.append(Kolo("K", 100))
    
    PrintAllFigures(List)
    List.pop(2)
    PrintAllFigures(List)

    for item in List:        
        #print(f"{item.Name}\tArea = {item.GetArea()}\tCircuit = {item.GetCircuit()}")
        print(item.Name + "\tArea = " + str(item.GetArea()) + "\tCircuit = " + str(item.GetCircuit()))

if __name__ == "__main__":
    main()
