from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import pymysql
import pandas as pd
import numpy as np
from pandasql import *
from os import startfile
mainwindow = Tk()
mainwindow.title("Store Data Recovery")
main_label = Label(mainwindow,text="STORE DATA RECOVERY",fg="dark green",font="Verdana 15 bold")
main_label.pack()
soa_database_label=Label(mainwindow,text="Select the bumping file by clicking the below button\n once done it will give the result of all the data missing ",fg="dark green",font="Verdana 10")
soa_database_label.pack()
Checkbutton(mainwindow, text="SOA",variable="var1")
def printvalue():
    bumpfile = filedialog.askopenfilename()
    headers = ["Database", "Table_SequenceName","FieldName","ExistingValue","NewmodifiedValue"]
    df1=pd.read_csv(bumpfile,names = headers)
    writer = pd.ExcelWriter('E:/python programs/Data Recovery/output.xlsx')
    soavalues = "select * from df1 where Database = 'SOA'"
    soadata = sqldf(soavalues)
    if len(soadata) > 0:
        soadata.to_excel(writer,'SOA')
        writer.save()
    storevalues = "select * from df1 where Database = 'Store'"
    storedata = sqldf(storevalues)
    if len(storedata) > 0:
        storedata.to_excel(writer,'Store')
        writer.save()
    # for Plato Values
    platovalues = "select * from df1 where Database = 'Plato'"
    platodata = sqldf(platovalues)
    if len(platovalues) > 0:
        platodata.to_excel(writer,'Plato')
        writer.save()
    specsvalues = "select * from df1 where Database = 'SPECS'"
    specsdata = sqldf(specsvalues)
    if len(specsvalues) > 0:
        specsdata.to_excel(writer,'SPECS')
        writer.save()
    startfile('E:/python programs/Data Recovery/output.xlsx')
def CheckRecovery():
    outputfile = pd.ExcelFile('E:/python programs/Data Recovery/output.xlsx')
    Soadf = outputfile.parse('SOA').values
    Storedf = outputfile.parse('Store').values
    Platodf = outputfile.parse('Plato').values
    Specsdf = outputfile.parse('SPECS').values
    val1 = Soadf[0,0]
    val2 = Soadf[0,1]
    val3 = Soadf[0,2]
    val4 = Soadf[0,3]
    val5 = Soadf[0,4]
    connectionobject = pymysql.connect(host="localhost",user="root",password="baban123",db="employees")
    employeesdata = pd.read_sql("select * from %s ",(val2),con=connectionobject)
    print(employeesdata)

        
Checkbutton(mainwindow, text="STORE",variable="var2")
Button(mainwindow,text="Select the Bumping file",command = printvalue).pack()
Button(mainwindow,text="Check if recovery is possible",command=CheckRecovery).pack()
mainwindow.state("zoomed")
mainwindow.mainloop()
