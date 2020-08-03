import tkinter as tk
from tkinter import ttk                 # To musi być żeby działał Combobox
import sqlite3

# Zmienne globalne
Root = tk.Tk()
Root.title("Database")


# Zapisanie danych do bazy
def Submit():
    
    # Utworzenie połączenia z bazą danych
    Connection = sqlite3.connect("database.db")
    
    # Kursor
    Cursor = Connection.cursor()
    
    # Polecenie
    Cursor.execute("INSERT INTO Ludzie VALUES (:f_name, :f_surname, :f_age)",
        {
            "f_name": NameEntry.get(),
            "f_surname": SurnameEntry.get(),
            "f_age": AgeEntry.get()
        }               
    )

    # Commit
    Connection.commit()

    # Zamknięcie połączenia z bazą danych
    Connection.close()   

    # Czyszczenie
    NameEntry.delete(0, tk.END)
    SurnameEntry.delete(0, tk.END)
    AgeEntry.delete(0, tk.END)
    return


# Odczytanie wszystkich rekordów
def ShowAll():

    # Utworzenie połączenia z bazą danych
    Connection = sqlite3.connect("database.db")
    
    # Kursor
    Cursor = Connection.cursor()
    
    # Polecenie
    Cursor.execute("SELECT *,oid FROM Ludzie")
    Result = Cursor.fetchall()
    print(Result)

    # Commit
    Connection.commit()

    # Zamknięcie połączenia z bazą danych
    Connection.close()   

    # Wyświetlenie
    ShowAllLabel["text"] = ""
    for Record in Result:
        for Item in Record:
            ShowAllLabel["text"] += str(Item) + ","
        ShowAllLabel["text"] += "\n"
    
    return

# Odczyt danych z bazy
def Query(Index):
    Index = int(Index)

    # Utworzenie połączenia z bazą danych
    Connection = sqlite3.connect("database.db")
    
    # Kursor
    Cursor = Connection.cursor()
    
    # Polecenie
    Cursor.execute("SELECT *,oid FROM Ludzie")
    Result = Cursor.fetchall()
    print(Result)

    # Commit
    Connection.commit()

    # Zamknięcie połączenia z bazą danych
    Connection.close()   

    # Czyszczenie
    NameEntry.delete(0, tk.END)
    SurnameEntry.delete(0, tk.END)
    AgeEntry.delete(0, tk.END)

    # Wyświetlenie
    NameEntry.insert(0, Result[Index][0])
    SurnameEntry.insert(0, Result[Index][1])
    AgeEntry.insert(0, Result[Index][2])
    return


# Kasowanie rekordów
def Delete(Index):

    # Utworzenie połączenia z bazą danych
    Connection = sqlite3.connect("database.db")
    
    # Kursor
    Cursor = Connection.cursor()
    
    # Polecenie
    Cursor.execute("DELETE from Ludzie WHERE oid=" + str(Index))
    #Cursor.execute("DELETE from Ludzie WHERE Wiek=" + IndexEntry.get())

    # Commit
    Connection.commit()

    # Zamknięcie połączenia z bazą danych
    Connection.close()   
    return

# Polecenie do bazy danych
#Cursor.execute("""
#    CREATE TABLE Ludzie(
#        Imie text,
#        Nazwisko text,
#        Wiek integer
#    )
#""")

# Formularz
NameLabel       =   ttk.Label(Root, text="Imię:")
SurnameLabel    =   ttk.Label(Root, text="Nazwisko:")
AgeLabel        =   ttk.Label(Root, text="Wiek:")
NameLabel.grid(row=0, column=0, sticky=tk.W)
SurnameLabel.grid(row=1, column=0, sticky=tk.W)
AgeLabel.grid(row=2, column=0, sticky=tk.W)

NameEntry       =   ttk.Entry(Root)
SurnameEntry    =   ttk.Entry(Root)
AgeEntry        =   ttk.Entry(Root)
NameEntry.grid(row=0, column=1)
SurnameEntry.grid(row=1, column=1)
AgeEntry.grid(row=2, column=1)

SubmitButton    =   ttk.Button(Root, text="Sumbit", command=Submit)
SubmitButton.grid(row=3, column=1, sticky=tk.W)

IndexLabel      =   ttk.Label(Root, text="Index")
IndexLabel.grid(row=4, column=0, sticky=tk.W)

IndexEntry      =   ttk.Entry(Root)
IndexEntry.grid(row=4, column=1)

QueryButton     =   ttk.Button(Root, text="Query", command=lambda: Query(IndexEntry.get()))
QueryButton.grid(row=5, column=1, sticky=tk.W)

DeleteButton    =   ttk.Button(Root, text="Delete", command=lambda: Delete(IndexEntry.get()))
DeleteButton.grid(row=6, column=1, sticky=tk.W)

ShowAllButton   =   ttk.Button(Root, text="Show All", command=ShowAll)
ShowAllButton.grid(row=7, column=1, sticky=tk.W)

ShowAllLabel    =   ttk.Label(Root)
ShowAllLabel.grid(row=8, column=0, columnspan=2)
ShowAllLabel["text"] = "test"

# Main loop    
Root.mainloop() 



