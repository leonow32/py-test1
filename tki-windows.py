import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk

# Zmienne globalne
Root = tk.Tk()

# Etykieta do wyświetlania wyników
Res = tk.StringVar()
Res.set("Tu beda wyniki")
ResLabel = tk.Label(Root, textvariable=Res)
ResLabel.pack()

# Info Box
def Info():
    Result = messagebox.showinfo("First popup", "info message")
    Res.set(Result)

tk.Button(Root, text="Info", command=Info).pack()

# Waring Box
def Warning():
    Result = messagebox.showwarning("First popup", "info message")
    Res.set(Result)

tk.Button(Root, text="Warning", command=Warning).pack()

# Error Box
def Error():
    Result = messagebox.showerror("First popup", "info message")
    Res.set(Result)

tk.Button(Root, text="Error", command=Error).pack()

# Question Box
def Question():
    Result = messagebox.askquestion("First popup", "pytanie?")
    Res.set(Result)

tk.Button(Root, text="Question", command=Question).pack()

# Ok/Cancel Box
def OkCancel():
    Result = messagebox.askokcancel("First popup", "pytanie?")
    Res.set(Result)

tk.Button(Root, text="OK Cancel", command=OkCancel).pack()

# Retry/Cancel Box
def RetryCancel():
    Result = messagebox.askretrycancel("First popup", "pytanie?")
    Res.set(Result)

tk.Button(Root, text="Retry Cancel", command=RetryCancel).pack()

# Yes/No Box
def YesNo():
    Result = messagebox.askyesno("First popup", "pytanie?")
    Res.set(Result)

tk.Button(Root, text="Yes No", command=YesNo).pack()

# Yes/No/Cancel Box
def YesNoCancel():
    Result = messagebox.askyesnocancel("First popup", "pytanie?")
    Res.set(Result)

tk.Button(Root, text="Yes No Cancel", command=YesNoCancel).pack()

# New Windows
def NewWindow():
    
    def WindowSaveText():
        Res.set("Label1 = " + TextBox.get())

    Window = tk.Toplevel()
    Window.iconbitmap("atom128.ico")
    Window.title("Pop up window")
    tk.Label(Window, text="Input something:").pack()
    TextBox = tk.Entry(Window)
    TextBox.pack()
    Button = tk.Button(Window, text="Save", command=WindowSaveText).pack()
    Quit = tk.Button(Window, text="Exit", command=Window.destroy).pack()

tk.Button(Root, text="New windows", command=NewWindow).pack()

# Open file
def OpenFile():
    Result = filedialog.askopenfilename(initialdir="/images", title="Wybierz plik", filetypes=(("Pliki PNG","*.png"),("Wszystkie pliki","*.*")))
    Res.set(Result)

tk.Button(Root, text="Open File", command=OpenFile).pack()

# Open image
def OpenImage():
    Result = filedialog.askopenfilename(initialdir="/images", title="Wybierz plik", filetypes=(("Pliki PNG","*.png"),("Wszystkie pliki","*.*")))
    Res.set(Result)
    Window = tk.Toplevel()
    Window.title("Image")
    global Obrazek
    Obrazek = ImageTk.PhotoImage(Image.open(Result))
    Foto = tk.Label(Window, image=Obrazek)
    Foto.pack()

tk.Button(Root, text="Open Image", command=OpenImage).pack()

# Main loop    
Root.title("Image viewer")
Root.iconbitmap("atom128.ico")
Root.mainloop() 



