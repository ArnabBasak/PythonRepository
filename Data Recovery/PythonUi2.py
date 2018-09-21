import csv
from tkinter import *
from tkinter import filedialog
import os
from tkinter import messagebox
import pymysql
Mainwindow = Tk()
Mainwindow.title('File Reading')
main_label = Label(Mainwindow,text="STORE DATA RECOVERY",fg="dark green",font="Verdana 15 bold")
main_label.pack()
soa_database_label=Label(Mainwindow,text="select database",fg="dark green",font="Verdana 10")
soa_database_label.pack()
Checkbutton(Mainwindow, text="SOA",variable="soa").pack()
Checkbutton(Mainwindow, text="STORE",variable="store").pack()
Checkbutton(Mainwindow,text="PLATO",variable="plato").pack()
def SelectFile():
    file_path = filedialog.askopenfilename()
    try:
        if os.path.getsize(file_path) == 0:
            messagebox.showerror("File Error","The file you selected is empty cannot proceed with the recovery")
        else:
            connectionobject = pymysql.connect(host="localhost",user="root",password="baban123",db="test")
            #try:
            cursorobject = connectionobject.cursor()
            cursorobject.execute("""CREATE TABLE IF NOT EXISTS `CSV_TEMP`
            (
               `Database_Name` VARCHAR(50),
               `Table_Sequence_Name` VARCHAR(50),
               `Field_Name` VARCHAR(50),
               `Existing_Value` VARCHAR(50),
               `New_modified_Value` VARCHAR(50) 
            )""")
            connectionobject.commit()
            csv_file = open(file_path,'r')
            csv_data = csv.reader(csv_file)
            for row in csv_data:
                print(row)
                cursorobject.execute('INSERT INTO CSV_TEMP VALUES ("%s", "%s", "%s", %s, %s)',row)
                connectionobject.commit()
            print("done")
            cursorobject.execute("select * from csv_temp where Database_Name like "'SOA'"")
            result = cursorobject.fetchall()
            print(result)

            # except:
            #    print("error")
    except IOError:
            messagebox.showerror("File Error","Sorry cannot read the file")


Button(text = "Select File",command = SelectFile).pack()
Button(text = "Start").pack()

Mainwindow.state('zoomed')
Mainwindow.mainloop()
