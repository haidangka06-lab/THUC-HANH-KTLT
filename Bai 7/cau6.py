from tkinter import *
def NewFile():
    print("New File!")
def OpenFile():
    print("Open File!")
def Exit():
    print("Exit the program!")
def InsText():
    print("Insert Text!")
def InsPic():
    print("Insert Picture!")
def About():
    print("This is a menu demo program")
root = Tk()
root.title("Menu Example")
root.geometry("400x200")
menu = Menu(root)
root.config(menu=menu)
# ---------- FILE MENU ----------
filemenu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=Exit)
# ---------- INSERT MENU ----------
insertmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Insert", menu=insertmenu)
insertmenu.add_command(label="Insert Text", command=InsText)
insertmenu.add_command(label="Insert Picture", command=InsPic)
# ---------- HELP MENU ----------
helpmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About", command=About)
root.mainloop()

