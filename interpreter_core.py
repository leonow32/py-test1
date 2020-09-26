# Interpreter poleceń w wersji obiektowej
class InterpreterClass:
    
    # Lista poleceń wprowadzana z klawiatury
    Args = []

    # Słownik zmiennych
    Variables = {}

    # Słownik poleceń - jest przekazywany poprzez konstruktow lub funkcje XXXX
    Commands = {}

    # Konstruktor
    def __init__(self, Commands):
        print("Konstruktor interpretera")
        self.Commands = Commands
        i = 0
        for Item in Commands.keys():
            print(f"{i}:\t{Item}")
            i += 1

    # Dodawanie polecenia do tablicy poleceń
    def CommandAdd(self, CommandName, Lambda):
        print(f"Dodawanie {CommandName}, {Lambda}")
        self.Commands[CommandName] = Lambda

    # Sprawdzenie czy podany argument jest liczbą
    def IsFloat(String):
        try:
            float(String)
            return True
        except ValueError:
            return False

    # Interpreter
    # Analizowany jest pierwszy element listy
    # - jeżeli jest liczbą, to jest zwracana liczba
    # - jeżeli jest poleceniem to wywoływana jest funkcja odpowiadająca temu poleceniu
    # - inaczej zwracany jest błąd
    def Interpreter(self, InterpreterInstance):                                                        

        # Odczytanie pierwszego elementu z listy, który będzie interpretowany i przesunięcie pozostałych elementów
        if len(self.Args) == 0:
            return None
        Argument = str(self.Args[0])
        self.Args = self.Args[1:]

        # Sprawdznie czy to float
        if InterpreterClass.IsFloat(Argument):
            print("Argument {Argument} to float")
            return float(Argument)

        # Sprawdzenie czy to zmienna
        if Argument in InterpreterClass.Variables:
            print(f"Argument {Argument} to zmienna = {self.Variables[Argument]}")
            return self.Variables[Argument]
    
        # Sprawdznie czy to polecenie
        if Argument in self.Commands:
            print(f"Argument {Argument} to polecenie")
            return self.Commands[Argument](InterpreterInstance)

        # Nie udało się zinterpretować
        print(f"Argument {Argument} jest inny")
        return None

    # Interpreter
    # Przyjmuje ciąg znaków będący poleceniem i zwraca wartość
    def InterpreterString(self, CommandLine, InterpreterInstance):

        # Rozbijanie wiersza polecen na poszczegolne wyrazy
        self.Args = CommandLine.split() 

        return self.Interpreter(InterpreterInstance)

