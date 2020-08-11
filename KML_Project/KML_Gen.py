import sys
import codecs
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as mBox
from tkinter import filedialog
from os import path
import makeKML

logFileList = None

def TexttoLower(text):
    return text.lower()

def getLogFiles():
    global logFileList
    fDir = path.dirname(__file__)
    logFiles = filedialog.askopenfilenames(parent=win, initialdir=fDir)
    logFileList = list(logFiles)
    logFileList.sort(reverse=True)
    openFilesListbox.config(state='normal')
    openFilesListbox.delete(1.0, tk.END)
    for logfile in logFiles:
        openFilesListbox.insert(tk.CURRENT, logfile+'\n')
    openFilesListbox.config(state='disabled')
    saveFileEditbox.config(state='normal')
    saveFileEditbox.insert(tk.INSERT, logFiles[0]+".kml")
    saveFileEditbox.config(state='disabled')

def makeKMLFile():
    global logFileList

    KMLFilepath = saveFileEditbox.get()
    KMLFilename = KMLFilepath[KMLFilepath.rfind('/')+1:]
    
    kml_file = open(KMLFilepath,'wt', encoding='UTF8')
    
    makeKML.make_kml_header(kml_file, KMLFilename)

    makeKML.open_Position_folder(kml_file)
    if chVarAOSP.get() == 1:
        makeKML.open_AOSP_folder(kml_file)
        for currentLogFile in logFileList:
            log_file = open(currentLogFile, 'rt', encoding='cp949', errors='ignore')
            logFileName = currentLogFile[currentLogFile.rfind('/')+1:]
            log_lines = log_file.readlines()
            makeKML.add_AOSP_location(log_lines, logFileName, kml_file)
            log_file.close()
        makeKML.close_AOSP_folder(kml_file)

    if chVarMMF.get() == 1:
        makeKML.open_MMF_folder(kml_file)
        for currentLogFile in logFileList:
            log_file = open(currentLogFile, 'rt', encoding='cp949', errors='ignore')
            log_lines = log_file.readlines()
            makeKML.add_MMF_location(log_lines, kml_file)
            log_file.close()
        makeKML.close_MMF_folder(kml_file)
    makeKML.close_Position_folder(kml_file)

    if chVarTrack.get() == 1:
        makeKML.open_Track_folder(kml_file)
        for currentLogFile in logFileList:
            log_file = open(currentLogFile, 'rt', encoding='cp949', errors='ignore')
            log_lines = log_file.readlines()
            makeKML.add_track_for_AOSP(log_lines, kml_file)
            log_file.close()
        makeKML.close_Track_folder(kml_file)

    makeKML.make_kml_tail(kml_file)

    mBox.showinfo('KML Generator', 'KML File (' + KMLFilename + ') is generated successfully...')

win = tk.Tk()
win.title("KML Generator (Ver. 0.1)")
win.resizable(0, 0)

## Upper Frame for selection items
itemChooseFrame = ttk.LabelFrame(win, text=' Select Items ')
itemChooseFrame.grid(column=0, row=0, sticky='WE')
itemChooseFrame.grid_configure(ipadx=5, ipady=5, padx=10, pady=10)

chVarAOSP = tk.IntVar() 
chgckAOSP = tk.Checkbutton(itemChooseFrame, text="AOSP Location", variable=chVarAOSP)
chgckAOSP.select() 
chgckAOSP.grid(column=0, row=1, sticky=tk.W) 
chgckAOSP.grid_configure(padx=20)

chVarMMF = tk.IntVar() 
chgckMMF = tk.Checkbutton(itemChooseFrame, text="MMF Location", variable=chVarMMF)
chgckMMF.select() 
chgckMMF.grid(column=1, row=1, sticky=tk.W) 
chgckMMF.grid_configure(padx=30)

chVarTrack = tk.IntVar() 
chgckTrack = tk.Checkbutton(itemChooseFrame, text="Track ", variable=chVarTrack)
chgckTrack.select() 
chgckTrack.grid(column=2, row=1, sticky=tk.W) 
chgckTrack.grid_configure(padx=40)

## Lower Frame for Input/Output Files
fileSelectionFrame = ttk.LabelFrame(win, text=' Select Files ')
fileSelectionFrame.grid(column=0, row=1, sticky='WE', padx=10, pady=10, ipadx=5, ipady=5)

openFilesBtn = ttk.Button(fileSelectionFrame, text='Open Log File', command=getLogFiles)
openFilesBtn.grid(column=2, row=1, sticky=tk.W, pady=10)

scrolW = 50
scrolH = 5
openFilesListbox = scrolledtext.ScrolledText(fileSelectionFrame, width=scrolW, height=scrolH, wrap=tk.WORD, state='disabled')
openFilesListbox.grid(column=0, row=1, columnspan=2, padx=5, pady=15)

aLabel = ttk.Label(fileSelectionFrame, text="  Output KML Filename")
aLabel.grid(column=0, row=2, sticky='W')

saveFileBtn = ttk.Button(fileSelectionFrame, text='Make KML File', command=makeKMLFile)
saveFileBtn.grid(column=2, row=3, sticky=tk.W)

saveFilename = tk.StringVar
saveFileEditbox = ttk.Entry(fileSelectionFrame, width=50, textvariable=saveFilename, state='disabled')
saveFileEditbox.grid(column=0, row=3, sticky='WE', padx=5)

win.mainloop()