# Interpreter poleceń odwróconej notacji polskiej

# Lista poleceń wprowadzana z klawiatury
Args = []

# Tablica wszystkich poleceń
Commands = {
    "exit":             lambda: CmdExit(),
    "commands":         lambda: CmdCommands(),
    "vars":             lambda: CmdVariables(),
    "=":                lambda: CmdSetVariable(),
    "const":            lambda: CmdConst(),
    "echo":             lambda: CmdEcho(),
    "inc":              lambda: CmdOperatorInc(),
    "dec":              lambda: CmdOperatorDec(),
    "+":                lambda: CmdOperatorAdd(),
    "-":                lambda: CmdOperatorSub(),
    "*":                lambda: CmdOperatorMul(),
    "/":                lambda: CmdOperatorDiv(),
}

# Słownik zmiennych
Variables = {}

def CmdExit():
    quit()
    return 

def CmdCommands():
    i = 0
    for Item in Commands.keys():
        print("{}:\t{}".format(i, Item))
        i = i+1

def CmdVariables():
    for Name, Value in Variables.items():
        print("{}:\t{}".format(Name, Value))

def CmdSetVariable():
    global Args
    Name = str(Args[0])
    
    ### Dodać sprawdzenie czy nazwa zmiennej nie koliduje z jakąś nazwą funkcji

    Args = Args[1:]
    Value = InterpreterGlobal()
    Variables[Name] = Value
    return Value

def CmdConst():
    return 123

def CmdEcho():
    return InterpreterGlobal()

def CmdOperatorInc():
    return InterpreterGlobal() + 1

def CmdOperatorDec():
    return InterpreterGlobal() - 1

def CmdOperatorAdd():
    return InterpreterGlobal() + InterpreterGlobal()

def CmdOperatorSub():
    return InterpreterGlobal() - InterpreterGlobal()

def CmdOperatorMul():
    return InterpreterGlobal() * InterpreterGlobal()

def CmdOperatorDiv():
    return InterpreterGlobal() / InterpreterGlobal()

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
def InterpreterGlobal():
    global Args

    # Odczytanie pierwszego elementu z listy, który będzie interpretowany przesunięcie pozostałych elementów
    if len(Args) == 0:
        return None
    Argument = str(Args[0])
    Args = Args[1:]

    # Sprawdznie czy to float
    if IsFloat(Argument):
        print("Argument {} to float".format(Argument))
        return float(Argument)

    # Sprawdzenie czy to zmienna
    if Argument in Variables:
        print("Argument {} to zmienna = {}".format(Argument, Variables[Argument]))
        return Variables[Argument]
    
    # Sprawdznie czy to polecenie
    if Argument in Commands:
        print("Argument {} to polecenie".format(Argument))
        return Commands[Argument]()

    # Nie udało się zinterpretować
    print("Argument {} jest inny".format(Argument))
    return None



# Funkcja main
def main():

    global Args
    
    while True:
        Args = input("> ")                                                          # Prompt
        Args = Args.split()                                                         # Rozbijanie wiersza polecen na poszczegolne wyrazy
        Result = InterpreterGlobal()
        print("Result = {}".format(Result))

if __name__ == "__main__":
	main()