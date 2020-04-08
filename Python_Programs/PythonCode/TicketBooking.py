"""
An Amusement park company wants one application for
theirbilling counter to enable ticketsale.
Assume the Amusement park authorities approached Max to get this application developed.
This application should haveticket prize asRs400 per person and
if a person buys more than 10 tickets then personiseligiblefor 10 percent discount.
Calculatethe total bill or amount according to the number of tickets that are sold.

"""
from tkinter import *
from tkinter import messagebox
import datetime
root = Tk()
root.title('Ticket Booking')
root.geometry("400x200")
root.resizable(0,0)
label = Label(root,text="How many tickets do you want?").grid(row=0,column=1)
userinput = Entry(root)
userinput.grid(row = 0,column=2,ipady=10)
def calculate():
        ticketvalue =  userinput.get()
        if len(ticketvalue) == 0:
            messagebox.showinfo("Warning","Please insert proper ticket value")
        elif int(ticketvalue) <= 10:
            messagebox.showinfo("Total","Total Bill is: "+str(int(ticketvalue)*400))
        elif int(ticketvalue) > 10:
            messagebox.showinfo("Total","Total Bill is: "+str(int(int(ticketvalue)*400)-(400*0.1)))
calButton = Button(root,text="calculate",command=calculate).grid(row=1,column=2)
root.mainloop()

# class TicketBooking:
#     def TicketBooking(self):
#         self.numberoftickets = int(input('How many tickets do you want'))
#         if self.numberoftickets > 10:
#             print("You have to pay",self.numberoftickets * 400-(400*0.1))
#         else:
#             print("You have to pay",self.numberoftickets * 400)
#TB = TicketBooking()
#TB.TicketBooking()
