import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as mBox

def clickMe():
    action.configure(text='Hello '+name.get() + ' ' + number.get())

win = tk.Tk()
win.title("Python GUI")

# We are creating a container frame to hold all other widgets # 1
monty = ttk.LabelFrame(win, text=' Monty Python ')
monty.grid(column=0, row=0)
monty.grid_configure(padx=8, pady=8)

aLabel = ttk.Label(monty, text="Enter a name:")
aLabel.grid(column=0, row=0, sticky='W')

name = tk.StringVar()
nameEntered = ttk.Entry(monty, width=12, textvariable=name)
nameEntered.grid(column=0, row=1, stick=tk.W)
nameEntered.focus()


# Creating combo cox widget
ttk.Label(monty, text="Choose a number: ").grid(column=1, row=0)
number = tk.StringVar()
numberChosen = ttk.Combobox(monty, width=12, textvariable=number)
numberChosen['values'] = (1,2,4,42,100)
numberChosen.grid(column=1, row=1)
numberChosen.current(0)

action = ttk.Button(monty, text="Click Me ! ",command=clickMe)
action.grid(column=2, row=1)


# Creating checkbuttons
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(monty, text="Disabled", variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)

chVarUn = tk.IntVar() 
check2 = tk.Checkbutton(monty, text="UnChecked", variable=chVarUn)
check2.deselect() 
check2.grid(column=1, row=4, sticky=tk.W) 

chVarEn = tk.IntVar() 
check3 = tk.Checkbutton(monty, text="Enabled", variable=chVarEn)
check3.select() 
check3.grid(column=2, row=4, sticky=tk.W) 

# Radiobutton Globals
colors = ["Blue", "Gold", "Red"]

# Radiobutton Callback 
def radCall(): 
    radSel=radVar.get()
    if radSel == 0: monty.configure(background=colors[0])
    elif radSel == 1: monty.configure(background=colors[1])
    elif radSel == 2: monty.configure(background=colors[2])

# create three Radiobuttons 
radVar = tk.IntVar() 
radVar.set(99)

for col in range(3):
    curRad = 'rad' + str(col)
    curRad = tk.Radiobutton(monty, text=colors[col], variable=radVar, value=col, command=radCall)
    curRad.grid(column=col, row=5, sticky=tk.W)


# Using a scrolled Text control 
scrolW = 30
scrolH = 3

scr = scrolledtext.ScrolledText(monty, width=scrolW, height=scrolH, wrap=tk.WORD)
scr.grid(column=0, columnspan=3)

# Create a container to hold labels
labelsFrame = ttk.LabelFrame(monty, text=' Labels in a Frame ')
labelsFrame.grid(column=0, row=7, padx=20, pady=30)
# Place labels into the container element
ttk.Label(labelsFrame, text="Label1").grid(column=0, row=0)
ttk.Label(labelsFrame, text="Label2").grid(column=0, row=1)
ttk.Label(labelsFrame, text="Label3").grid(column=0, row=2)

for child in labelsFrame.winfo_children():
    child.grid_configure(padx=8, pady=4)

# Place cursor into name Entry
nameEntered.focus()

def _quit():
    win.quit()
    win.destroy()
    exit()

def _msgBox():
    mBox.showinfo('Python Message Info Box', 'A Python GUI created using tkinter:\nThe year is 2020.')

# Create Menu
menuBar = Menu(win)
win.config(menu=menuBar)

fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="New")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=_quit)
menuBar.add_cascade(label="File", menu=fileMenu)

helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="About", command=_msgBox)
menuBar.add_cascade(label="Help", menu=helpMenu)

win.mainloop()

