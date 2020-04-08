from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("200x200")

def run():
    messagebox.showinfo("information","This button got clicked")
def open():
    top = Toplevel(root)
    topbtn = Button(top,text="Click Me",command=run).grid(row=0,column=0)
    top.mainloop()

btn = Button(root,text="Click",command=open).grid(column=0,row=0)
root.mainloop()
