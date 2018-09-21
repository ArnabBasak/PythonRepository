import nltk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import  os

MainWindow = Tk()
MainWindow.title('Gender Guessing')
MainWindow.state("zoomed")
def AddFile():
    file_path = filedialog.askopenfilename()
    if os.stat(file_path).st_size > 0:
        messagebox.showinfo("File Selected","Continue")
    else:
        messagebox.showerror("File Error","File you selected is empty")
button1 = Button(text ="Add file",command = AddFile)
button1.pack()
MainWindow.mainloop()