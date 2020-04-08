from tkinter import *
from tkinter import messagebox
import datetime
root = Tk()
root.title("Simple Form")
label1 = Label(root,text="Name").grid(row=0,column=0)
entry1 = Entry(root)
entry1.grid(row=0,column=1)
def output():
    if datetime.datetime.now().hour < 12:
        messagebox.showinfo("Message","Good Morning "+entry1.get())
    elif datetime.datetime.now().hour >= 12 and datetime.datetime.now().hour < 15:
        messagebox.showinfo("Message","Good Afternoon "+entry1.get())
    elif datetime.datetime.now().hour > 15:
        messagebox.showinfo("Message","Good Evening "+entry1.get())
submit = Button(root,text="submit",command=output).grid(row=1,column=1)
root.mainloop()
