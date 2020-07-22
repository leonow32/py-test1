from tkinter import *
#import tkinter as tk

# Tworzenie okna głównego
Root = Tk()
Root.title("Hello World")

# Tworzenie kontrolki typu label
Label1 = Label(Root, text = "Hello world!")
Label1.pack()
Label1.pack(side = TOP)

# Co to jest?
e = Entry(Root, width=35, borderwidth=5)



# Main loop    
Root.mainloop() 