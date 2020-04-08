"""
In this file we will try to automate the high level analysis of the store data recovery
using python
"""

import pandas as pd #importing this library for reading and storeing in data frame
import numpy as np #for calculation on the data
from tkinter import * #For UI creation
from tkinter import messagebox #to generate messages in the UI
import pymysql #to import data from mysql database
from sqlalchemy import create_engine #for ORM to import the data
import datetime #for filtering the data on basis of date and time
from datetime import datetime as dt # to remove the timestamps from the date
class dataRecovery:
    def connection(self):
        """This funtion will create a connection and fetch the data from all the necessary tables in mysql"""
        try:
            self.engine = create_engine('mysql+pymysql://root:library@localhost:3306/soa')
            self.customer_data = pd.read_sql_query('SELECT * FROM customer', self.engine)
            self.record_data = pd.read_sql_query('SELECT * FROM record', self.engine)
            self.scheme_data = pd.read_sql_query('SELECT * FROM customer_contact_lens_scheme', self.engine)
            self.salesHeader_data = pd.read_sql_query('SELECT * FROM sales_header', self.engine)
            self.ClinicalDispense_data = pd.read_sql_query('SELECT * FROM clinical_dispense_order', self.engine)
            self.DispenseItem_data = pd.read_sql_query('SELECT * FROM dispense_item', self.engine)
            self.NHSVoucer_data = pd.read_sql_query('SELECT * FROM nhsvoucher', self.engine)
        except:
            messagebox.showerror("error","something wrong with the connection")
    def userInterface(self):
        """This funtion will create the necessary UI needed for the application """
        mainwindow = Tk()
        mainwindow.geometry('300x200')
        mainwindow.title('Store Data recovery')
        mainwindow.resizable(0,0)
        self.userlabel = Label(mainwindow,text='username').grid(row=0,column=0)
        self.usertext = Entry(mainwindow)
        self.usertext.grid(row=0,column=1)
        self.passlabel = Label(mainwindow,text="Password").grid(row=1,column=0)
        self.passtext = Entry(mainwindow,show="*")
        self.passtext.grid(row=1,column=1)
        def login():
            """This funtion will login into the application and a new window will open"""
            self.username = self.usertext.get()
            self.password = self.passtext.get()
            if self.username == 'admin' and self.password == 'admin':
                mainwindow.wm_iconify()
                commandwindow = Toplevel(mainwindow)
                commandwindow.title('Data Recovery')
                commandwindow.geometry("700x500")
                commandwindow.resizable(0,0)
                date1label = Label(commandwindow,text="Enter the from Date").grid(row=0,column=0)
                date1Entry = Entry(commandwindow)
                date1Entry.grid(row=0,column=1)
                date2label = Label(commandwindow,text="Enter the to Date").grid(row=0,column=2)
                date2Entry = Entry(commandwindow)
                date2Entry.grid(row=0,column=3)
                days_text = StringVar(mainwindow)
                display_days = Label(commandwindow,textvariable=days_text).grid(row=1,columnspan=3)
                customer_text = StringVar(mainwindow)
                display_customer = Label(commandwindow,textvariable=customer_text).grid(row=2,columnspan=3)
                record_text = StringVar(mainwindow)
                display_record = Label(commandwindow,textvariable=record_text).grid(row=3,columnspan=3)
                scheme_text = StringVar(mainwindow)
                display_scheme = Label(commandwindow,textvariable=scheme_text).grid(row=4,columnspan=3)
                salesheader_text = StringVar(mainwindow)
                salesheader_display = Label(commandwindow,textvariable=salesheader_text).grid(row=5,columnspan=3)
                clinicaldispense_text = StringVar(mainwindow)
                clinicaldispense_display = Label(commandwindow,textvariable=clinicaldispense_text).grid(row=6,columnspan=3)
                dispense_item_text = StringVar(mainwindow)
                dispense_item_display = Label(commandwindow,textvariable=dispense_item_text).grid(row=7,columnspan=3)
                nhsvoucher_text = StringVar(commandwindow)
                nhsvoucher_display = Label(commandwindow,textvariable=nhsvoucher_text).grid(row=8,columnspan=3)
                sales_detail_text = StringVar(mainwindow)
                sales_detail_display = Label(commandwindow,textvariable=sales_detail_text).grid(row=9,columnspan=3)
                def HighLevelAnalysis():
                    date1 = date1Entry.get()
                    date2 = date2Entry.get()
                    try:
                        d1 = datetime.datetime.strptime(date1,"%Y-%m-%d") #This will check if the inputed date is in correct format
                        d2 = datetime.datetime.strptime(date2,"%Y-%m-%d")
                        days_dataloss = abs((d2-d1).days) #this is calculating the number of data loss happened
                        days_text.set("Total day(s) of data loss is: "+str(days_dataloss))
                        self.connection() #This is calling the above funtion if all the dates are inputed correctly
                        #customer data count
                        self.customer_data['date_first_registered'] = self.customer_data['date_first_registered'].dt.normalize()
                        customer_count = int(self.customer_data[['date_first_registered']][(self.customer_data['date_first_registered'] >= d1) & (self.customer_data['date_first_registered'] <= d2)].count())
                        customer_text.set("Total number of customer missing are: "+str(customer_count))
                        #obtaining customer missing customer list
                        customer_list = self.customer_data[['customer_id']][(self.customer_data['date_first_registered'] >= d1) & (self.customer_data['date_first_registered'] <= d2)].values.tolist()
                        new_customer_list = []
                        def flattenlist(customer_list):
                            """This funtion will flatten the list from list for list to list"""
                            for i in customer_list:
                                if type(i) == list:
                                    flattenlist(i)
                                else:
                                    new_customer_list.append(i)
                        flattenlist(customer_list)
                        #counting the records missing
                        self.record_data['record_id'] = self.record_data['customer_id'].apply(lambda x: 'True' if x in new_customer_list else 'False') #this is fetching the missing records
                        record_list = self.record_data.record_id.value_counts().tolist() # output is a series so converting into a list
                        if len(record_list) == 2:
                            record_text.set('Total number of Records missing are: '+str(record_list[1])) #printing the second element of the list since the second element denotes the true values
                        else:
                            record_text.set('Total number of Records missing are: '+'0')
                        #counting schemes missing
                        self.scheme_data['customer_contact_lens_scheme_id'] = self.scheme_data['customer_id'].apply(lambda x: 'True' if x in new_customer_list else 'False')
                        scheme_list = self.scheme_data.customer_contact_lens_scheme_id.value_counts().tolist()
                        if len(scheme_list) == 2:
                            scheme_text.set('Total number of scheme missing are: '+str(scheme_list[1]))
                        else:
                            scheme_text.set('Total number of scheme missing are: '+'0')
                        #counting the sales header missing
                        self.salesHeader_data['sales_header_id'] = self.salesHeader_data['customer_id'].apply(lambda x: 'True' if x in new_customer_list else 'False')
                        sales_headerlist = self.salesHeader_data.sales_header_id.value_counts().tolist()
                        if len(sales_headerlist) == 2:
                            salesheader_text.set("Total number of sales header missing are: "+str(sales_headerlist[1]))
                        else:
                            salesheader_text.set("Total number of sales header missing are: "+'0')
                        #counting the clinical dispense order missing
                        self.ClinicalDispense_data['clinical_dispense_order_id'] = self.ClinicalDispense_data['customer_id'].apply(lambda x: 'True' if x in new_customer_list else 'False')
                        ClinicalDispense_list = self.ClinicalDispense_data.clinical_dispense_order_id.value_counts().tolist()
                        if len(ClinicalDispense_list) == 2:
                            clinicaldispense_text.set("Total number of clinical dispense order missing are: "+str(ClinicalDispense_list[1]))
                        else:
                            clinicaldispense_text.set("Total number of clinical dispense order missing are: "+'0')
                        #Dispense item count
                        dispense_item_count = int(self.DispenseItem_data[['collection_date']][(self.DispenseItem_data['collection_date'] >= d1) & (self.DispenseItem_data['collection_date'] <= d2)].count())
                        dispense_item_text.set("Total number of dispense item missing are: "+str(dispense_item_count))
                        #NHS Voucher count
                        self.NHSVoucer_data['test_date'] = pd.to_datetime(self.NHSVoucer_data['test_date'])
                        nhs_coucher_count = int(self.NHSVoucer_data[['test_date']][(self.NHSVoucer_data['test_date'] >= d1) & (self.NHSVoucer_data['test_date'] <= d2)].count())
                        nhsvoucher_text.set("Total number of NHS voucher missing are: "+str(nhs_coucher_count))
                        #sales_detail
                        d1 = datetime.datetime.date(d1)
                        d2 = datetime.datetime.date(d2)
                        sales_detail_query = "select count(*) from sales_detail where sales_header_id in (select sales_header_id from sales_header where customer_id in (select customer_id from customer where date_first_registered >= '{d1}' and date_first_registered <= '{d2}'))".format(d1=d1,d2=d2)
                        salesDetail_data = pd.read_sql_query(sales_detail_query,self.engine)
                        sales_detail_text.set("Total number of sales detail record missing are: "+str(int(salesDetail_data.values)))
                    except ValueError:
                        messagebox.showinfo("Error","Incorrect date format should be YYYY-MM-DD")
                processButton = Button(commandwindow,text="Start Analysis",command=HighLevelAnalysis).grid(row=0,column=4)
            else:
                messagebox.showinfo("error","Invalid credentials")
        loginButton = Button(mainwindow,text='Login',command=login).grid(row=2,column=0)
        mainwindow.mainloop()




d = dataRecovery()
d.userInterface()




"""
Mapping
customer --> dates
record --> customer_id
customer_contact_lens_scheme --> customer_id
sales_header --> customer_id
sales_detail --> sales_header_id
sales_payment --> sales_header_id
clinical_dispense_order --> customer_id
dispense_item --> dates
nhsvoucher --> date

"""
