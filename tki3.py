from tkinter import *

# Zmiana tekstu po naciśnięciu przycisku
def ChangeLabel():
    #myLabel = Label(Root, text = "Nowy Label").grid(row = 0, column = 3)
    Label2.text.set("asd")

# Okna główne
Root = Tk()
Root.title("Hello World")

# Tworzenie kontrolki typu label
Label1 = Label(Root, text = "Jak się nazywasz?").grid(row = 0, column = 0)

# Textbox
Textbox1 = Entry(Root, width = 25).grid(row = 1, column = 0)
#Textbox1.insert("Jan Kowalski")

# Przycisk
Button1 = Button(Root, text = "Click me!", command = ChangeLabel).grid(row = 2, column = 0)

# Pozdrowienie
Label2 = Label(Root, text = "_").grid(row = 3, column = 0)



# Main loop    
Root.mainloop() 