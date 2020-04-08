from tkinter import messagebox
from tkinter import *
import datetime

root = Tk()
root.title("Age Calculator")
label = Label(root,text="Age Calculator").grid(row=0,column=1)
namelabel = Label(root,text="Enter your name").grid(row=1,column=0)
nameentry = Entry(root)
nameentry.grid(row=1,column=1)
agelabel = Label(root,text="Enter your full Birth year").grid(row=2,column=0)
ageentry = Entry(root)
ageentry.grid(row=2,column=1)
def calculateage():
    name = nameentry.get()
    if len(ageentry.get()) < 4:
        messagebox.showinfo("Error","Please enter year in 4 digits")
    try:
        age = int(ageentry.get())
    except ValueError:
        messagebox.showinfo("Error","Please enter an numbers")
    if len(name) == 0 and len(age) == 0:
        messagebox.showinfo("Error","Please enter the values properly")
    elif len(str(age)) < 4:
        messagebox.showinfo("Error","Please enter the year in 4 digit")
    else:
        birthcentenary = age + 100
        if datetime.datetime.now().hour < 12:
            messagebox.showinfo("Good morning",name+"You will complete birth birthcentenary in the year "+str(birthcentenary))
        elif datetime.datetime.now().hour ==12:
            messagebox.showinfo("Good Afternoon",name+"You will complete birth birthcentenary in the year "+str(birthcentenary))
        elif datetime.datetime.now().hour > 12:
            messagebox.showinfo("Good Evening",name+"You will complete birth birthcentenary in the year "+str(birthcentenary))


calculate = Button(root,text="Calculate",command=calculateage).grid(row=3,column=1)
root.mainloop()
