from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os
import subprocess
Mainwindow = Tk()
Mainwindow.title('Sanity Checks')
Mainwindow.configure(background='green')
main_label = Label(Mainwindow,text="SANITY TEST FOR PILOT STORES",fg="white",font="Timesnewroman 15 bold")
main_label.configure(background='green')
main_label.pack(fill=X,pady=5)
text_label=Label(Mainwindow,text="Enter IP for the stores",fg="white",font="Timesnewroman 10 bold")
text_label.configure(background = 'green')
text_label.pack()
Mytext = Text(Mainwindow,width=30,height=5)
Mytext.pack(pady=10)
#e.focus_set()
def callback():
    #print (e.get())
    content = Mytext.get("1.0","end-1c")
    if len(content) <= 2:
        messagebox.showerror('data info','please enter the IP properly')
    else:
        inputfile = open("/home/arnab/Desktop/inputfile.txt",'w')
        inputfile.write(content)
        inputfile.close()
        """ executing the shell script make sure that this python script and the shell script is in same folder"""
        subprocess.call(['bash','test.sh'])
        """reading the output file this should also be in the same location as the input file and the python script"""
        outputfile = open("/home/arnab/Desktop/python_programs/output.txt",'r')
        outputmatter = outputfile.read()
        messagebox.showinfo("output",outputmatter)
Main_Button = Button(Mainwindow,text="Start",fg="green",font="calibari 10 bold", command=callback)
Main_Button.configure(background = "white")
Main_Button.pack()
w, h = Mainwindow.winfo_screenwidth(), Mainwindow.winfo_screenheight()
Mainwindow.geometry("%dx%d+0+0" % (w, h))
Mainwindow.mainloop()

