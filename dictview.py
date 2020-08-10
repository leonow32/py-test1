# Test slownikow

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
        "k": "kkk",
        },
    "l": "lll",
    }


def printDict(DictInstance, NestLevel):
    for a, b in DictInstance.items():
        print("x" * NestLevel, a, ": ", b)

    return

print(D)

printDict(D, 2)
