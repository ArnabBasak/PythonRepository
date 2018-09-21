from tkinter import *
import pymysql
from tkinter import messagebox
top = Tk()
top.title('DataBase Interface')
L1 = Label(text="First Name")
L1.place(x=10,y=10)
L1.pack()
E1 = Entry(bd = 5)
E1.pack()
L2 = Label(text = "Last Name")
L2.place(x=10,y=500)
L2.pack()
E2 = Entry(bd = 5)

E2.pack()
def getcontent():
    E1content = E1.get()
    E2content = E2.get()
    if len(E1content) == 0 or len(E2content) == 0:
         messagebox.showinfo("User Input","please fill the data properly")
    else:
        db_conn = pymysql.connect(host = "localhost",user = "root",password = "library",db = "student")
        cursor_s = db_conn.cursor()
        cursor_s.execute("insert into studentname(firstname,lastname) values(%s,%s)",(E1content,E2content))
        db_conn.commit()
        messagebox.showinfo("User Input","data inserted sucessfully")
        #print(E1content)
        #print(E2content)
B = Button(text = "Submit",command = getcontent)
B.pack()
top.state("zoomed")
top.mainloop()