from math import sqrt

# Klasa bazowa
class Punkt2D:

    # Zmienne 
    X = 0
    Y = 0
    Dist = 0
    Name = ""

    # Konstruktor
    def __init__(self, X, Y, Name):
        self.X = X
        self.Y = Y
        self.Name = Name
        self.Dist = sqrt(X**2 + Y**2)
        print(f"Creaded point {Name}=({X},{Y}), distance {self.Dist}")

    # Destruktor
    def __del__(self):
        print(f"Deleted point {self.Name}=({self.X},{self.Y}), distance {self.Dist}")

    # Wyświetlenie współrzędnych
    def Info(self):
        print(f"{self.Name}=({self.X},{self.Y}), dist={self.Dist}")

    # Operator +
    def __add__(a, b):
        return Punkt2D(a.X + b.X, a.X + b.Y, a.Name + b.Name)

    # Operator -
    def __sub__(a, b):
        return Punkt2D(a.X - b.X, a.X - b.Y, a.Name + b.Name)

    # Operator *
    def __mul__(a, b):
        return Punkt2D(a.X * b.X, a.X * b.Y, a.Name + b.Name)

    # Operator /
    def __truediv__(a, b):
        return Punkt2D(a.X / b.X, a.X / b.Y, a.Name + b.Name)

    # Operator =
    def __eq__(a, b):
        return a.Dist == b.Dist

    # Operator !=
    def __nq__(a, b):
        return a.Dist != b.Dist

    # Operator >
    def __gt__(a, b):
        return a.Dist > b.Dist

    # Operator >=
    def __ge__(a, b):
        return a.Dist >= b.Dist

    # Operator <
    def __gt__(a, b):
        return a.Dist < b.Dist

    # Operator <=
    def __ge__(a, b):
        return a.Dist <= b.Dist

# Main
def main():

    P1 = Punkt2D(3, 4, "P1")
    P1a = Punkt2D(-3, -4, "P1a")
    # P1.Info()

    P2 = Punkt2D(6, 8, "P2")
    # P2.Info()

    """
    P3 = P1 + P2
    P3.Info()

    P3 = P1 - P2
    P3.Info()

    P3 = P1 * P2
    P3.Info()

    P3 = P1 / P2
    P3.Info()
    """

    print(P1 < P1a)
    print(P1 <= P1a)


    return

# Main
if __name__ == "__main__":
    main()
