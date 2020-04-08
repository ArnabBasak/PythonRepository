from tkinter import *
from tkinter import messagebox
import pickle
root = Tk()
root.title('Runs Prediction')
root.geometry('500x100')
root.resizable(0,0)
selectlabel = Label(root,text='Select a player name',font='segoe 13 bold').grid(row=0,column=0)
variable = StringVar(root)
variable.set("select")
playeroption = OptionMenu(root,variable,"Virat Kohli","Rohit Sharma","Kane Williamson","Steve Smith")
playeroption.grid(row=0,column=1)
def predict():
    if variable.get() == "select":
        messagebox.showinfo("Error",'Please select a player name')
    elif variable.get() == "Virat Kohli":
        with open('Virat_Model','rb') as f:
            vp = pickle.load(f)
        match = vp.predict(18246)
        messagebox.showinfo("Answer","Virat will break sachin's ODI runs record of 18246 runs in his "+str(int(match))+" ODI match")
    elif variable.get() == "Rohit Sharma":
        with open('rohit_model','rb') as f:
            rmodel = pickle.load(f)
        rmatch = rmodel.predict(18246)
        messagebox.showinfo("Answer","Rohit will break sachin's ODI record of 18246 runs in his "+str(int(rmatch))+" ODI match")
    elif variable.get() == "Kane Williamson":
        with open('kane_model','rb') as f:
            kanep = pickle.load(f)
        kmatch = kanep.predict(18246)
        messagebox.showinfo("Answer","Kane Williamson will break sachin's ODI runs record of 18246 runs in his "+str(int(kmatch))+" ODI match")
    elif variable.get() == "Steve Smith":
        with open('steve_model','rb') as f:
            smodel = pickle.load(f)
        smatch = smodel.predict(18246)
        messagebox.showinfo("Answer","Steve Smith will break sachin's ODI runs record of 18246 runs in his "+str(int(smatch))+" ODI match")
predictButton = Button(root,text="Predict",command=predict,font = "Segoe 13 bold").grid(row=1,column=1)
root.mainloop()
