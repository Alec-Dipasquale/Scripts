import tkinter as tk 
from tkinter import filedialog, Text, ttk
import os

root = tk.Tk()
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]

def addApp():
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir = "/", title="Select File",
                                            filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    for app in apps:
        label = tk.Label(frame, text = app, bg = "gray")
        label.pack()


def runApps():
    for app in apps:
        os.startfile(app)

def saveFile():
    popup = tk.Tk()
    popup.wm_title("Save File")
    popCanvas = tk.Canvas(popup, height = 150, width = 200)
    
    ttk.Label(popup, text="File Name: ").grid(row=0)

    entry = tk.Entry(popup)
    entry.grid(row=0, column = 1)
    popCanvas.pack()

    saveButton = ttk.Button(popup, text= "Save", command = saveFile)
    saveButton.pack()
    popup.mainloop()

canvas = tk.Canvas(root, height = 700, width = 700, bg = "#8B8B00")
canvas.pack()

frame = tk.Frame(root, bg = "white" )
frame.place(relwidth = 0.8, relheight = 0.8, relx = 0.1 , rely = 0.1)

openFile = tk.Button(root, text = "Open File", padx=10,
                    pady=5, fg="white", bg = "#8B8B00", command=addApp)
openFile.pack()

saveFileList = tk.Button(root, text = "Save App Setup", padx=10,
                    pady=5, fg="white", bg = "#8B8B00", command=saveFile)
saveFileList.pack()

openFile = tk.Button(root, text = "Open File", padx=10,
                    pady=5, fg="white", bg = "#8B8B00", command=addApp)
openFile.pack()

runnApps = tk.Button(root, text = "Run Apps", padx=10,
                    pady=5, fg="white", bg = "#8B8B00", command = runApps)
runnApps.pack()

for app in apps:
    label = tk.Label(frame, text = app)
    label.pack()

root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')

