# Prosty program demostracyjny do podstawowych kontrolek z TKinter

import tkinter as tk

# Funkcje
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
Button0 = tk.Button(Root, text="0", width=10, height=2, padx=3, pady=0, command=ButtonCmd)
Button1 = tk.Button(Root, text="1", width=10, height=2, padx=3, pady=0, command=ButtonCmd)
Button2 = tk.Button(Root, text="2", width=10, height=2, padx=3, pady=0, command=ButtonCmd)
Button3 = tk.Button(Root, text="3", width=10, height=2, padx=3, pady=0, command=ButtonCmd)
Button4 = tk.Button(Root, text="4", width=10, height=2, padx=3, pady=0, command=ButtonCmd)
Button5 = tk.Button(Root, text="5", width=10, height=2, padx=3, pady=0, command=ButtonCmd)
Button6 = tk.Button(Root, text="6", width=10, height=2, padx=3, pady=0, command=ButtonCmd)
Button7 = tk.Button(Root, text="7", width=10, height=2, padx=3, pady=0, command=ButtonCmd)
Button8 = tk.Button(Root, text="8", width=10, height=2, padx=3, pady=0, command=ButtonCmd)
Button9 = tk.Button(Root, text="9", width=10, height=2, padx=3, pady=0, command=ButtonCmd)
ButtonRET = tk.Button(Root, text="C", width=10, height=2, padx=3, pady=0, command=ButtonCmd)
ButtonCLR = tk.Button(Root, text="CLR", width=10, height=2, padx=3, pady=0, command=ButtonCmd)
ButtonADD = tk.Button(Root, text="+", width=10, height=2, padx=3, pady=0, command=ButtonCmd)
ButtonSUB = tk.Button(Root, text="-", width=10, height=2, padx=3, pady=0, command=ButtonCmd)
ButtonMUL = tk.Button(Root, text="*", width=10, height=2, padx=3, pady=0, command=ButtonCmd)
ButtonDIV = tk.Button(Root, text="/", width=10, height=2, padx=3, pady=0, command=ButtonCmd)
ButtonDOT = tk.Button(Root, text=",", width=10, height=2, padx=3, pady=0, command=ButtonCmd)
ButtonSGN = tk.Button(Root, text="+/-", width=10, height=2, padx=3, pady=0, command=ButtonCmd)
ButtonEXE = tk.Button(Root, text="=", width=10, height=2, padx=3, pady=20, command=ButtonCmd)

# Rozmieszczenie przycisków
ButtonRET.grid(row=1, column=0)
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



"""
# Część 2 - kopiwanie tekstu bez StringVar
def Klik2():
    Label2.config(text = "Label2 = " + Entry2.get())

Label2 = tk.Label(Root, text = "Label2")
Label2.grid(row = 0, column = 1)
Entry2 = tk.Entry(Root)
Entry2.grid(row = 1, column = 1)
Button2 = tk.Button(Root, text = "Skopiuj2", command = Klik2)
Button2.grid(row = 2, column = 1)
"""

# Main loop    
Root.mainloop() 


