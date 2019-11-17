import tkinter as tk
root = tk.Tk()
root.title("Buttons example")
button = tk.Button(root,text='Click me',command=root.destroy)
button.pack()
root.mainloop()
