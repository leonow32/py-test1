from tkinter import *
#import tkinter as tk

window = Tk() # tworzenie okna głównego
window.title( "Hello World" ) # ustawienie tytułu okna głównego
# tworzenie kontrolki typu label
label = tk.Label( window, text = "Witaj Świecie programowania\nCo swym urokiem nas zabawia\nCo otwiera nowe możliwości\nZ binarnych liczb złożoności" )
label.pack( side = tk.BOTTOM ) # podpinanie kontrolki pod okno
    
tk.mainloop() # wywołanie pętli komunikatów