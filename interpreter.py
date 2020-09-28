# Interpreter poleceń odwróconej notacji polskiej
from interpreter_core import *



# Tablica wszystkich poleceń
Commands = {
    "exit":             lambda ii: CmdExit(ii),
    "all":              lambda ii: CmdAllCommands(ii),
    "vars":             lambda ii: CmdVariables(ii),
    "=":                lambda ii: CmdSetVariable(ii),
    "const":            lambda ii: CmdConst(ii),
    "echo":             lambda ii: CmdEcho(ii),
    "inc":              lambda ii: CmdOperatorInc(ii),
    "dec":              lambda ii: CmdOperatorDec(ii),
    "+":                lambda ii: CmdOperatorAdd(ii),
    "-":                lambda ii: CmdOperatorSub(ii),
    "*":                lambda ii: CmdOperatorMul(ii),
    "/":                lambda ii: CmdOperatorDiv(ii),
}

Commands2 = {
    "all":              lambda ii: CmdAllCommands(ii),
    "echo":             lambda ii: CmdEcho(ii),
}



def CmdExit(ii):
    quit()
    return 

def CmdAllCommands(ii):
    i = 0
    for Item in ii.Commands.keys():
        print(f"{i}:\t{Item}")
        i = i+1

def CmdVariables(ii):
    for Name, Value in ii.Variables.items():
        print(f"{Name}:\t{Value}")

def CmdSetVariable(ii):
    Name = str(ii.Args[0])
    
    ### Dodać sprawdzenie czy nazwa zmiennej nie koliduje z jakąś nazwą funkcji

    ii.Args = ii.Args[1:]
    Value = ii.Interpreter(ii)
    ii.Variables[Name] = Value
    return Value

def CmdConst(ii):
    return 123

def CmdEcho(ii):
    return ii.Interpreter(ii)

def CmdOperatorInc(ii):
    return ii.Interpreter(ii) + 1

def CmdOperatorDec(ii):
    return ii.Interpreter(ii) - 1

def CmdOperatorAdd(ii):
    return ii.Interpreter(ii) + ii.Interpreter(ii)

def CmdOperatorSub(ii):
    return ii.Interpreter(ii) - ii.Interpreter(ii)

def CmdOperatorMul(ii):
    return ii.Interpreter(ii) * ii.Interpreter(ii)

def CmdOperatorDiv(ii):
    return ii.Interpreter(ii) / ii.Interpreter(ii)

def CmdTestDodawaniaPolecen(ii):
    print("Polecenie dodane po konstruktorze")
    return None





# Funkcja main
def main():

    # Instancja interpretera
    Inter0 = InterpreterClass(Commands)
    Inter0.CommandAdd("dodane", lambda ii: CmdTestDodawaniaPolecen(ii))

    #Inter1 = InterpreterClass(Commands2)
    
    while True:
        InputCommand = input("0> ")                                                          # Prompt
        Result = Inter0.InterpreterString(InputCommand, Inter0)
        print(f"Result0 = {Result}")

        #InputCommand = input("1> ")                                                          # Prompt
        #Result = Inter1.InterpreterString(InputCommand, Inter1)
        #print(f"Result1 = {Result}")

if __name__ == "__main__":
	main()