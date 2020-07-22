from tkinter import *

# Zmiana tekstu po naciśnięciu przycisku
def Klik():
    myLabel = Label(Root, text = "Nowy Label").grid(row = 0, column = 3)

# Tworzenie okna głównego
Root = Tk()
Root.title("Hello World")

# Tworzenie kontrolki typu label
Label1 = Label(Root, text = "Hello world!")
Label2 = Label(Root, text = "Drugi text!")
Label3 = Label(Root, text = "Trzeci")

Label1.grid(row = 0, column = 0)
Label2.grid(row = 1, column = 1)
Label3.grid(row = 3, column = 3)

# To samo tylko w jednej linii
Label4 = Label(Root, text = "qwerty").grid(row = 0, column = 3)
Label5 = Label(Root, text = "abcdef").grid(row = 1, column = 1)

# Przycisk
Button1 = Button(Root, text = "Click me!", command = Klik).grid(row = 4, column = 0)
Button2 = Button(Root, text = "Click me!", state = DISABLED).grid(row = 5, column = 0)
Button3 = Button(Root, text = "Click me!", padx = 50, pady = 80).grid(row = 6, column = 0)


# Main loop    
Root.mainloop() 