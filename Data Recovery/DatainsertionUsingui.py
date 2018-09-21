from tkinter import *
import pymysql
from tkinter import messagebox
window = Tk()
window_label = Label(window,text = "firstname")
window_label.place(x=10,y=10)
window_label.pack()
window_text = Entry(window,bd = 5)
window_text.pack()
window_label1 = Label(window,text = "lastname")
window_label1.place(x=10,y=500)
window_label1.pack()
window_text1 = Entry(window,bd = 5)
window_text1.pack()
def insertdata():
    firstname = window_text.get()
    lastname = window_text1.get()
    if len(firstname) == 0 or len(lastname) == 0:
        messagebox.showerror("ERROR","fill the data properly")
    else:
        connsql= pymysql.connect(host="localhost", user="root", password="baban123", db="test")
        cursur = connsql.cursor()
        cursur.execute("insert into student (firstname,lastname) values(%s,%s)",(firstname,lastname))
        connsql.commit()
        messagebox.showinfo("user info","data inserted successfully")
window_button = Button(window,text ="Submit",command = insertdata)
window_button.pack()
window.mainloop()
