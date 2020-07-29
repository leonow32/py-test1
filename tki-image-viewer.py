import tkinter as tk
from PIL import Image
from PIL import ImageTk

# Zmienne globalne
Root = tk.Tk()
ActualImageNumber = 0
ImageList = []
Text1 = tk.StringVar(Root)
StatusBarText = tk.StringVar(Root)

# Zmiana obrazka
def ChangeImage(NewImageNumber):
    print("ChangeImage(" + str(NewImageNumber) + ")")
    
    # Kontrola poprawności
    if NewImageNumber < 0:
        print("<0")
        return

    if NewImageNumber >= len(ImageList):
        print(">=len(ImageList)=" + str(len(ImageList)))
        return
    
    # Zmiana obrazka
    global ActualImageNumber
    global ImageLabel
    ImageLabel.grid_forget()
    ImageLabel = tk.Label(image=ImageList[NewImageNumber])
    ImageLabel.grid(row=0, column=0, columnspan=3)
    ActualImageNumber = NewImageNumber

    # Włączanie/wyłączanie przycisków przewijania
    if(ActualImageNumber == len(ImageList)-1):
        ButtonNext.config(state=tk.DISABLED)
    else:
        ButtonNext.config(state=tk.ACTIVE)
    
    if(ActualImageNumber == 0):
        ButtonPrev.config(state=tk.DISABLED)
    else:
        ButtonPrev.config(state=tk.ACTIVE)

    # Aktualizacja statusu
    global StatusBarText
    StatusBarText.set("Image {} / {}".format(ActualImageNumber+1, len(ImageList)))

# Okna główne
Root.title("Image viewer")
Root.iconbitmap("atom128.ico")

# Obrazki
#Image0 = ImageTk.PhotoImage(Image.open("images/0.png"))
#Image1 = ImageTk.PhotoImage(Image.open("images/1.png"))
#Image2 = ImageTk.PhotoImage(Image.open("images/2.png"))
#Image3 = ImageTk.PhotoImage(Image.open("images/3.png"))
#Image4 = ImageTk.PhotoImage(Image.open("images/4.png"))

# Lista obrazków - wersja 1
#ImageList = [Image0, Image1, Image2, Image3, Image4]

# Lista obrazków - wersja 2
#ImageList.append(Image0)
#ImageList.append(Image1)
#ImageList.append(Image2)
#ImageList.append(Image3)
#ImageList.append(Image4)

# Lista obrazków - wersja 3
#ImageList += [Image0]
#ImageList += [Image1]
#ImageList += [Image2]
#ImageList += [Image3]
#ImageList += [Image4]

for i in range(5):
    print(i)
    ImageList.append(ImageTk.PhotoImage(Image.open("images/" + str(i) + ".png")))

# Umieszczenie pierwszego obrazka
ImageLabel = tk.Label(image=ImageList[0])
ImageLabel.grid(row=0, column=0, columnspan=3)

# Tekst w pasku stanu
StatusBarText.set("Image 1 / " + str(len(ImageList)))

# Przyciski
ButtonExit = tk.Button(Root, text="Exit", command=Root.quit)
ButtonNext = tk.Button(Root, text=">", command=lambda: ChangeImage(ActualImageNumber+1))
ButtonPrev = tk.Button(Root, text="<", command=lambda: ChangeImage(ActualImageNumber-1), state=tk.DISABLED)
ButtonPrev.grid(row=1, column=0)
ButtonExit.grid(row=1, column=1)
ButtonNext.grid(row=1, column=2)

# Status bar
StatusBar = tk.Label(Root, textvariable=StatusBarText, bd=1, relief=tk.SUNKEN, anchor=tk.E)
StatusBar.grid(row=2, column=0, columnspan=3, sticky=tk.W+tk.E)

# Main loop    
Root.mainloop() 

