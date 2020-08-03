import tkinter as tk
from tkinter import ttk                 # To musi być żeby działał Combobox

# Zmienne globalne
Root = tk.Tk()


# OptionMenu
Result0 = tk.StringVar()
Result0.set("Tu beda wyniki")
Result0Label = tk.Label(Root, textvariable=Result0)
Result0Label.grid(row=0, column=0)

Options = [
    "Poniedzialek",
    "Wtorek",
    "Sroda",
    "Czwartek",
    "Piatek",
    "Sobota",
    "Niedziela"
]

OptionMenu1 = tk.OptionMenu(Root, Result0, *Options)              # uwaga na znak *
OptionMenu1.grid(row=1, column=0)


# Listbox
Result1Label = tk.Label(Root, text="Result1")
Result1Label.grid(row=0, column=1)

def ListBoxShow():
    Result1Label.config(text = ListBox.get(tk.ANCHOR) + str(ListBox.curselection()))

ListBox = tk.Listbox(Root)
ListBox.grid(row=1, column=1)
ListBox.insert(tk.END, *Options)

Button1 = tk.Button(Root, text="Read", command=ListBoxShow)
Button1.grid(row=2, column=1)

# ComboBox
Result2 = tk.StringVar()
Result2.set("Combo Result")

Options2 = [
    "Styczen",
    "Luty",
    "Marzec",
    "Kwiecień",
    "Maj",
    "Czerwiec",
    "Lipiec",
    "Sierpień",
    "Wrzesień",
    "Październik",
    "Listopad",
    "Grudzień"
]

Result2Label = tk.Label(Root, textvariable=Result2)
Result2Label.grid(row=0, column=2)

Combo1 = ttk.Combobox(Root, textvariable=Result2)
#Combo1['values'] = ("a", "bb", "ccc")
Combo1["values"] = Options2
Combo1.grid(row=1, column=2)


# Main loop    
Root.title("Testy list")
Root.geometry("500x500")
Root.mainloop() 


