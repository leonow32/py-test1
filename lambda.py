# Test slowniko i funkcji lambda

def OperationNone(x):
    return "Default"

def OperationInc(x):
    return x+1

def OperationDec(x):
    return x-1


Commands = {
    "inc": lambda arg: OperationInc(arg),
    "dec": lambda arg: OperationDec(arg),
    }

Commands.setdefault("0", OperationNone)

def PrintDict(DictInstance, NestLevel):
    for a, b in DictInstance.items():
        if type(b) == dict:
            print("    " * NestLevel, a, ":", type(b))
            printDict(b, NestLevel+1)
        else:
            print("    " * NestLevel, a, ":", b, type(b))

    return

cmd = ""



def main():
    PrintDict(Commands, 0)
    while True:
        cmd = input("> ")
        
        if cmd == "exit":
            quit()
            
        elif cmd == "print":
            PrintDict(Commands, 0)
            
        elif cmd == "test":
            print("Hello")

        else:
            print(Commands[cmd](100))

if __name__ == "__main__":
	main()