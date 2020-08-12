# Test slownika i funkcji lambda

# Tablica wszystkich poleceń
Commands = {
    "inc":              lambda Args: OperationInc(Args),
    "dec":              lambda Args: OperationDec(Args),
    "+":                lambda Args: OperationAdd(Args),
    "-":                lambda Args: OperationSub(Args),
    "*":                lambda Args: OperationMul(Args),
    "/":                lambda Args: OperationDiv(Args),
    "show":             lambda Args: ShowArgs(Args),
    "pd":               lambda Args: PrintDictCmd(Args),
    "l1":               lambda Args: CmdPrintList1(Args),
    "l2":               lambda Args: CmdPrintList2(Args),
    "r":                lambda Args: CmdRekurencja(Args),
    "exit":             lambda Args: Exit(Args),
    }

# Interpreter
# Analizowany jest pierwszy element listy
# - jeżeli jest liczbą, to jest zwracana liczba
# - jeżeli jest poleceniem to wywoływana jest funkcja odpowiadająca temu poleceniu
# - inaczej zwracany jest błąd
def Interpreter(Args):
    Result = Commands[Args[0]](Args) if Args[0] in Commands else "Bad command"
    return Result

List = [
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    ]

def PrintList(inp):
    i = 0

    for item in inp:
        print("{}:\t{}".format(i, item))
        inp[i] = inp[i] * 10
        i = i+1

def CmdPrintList1(Args):
    PrintList(List)
    return ""

def CmdPrintList2(Args):
    PrintList(List[1:3])
    return ""

def Rekurencja(InputList):

    print("==== List count: {}".format(len(InputList)))
    if len(InputList) == 0:
        return

    i = 0;
    for value in InputList:
        print("{}\t{}".format(i, value))
        i = i+1
    
    # Wywolanie z ta sama lista, ale bez pierwszego elementu
    Rekurencja(InputList[1:])     
        
    return

def CmdRekurencja(Args):
    Rekurencja(List)
    return ""

def Exit(Args):
    quit()

def ShowArgs(Args):
    i = 0;
    for value in Args:
        print("{}\t{}".format(i, value))
        i = i+1
    return ""

def OperationInc(Args):
    return float(Args[1]) + 1

def OperationDec(Args):
    return float(Args[1]) - 1

def OperationAdd(Args):
    return float(Args[1]) + float(Args[2])

def OperationSub(Args):
    return float(Args[1]) - float(Args[2])

def OperationMul(Args):
    return float(Args[1]) * float(Args[2])

def OperationDiv(Args):
    return float(Args[1]) / float(Args[2])

def PrintDictCmd(Args):
    PrintDict(Commands, 0)
    return ""

# Wyświetlenie słownika
def PrintDict(DictInstance, NestLevel):
    for a, b in DictInstance.items():
        if type(b) == dict:
            print("    " * NestLevel, a, ":", type(b))
            printDict(b, NestLevel+1)
        else:
            print("    " * NestLevel, a, ":", b, type(b))

# Funkcja main
def main():
    PrintDict(Commands, 0)
    
    while True:
        Args = input("> ")                                                          # Prompt
        Args = Args.split()                                                         # Rozbijanie wiersza polecen na poszczegolne wyrazy
        if len(Args) == 0: continue                                                 # Kontrola czy wprowadzono chociaz jeden argument
        #print(Commands[Args[0]](Args) if Args[0] in Commands else "Bad command")    # Wykonanie polecenia
        Result = Interpreter(Args)
        print("Result={}".format(Result))

if __name__ == "__main__":
	main()