from tkinter import *
from tkinter import messagebox
top = Tk()
def fun():
    messagebox.showinfo("Message","Hello all")

b1 = Button(top,text="Click Me",command=fun)
b1.pack(side=LEFT)
top.mainloop()
