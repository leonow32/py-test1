# Test slownikow

def Funkcja1(x):
    return x+1

def Funkcja2(x):
    return x+1


D = {
    "a": "aaa",
    "b": "bbb",
    "c": "ccc",
    "d": {
        "e": "eee",
        "f": "fff",
        "g": "ggg",
        "h": {
            "i": "iii",
            "j": "jjj",
            },
        "k": {
            "l": "lll",
            "m": "mmm",
            },
        },
    "n": "nnn",
    "o": Funkcja1,
    "p": Funkcja1,
    "q": Funkcja2,
    "r": Funkcja2,
    "s": lambda x: Funkcja1(x),
    "t": lambda: Funkcja1(1),
    }


def printDict(DictInstance, NestLevel):
    for a, b in DictInstance.items():
        if type(b) == dict:
            print("    " * NestLevel, a, ": ")
            printDict(b, NestLevel+1)
        else:
            print("    " * NestLevel, a, ": ", b, type(b))

    return

printDict(D, 0)
print("==1==")
arg = input("wpisz s:")
#print(D["s"](123))
print(D[arg](123))
print("==2==")
arg = input("wpisz t:")
#print(D["t"]())
print(D[arg]())
