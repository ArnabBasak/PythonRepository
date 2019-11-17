from tkinter import *
root = Tk()
message = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"
msg = Message(root,text=message)
msg.config(bg='lightgreen', font=('times', 24, 'italic'))
msg.pack(fill=X)
root.mainloop()
