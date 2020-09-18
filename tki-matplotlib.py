# Test MatPlotLib
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt

# Zmienne globalne
Root = tk.Tk()

def Graph():
    Price = np.random.normal(200000, 25000, 500)
    plt.hist(Price, 100)
    plt.show()

# Przycisk
Button = ttk.Button(Root, text="Graph", command=Graph)
Button.pack()

# Main loop    
Root.title("Testy MatPlotLib")
Root.geometry("500x500")
Root.mainloop() 
