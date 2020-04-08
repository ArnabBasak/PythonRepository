"""
will create a dice game using tkinter
"""
from tkinter import *
from tkinter import messagebox
import random
root = Tk()
root.title("The Dice Game")
label = Label(root,text="select any value").grid(row=0,column=0)
variable = StringVar(root)
variable.set("Select")
option = OptionMenu(root,variable,"1","2","3","4","5","6")
option.grid(row=0,column=1)
def gamePlay():
    systemgenerator = [1,2,3,4,5,6]
    if variable.get() == "Select":
        messagebox.showinfo("Error","Please select a proper number")
    elif int(variable.get()) == random.choice(systemgenerator):
        messagebox.showinfo("Congratulation","You Won as system also selected "+str(random.choice(systemgenerator)))
    elif int(variable.get()) != random.choice(systemgenerator):
        messagebox.showinfo("Sorry","You lost as system selected "+str(random.choice(systemgenerator)))
play = Button(root,text="play",command=gamePlay).grid(row=1,column=1)
root.mainloop()
