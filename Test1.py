# Prosty program demostracyjny do podstawowych kontrolek z TKinter

import tkinter as tk
import tkinter.messagebox as tkmb
import platform

print(platform.python_version())

# Zmienne globalne
FirstNum = 0
Operation = ' '
DisplayResult = False

# Funkcje
def ButtonCmdDigit(Dig):
    global DisplayResult
    Current = str(Display.get())
    if DisplayResult:
        DisplayResult = False
        print("Result clear")
        Current = ""
    if Current == "0" and len(Current) == 1:
        print("zero")
        Current = ""
    Display.delete(0, tk.END)
    Display.insert(0, str(Current) + str(Dig))

def ButtonCmdDot():
    Current = str(Display.get())
    if(Current.count('.') == 0):
        global DisplayResult
        if DisplayResult:
            DisplayResult = False
            print("Result clear")
            Current = "0"
        Display.delete(0, tk.END)
        Display.insert(0, str(Current) + '.')
    else:
        print("juz jest dot")

def ButtonCmdClear():
    Display.delete(0, tk.END)
    Display.insert(0, "0")
    FirstNum = 0
    Operation = ' '

def ButtonCmdUndo():
    Current = str(Display.get())
    Current = Current[0:-1]
    Display.delete(0, tk.END)
    Display.insert(0, Current)

def ButtonCmdOperation(Operator):
    global Operation
    global FirstNum 
    Operation = Operator
    FirstNum = str(Display.get())
    Display.delete(0, tk.END)
    Display.insert(0, "0")

def ButtonCmdSign():
    Current = str(Display.get())
    if Current[0] == '-':
        Current = Current[1:len(Current)]
    else:
        Current = "-" + Current
    Display.delete(0, tk.END)
    Display.insert(0, Current)

def ButtonCmdExe():
    global FirstNum
    global DisplayResult
    SecondNum = str(Display.get())
    Result = 0
    print(FirstNum, Operation, SecondNum)
    if Operation == '+':
        Result = float(FirstNum) + float(SecondNum)
    elif Operation == '-':
        Result = float(FirstNum) - float(SecondNum)
    elif Operation == '*':
        Result = float(FirstNum) * float(SecondNum)
    elif Operation == '/':
        if float(SecondNum) == 0:
            tkmb.showerror("Title4", "Message4")
        else:
            Result = float(FirstNum) / float(SecondNum)
    else:
        print("Zly opcode")
    Display.delete(0, tk.END)
    Display.insert(0, Result)
    DisplayResult = True

def ButtonCmd():
    return
    

# Okna główne
Root = tk.Tk()
Root.title("Kalkulator")

# Wyświetlacz
Display = tk.Entry(Root, width=25, font="Consolas 20")
Display.grid(row=0, column=0, columnspan=4)
Display.insert(0, "0")

# Definicje przycisków
Button0 = tk.Button(Root, text="0", font="Consolas 12", width=10, height=2, padx=0, pady=0, command=lambda: ButtonCmdDigit(0))
Button1 = tk.Button(Root, text="1", font="Consolas 12", width=10, height=2, padx=0, pady=0, command=lambda: ButtonCmdDigit(1))
Button2 = tk.Button(Root, text="2", font="Consolas 12", width=10, height=2, padx=0, pady=0, command=lambda: ButtonCmdDigit(2))
Button3 = tk.Button(Root, text="3", font="Consolas 12", width=10, height=2, padx=0, pady=0, command=lambda: ButtonCmdDigit(3))
Button4 = tk.Button(Root, text="4", font="Consolas 12", width=10, height=2, padx=0, pady=0, command=lambda: ButtonCmdDigit(4))
Button5 = tk.Button(Root, text="5", font="Consolas 12", width=10, height=2, padx=0, pady=0, command=lambda: ButtonCmdDigit(5))
Button6 = tk.Button(Root, text="6", font="Consolas 12", width=10, height=2, padx=0, pady=0, command=lambda: ButtonCmdDigit(6))
Button7 = tk.Button(Root, text="7", font="Consolas 12", width=10, height=2, padx=0, pady=0, command=lambda: ButtonCmdDigit(7))
Button8 = tk.Button(Root, text="8", font="Consolas 12", width=10, height=2, padx=0, pady=0, command=lambda: ButtonCmdDigit(8))
Button9 = tk.Button(Root, text="9", font="Consolas 12", width=10, height=2, padx=0, pady=0, command=lambda: ButtonCmdDigit(9))
ButtonUND = tk.Button(Root, text="C", font="Consolas 12", width=10, height=2, padx=0, pady=0, command=ButtonCmdUndo)
ButtonCLR = tk.Button(Root, text="CLR", font="Consolas 12", width=10, height=2, padx=0, pady=0, command=ButtonCmdClear)
ButtonADD = tk.Button(Root, text="+", font="Consolas 12", width=10, height=2, padx=0, pady=0, command=lambda: ButtonCmdOperation('+'))
ButtonSUB = tk.Button(Root, text="-", font="Consolas 12", width=10, height=2, padx=0, pady=0, command=lambda: ButtonCmdOperation('-'))
ButtonMUL = tk.Button(Root, text="*", font="Consolas 12", width=10, height=2, padx=0, pady=0, command=lambda: ButtonCmdOperation('*'))
ButtonDIV = tk.Button(Root, text="/", font="Consolas 12", width=10, height=2, padx=0, pady=0, command=lambda: ButtonCmdOperation('/'))
ButtonDOT = tk.Button(Root, text=",", font="Consolas 12", width=10, height=2, padx=0, pady=0, command=ButtonCmdDot)
ButtonSGN = tk.Button(Root, text="+/-", font="Consolas 12", width=10, height=2, padx=0, pady=0, command=ButtonCmdSign)
ButtonEXE = tk.Button(Root, text="=", font="Consolas 12", width=10, height=2, padx=0, pady=25, command=ButtonCmdExe)

# Rozmieszczenie przycisków
ButtonUND.grid(row=1, column=0)
ButtonCLR.grid(row=1, column=1)
ButtonDIV.grid(row=1, column=2)
ButtonMUL.grid(row=1, column=3)

Button7.grid(row=2, column=0)
Button8.grid(row=2, column=1)
Button9.grid(row=2, column=2)
ButtonSUB.grid(row=2, column=3)

Button4.grid(row=3, column=0)
Button5.grid(row=3, column=1)
Button6.grid(row=3, column=2)
ButtonADD.grid(row=3, column=3)

Button1.grid(row=4, column=0)
Button2.grid(row=4, column=1)
Button3.grid(row=4, column=2)
ButtonEXE.grid(row=4, column=3, rowspan=2)

Button0.grid(row=5, column=0)
ButtonDOT.grid(row=5, column=1)
ButtonSGN.grid(row=5, column=2)

# Main loop    
Root.mainloop() 


