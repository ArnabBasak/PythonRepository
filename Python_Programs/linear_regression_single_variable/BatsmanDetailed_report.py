from tkinter import *
from tkinter import messagebox
import pickle
import pandas as pd
import numpy as np
root = Tk()
root.geometry('500x100')
root.title("Detailed Report")
root.resizable(0,0)
selectlabel = Label(root,text='Select a player name',font='segoe 13 bold').grid(row=0,column=0)
variable = StringVar(root)
variable.set("select")
playeroption = OptionMenu(root,variable,"Virat Kohli","Rohit Sharma","Kane Williamson","Steve Smith")
playeroption.grid(row=0,column=1)
labelvariable = StringVar(root)
def Check():
    if variable.get() == "select":
        messagebox.showinfo("Error","Please select a value")
    elif variable.get() == "Virat Kohli":
        vdata = pd.read_csv('viratODI.csv',sep="\t")
        matches = vdata['Matches'].count()
        runs = vdata['Runs'].max()
        with open('Virat_Model','rb') as f:
            vp = pickle.load(f)
        vrecord = vp.predict(18246)
        vrecord = int(vrecord) - int(matches)
        messagebox.showinfo("Virat_Facts",'Virat played: \t'+str(matches)+" ODI matches""\n"+'and scored:\t'+str(runs)+" runs till now""\n"+"Virat requires: "+str(int(vrecord))+" more matches to break the record of sachin tendulkar's maximum ODI runs")
    elif variable.get() == "Rohit Sharma":
        rdata = pd.read_csv('rohit.csv',sep="\t")
        matches = rdata['Matches'].count()
        runs = rdata['Runs'].max()
        with open('rohit_model','rb') as f:
            rp = pickle.load(f)
        rrecord = rp.predict(18246)
        rrecord = int(rrecord) - int(matches)
        messagebox.showinfo("Rohit_Facts",'Rohit played: \t'+str(matches)+" ODI matches""\n"+'and scored:\t'+str(runs)+" runs till now""\n"+"Rohit requires: "+str(int(rrecord))+" more matches to break the record of sachin tendulkar's maximum ODI runs")
    elif variable.get() == "Kane Williamson":
        kdata = pd.read_csv('Kane.csv',sep="\t")
        matches = kdata['Matches'].count()
        runs = kdata['Aggr'].max()
        with open('kane_model','rb') as f:
            kp = pickle.load(f)
        krecord = kp.predict(18246)
        krecord = int(krecord) - int(matches)
        messagebox.showinfo("Kane_Facts",'Kane played: \t'+str(matches)+" ODI matches""\n"+'and scored:\t'+str(runs)+" runs till now""\n"+"Kane requires: "+str(int(krecord))+" more matches to break the record of sachin tendulkar's maximum ODI runs")
    elif variable.get() == "Steve Smith":
        sdata = pd.read_csv('steve.csv',sep="\t")
        matches = sdata['Matches'].count()
        runs = sdata['Runs'].max()
        with open('steve_model','rb') as f:
            sp = pickle.load(f)
        srecord = sp.predict(18246)
        srecord = int(srecord) - int(matches)
        messagebox.showinfo("Steve_Facts",'Steve played: \t'+str(matches)+" ODI matches""\n"+'and scored:\t'+str(runs)+" runs till now""\n"+"Steve requires: "+str(int(srecord))+" more matches to break the record of sachin tendulkar's maximum ODI runs")
button = Button(root,text="submit",command=Check).grid(row=2,column=1)
root.mainloop()
