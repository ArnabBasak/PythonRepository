from tkinter import *
root = Tk()
root.title("Message Box")
logo = PhotoImage(file="E:\python programs\gui python\logo-200.png")
explanation = """At present,only GIF and PPM/PGM
formats are supported,but an interface
exits to allow additional image file
formats to be added easily"""
w = Label(root,compound=CENTER,text=explanation,image=logo).pack(side="top")
root.mainloop()
