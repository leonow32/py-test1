# Interpreter poleceń odwróconej notacji polskiej
from interpreter_core import *

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







# Funkcja main
def main():

    global Args

    Inter = InterpreterClass(Commands)
    
    while True:
        Args = input("> ")                                                          # Prompt
        
        Result = Inter.InterpreterGlobal(Args)
        print("Result = {}".format(Result))

if __name__ == "__main__":
	main()