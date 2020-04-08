from  tkinter import *
from tkinter import messagebox
import pymysql
import datetime
root = Tk()
root.title('Ticket Booking')
root.geometry("300x100")
usernamelabel = Label(root,text="username").grid(row=0,column=0)
usertext = Entry(root)
usertext.grid(row=0,column=1)
passwordlabel = Label(root,text="password").grid(row=1,column=0)
passwordtext = Entry(root,show="*")
passwordtext.grid(row=1,column=1)
def login():
    username = usertext.get()
    password = passwordtext.get()
    if len(username) <= 0 and len(password) <=0:
        messagebox.showinfo("Error","Invalid credentials")
    else:
        db = pymysql.connect(host="localhost",user="root",password="library",db="ticket_booking")
        cursor = db.cursor()
        cursor.execute("select * from user")
        results = cursor.fetchall()
        for row in results:
            name = row[0]
            pwd = row[1]
            if name == username and pwd == password:
                #messagebox.showinfo("Info",'congratulations')
                root.minsize()
                ticket_booking = Toplevel(root)
                ticket_booking.title("book tickets")
                ticket_booking.geometry("500x500")
                now = datetime.datetime.now().hour
                if now < 8:
                    cursor = db.cursor()
                    cursor.execute("insert into tickets_booking values ")
                elif now < 12:
                    greeting = Label(ticket_booking,text="Good Morning").grid(row=0,column=0)
                elif now > 12:
                    greeting = Label(ticket_booking,text="Good Evening").grid(row=0,column=0)
                ticket_booking.mainloop()
            else:
                messagebox.showinfo("Error","Invalid Credentials")

login = Button(root,text="Login",command=login).grid(row=2,column=1)
root.mainloop()
