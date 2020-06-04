import tkinter as tk # imports
from tkinter import ttk

win = tk.Tk() # Create instance
win.title("Python GUI") # Add a title
tabControl = ttk.Notebook(win) # Create Tab Control

tab1 = ttk.Frame(tabControl) # Create a tab
tabControl.add(tab1, text='Tab 1') # Add the tab
tabControl.pack(expand=1, fill="both") # Pack to make visible

tab2 = ttk.Frame(tabControl) # Add a second tab
tabControl.add(tab2, text='Tab 2') # Make second tab visible

monty = ttk.LabelFrame(tab1, text=' Monty Python ')
monty.grid(column=0, row=0, padx=8, pady=4)
ttk.Label(monty, text="Enter a name:").grid(column=0, row=0, sticky='W')

monty2 = ttk.LabelFrame(tab2, text=' The Snake ')
monty2.grid(column=0, row=0, padx=8, pady=4)
ttk.Label(monty2, text="Enter a name:").grid(column=0, row=0, sticky='W')

chVarDis = tk.IntVar()
check1 = tk.Checkbutton(monty2, text="Disabled", variable=chVarDis, state='disabled')

win.mainloop() # Start GUI