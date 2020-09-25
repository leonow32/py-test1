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

    # Sprawdzenie czy podany argument jest liczbą
    def IsFloat(String):
        try:
            float(String)
            return True
        except ValueError:
            return False

    # Interpreter
    # Przyjmuje ciąg znaków będący poleceniem i zwraca wartość
#    def Interpreter(CommandLine):
#        return

    # Interpreter
    # Analizowany jest pierwszy element listy
    # - jeżeli jest liczbą, to jest zwracana liczba
    # - jeżeli jest poleceniem to wywoływana jest funkcja odpowiadająca temu poleceniu
    # - inaczej zwracany jest błąd
    def InterpreterGlobal(self, Args):
        
        # Rozbijanie wiersza polecen na poszczegolne wyrazy
        Args = Args.split()                                                         

        # Odczytanie pierwszego elementu z listy, który będzie interpretowany przesunięcie pozostałych elementów
        if len(Args) == 0:
            return None
        Argument = str(Args[0])
        Args = Args[1:]

        # Sprawdznie czy to float
        if InterpreterClass.IsFloat(Argument):
            print("Argument {} to float".format(Argument))
            return float(Argument)

        # Sprawdzenie czy to zmienna
        if Argument in InterpreterClass.Variables:
            print("Argument {} to zmienna = {}".format(Argument, Variables[Argument]))
            return Variables[Argument]
    
        # Sprawdznie czy to polecenie
        if Argument in InterpreterClass.Commands:
            print("Argument {} to polecenie".format(Argument))
            return Commands[Argument]()

        # Nie udało się zinterpretować
        print("Argument {} jest inny".format(Argument))
        return None

