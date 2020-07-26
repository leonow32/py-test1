# Prosty program demostracyjny do podstawowych kontrolek z TKinter

import tkinter as tk

# Funkcje
def ButtonCmdDigit(Dig):
    Current = str(Display.get())
    if Current == "0" and len(Current) == 1:
        print("zero")
        Current = ""
    Display.delete(0, tk.END)
    Display.insert(0, str(Current) + str(Dig))

def ButtonCmdClear():
    Display.delete(0, tk.END)

def ButtonCmdUndo():
    Current = str(Display.get())
    Current = Current[0:-1]
    Display.delete(0, tk.END)
    Display.insert(0, Current)

def ButtonCmd():
    return
    

# Okna główne
Root = tk.Tk()
Root.title("Kalkulator")

# Wyświetlacz
Display = tk.Entry(Root, width=50)
Display.grid(row=0, column=0, columnspan=4)
Display.insert(0, "0")

# Definicje przycisków
Button0 = tk.Button(Root, text="0", width=10, height=2, padx=3, pady=0, command=lambda: ButtonCmdDigit(0))
Button1 = tk.Button(Root, text="1", width=10, height=2, padx=3, pady=0, command=lambda: ButtonCmdDigit(1))
Button2 = tk.Button(Root, text="2", width=10, height=2, padx=3, pady=0, command=lambda: ButtonCmdDigit(2))
Button3 = tk.Button(Root, text="3", width=10, height=2, padx=3, pady=0, command=lambda: ButtonCmdDigit(3))
Button4 = tk.Button(Root, text="4", width=10, height=2, padx=3, pady=0, command=lambda: ButtonCmdDigit(4))
Button5 = tk.Button(Root, text="5", width=10, height=2, padx=3, pady=0, command=lambda: ButtonCmdDigit(5))
Button6 = tk.Button(Root, text="6", width=10, height=2, padx=3, pady=0, command=lambda: ButtonCmdDigit(6))
Button7 = tk.Button(Root, text="7", width=10, height=2, padx=3, pady=0, command=lambda: ButtonCmdDigit(7))
Button8 = tk.Button(Root, text="8", width=10, height=2, padx=3, pady=0, command=lambda: ButtonCmdDigit(8))
Button9 = tk.Button(Root, text="9", width=10, height=2, padx=3, pady=0, command=lambda: ButtonCmdDigit(9))
ButtonUND = tk.Button(Root, text="C", width=10, height=2, padx=3, pady=0, command=ButtonCmdUndo)
ButtonCLR = tk.Button(Root, text="CLR", width=10, height=2, padx=3, pady=0, command=ButtonCmdClear)
ButtonADD = tk.Button(Root, text="+", width=10, height=2, padx=3, pady=0, command=ButtonCmd)
ButtonSUB = tk.Button(Root, text="-", width=10, height=2, padx=3, pady=0, command=ButtonCmd)
ButtonMUL = tk.Button(Root, text="*", width=10, height=2, padx=3, pady=0, command=ButtonCmd)
ButtonDIV = tk.Button(Root, text="/", width=10, height=2, padx=3, pady=0, command=ButtonCmd)
ButtonDOT = tk.Button(Root, text=",", width=10, height=2, padx=3, pady=0, command=ButtonCmd)
ButtonSGN = tk.Button(Root, text="+/-", width=10, height=2, padx=3, pady=0, command=ButtonCmd)
ButtonEXE = tk.Button(Root, text="=", width=10, height=2, padx=3, pady=20, command=ButtonCmd)

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


