# Prosty program demostracyjny do podstawowych kontrolek z TKinter

import tkinter as tk

# Okna główne
Root = tk.Tk()
Root.title("Hello World")

# Część 1 - kopiowanie tekstu poprzez StringVar
def Klik1():
    Text1.set("Label1 = " + Text1.get())

Text1 = tk.StringVar()
Text1.set("Label1")
Label1 = tk.Label(Root, textvariable = Text1)
Label1.grid(row = 0, column = 0)
Entry1 = tk.Entry(Root)
Entry1.grid(row = 1, column = 0)
Button1 = tk.Button(Root, text = "Skopiuj1", command = Klik1)
Button1.grid(row = 2, column = 0)

# Część 2 - kopiwanie tekstu bez StringVar
def Klik2():
    Label2.config(text = "Label2 = " + Entry2.get())

Label2 = tk.Label(Root, text = "Label2")
Label2.grid(row = 0, column = 1)
Entry2 = tk.Entry(Root)
Entry2.grid(row = 1, column = 1)
Button2 = tk.Button(Root, text = "Skopiuj2", command = Klik2)
Button2.grid(row = 2, column = 1)

# Main loop    
Root.mainloop() 

