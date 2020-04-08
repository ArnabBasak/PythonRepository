from tkinter import *
from tkinter import messagebox
import math
import random

root = Tk()
root.geometry("300x200")
root.resizable(0,0)
root.title("Number Guessing Game")
label = Label(root,text="Login here").grid(row=0,column=1)
label1 = Label(root,text="Username").grid(row=1,column=0)
entry1 = Entry(root)
entry1.grid(row=1,column=1)
label2 = Label(root,text="Password").grid(row=2,column=0)
entry2 = Entry(root,show="*")
entry2.grid(row=2,column=1)
def login():
    username = entry1.get()
    password = entry2.get()
    if username == "admin" and password == "admin":
        gamewindow = Toplevel(root)
        variable = StringVar(gamewindow)
        variable.set("select")
        label = Label(gamewindow,text="select any value").grid(row=0,column=0)
        option = OptionMenu(gamewindow,variable,"1","2","3","4","5","6","7","8","9","10")
        option.grid(row=0,column=1)
        def gamePlay():
            systemgenerator = [1,2,3,4,5,6,7,8,9,10]
            if variable.get() == "select":
                messagebox.showinfo("error","Please select any value")
            elif variable.get() == str(random.choice(systemgenerator)):
                messagebox.showinfo("Congratulation","You have won as system also guessed the number "+str(random.choice(systemgenerator)))
            elif variable.get() != str(random.choice(systemgenerator)):
                diff = int(variable.get()) - int(random.choice(systemgenerator))
                if diff < 0:
                    messagebox.showinfo("Sorry","You exceed by "+str(abs(diff)))
                else:
                    messagebox.showinfo("Sorry","You were behind by "+str(diff))


        playbutton = Button(gamewindow,text="submit",command=gamePlay).grid(row=1,column=1)
        gamewindow.mainloop()
    else:
        messagebox.showinfo("error","invalid input")
submit = Button(root,text="Login",command=login).grid(row=3,column=1)
root.mainloop()
