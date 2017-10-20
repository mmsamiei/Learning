import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Python GUI")

#win.resizable(0, 0) # this makes nonresizble our window
aLabel = ttk.Label(win, text="A Label")
aLabel.grid(column=0, row=0)

def clickMe():
    action.configure(text="** I have been CLicked! **")
    aLabel.configure(foreground='red')

# Adding a Button
action = ttk.Button(win, text="Click Me!", command=clickMe)
action.grid(column=1, row=0)


win.mainloop()
