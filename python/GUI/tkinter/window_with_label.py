import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Python GUI")

#win.resizable(0, 0) # this makes nonresizble our window
ttk.Label(win, text="A Label").grid(column=0, row=0)

win.mainloop()
