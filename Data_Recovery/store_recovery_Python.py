import datetime
import pymysql
import pandas as pd
class recovery():
    def __init__(self):
        self.fromdate = ''
        self.todate = ''
        self.d1 = ''
        self.d2 = ''
        self.db = ''
        self.diff = 0
        self.dumpsCustomerDf = pd.DataFrame()
        self.dumpsCustomerDf = self.dumpsCustomerDf.fillna(0)
        self.liveCustomerDf = pd.DataFrame()
        self.liveCustomerDf = self.liveCustomerDf.fillna(0)
    def inputDate(self):
        self.fromdate = input('enter the date from YYYY-MM--DD format when the data is missing')
        self.todate = input('enter the date till YYYY-MM--DD format when the data is missing')
        try:
            self.d1 = datetime.datetime.strptime(self.fromdate, "%Y-%m-%d")
            self.d2 = datetime.datetime.strptime(self.todate, "%Y-%m-%d")
            print("d1,d2 is equal to: ",self.d1,self.d2)
            self.diff = abs((self.d2 - self.d1).days)
        except ValueError:
            print(ValueError("Incorrect data format, should be YYYY-MM-DD"))
        print('data was missing from',self.fromdate)
        print('data was missing till',self.todate)
        print('total number of days the data lost',self.diff)
    def connectDb(self):
         try:
             self.db = pymysql.connect(host="localhost",user="root",passwd="library",db="soa")
         except Exception:
             print("Error in MySQL connection")
    def HighlevelFile(self):
        pass
    def countCustomer(self):
         self.connectDb()
         if self.d1 != '' and self.d2 != '':
            try:
                 self.cur = self.db.cursor()
                 self.cur.execute("SELECT count(*) FROM customer WHERE date_first_registered LIKE %s", ("%" + str(self.d1).strip("00:00:00") + "%",))
                 self.result = self.cur.fetchone()
                 print("the total number of customer is missing are:",self.result[0])
            except Exception:
                 print(Exception)
         else:
                 print('To date and from date is invalid')
    def countRecord(self):
         self.connectDb()
         if self.d1 != '' and self.d2 != '':
             try:
                 self.cur = self.db.cursor()
                 self.cur.execute("select count(*) From record where customer_arrival_time LIKE %s",("%" + str(self.d1).strip("00:00:00")+ "%",))
                 self.result = self.cur.fetchall()
                 print("The total number of records missing are:",self.result[0])
             except Exception:
                 print(Exception)
         else:
             print('To date and from date is invalid')
    def countSchemes(self):
         self.connectDb()
         if self.d1 != '' and self.d2 != '':
             try:
                 self.cur = self.db.cursor()
                 self.cur.execute("select count(*) from customer_contact_lens_scheme where scheme_state_date LIKE %s",("%" + str(self.d1).strip("00:00:00")+ "%",))
                 self.result = self.cur.fetchall()
                 print("The total number of schemes missing are: ",self.result[0])
             except Exception:
                 print(Exception)
         else:
             print('To date and from date is invalid')
    def countSalesHeader(self):
         self.connectDb()
         if self.d1 != '' and self.d2 != '':
             try:
                 self.cur = self.db.cursor()
                 self.cur.execute("select count(*) from sales_header where sale_date LIKE %s",("%" + str(self.d1).strip("00:00:00")+ "%",))
                 self.result = self.cur.fetchall()
                 print("The total number of sales_header missing are: ",self.result[0])
             except Exception:
                 print(Exception)
         else:
             print('To date and from date is invalid')
    def countSalesDetail(self):
         self.connectDb()
         if self.d1 != '' and self.d2 != '':
             try:
                 self.cur = self.db.cursor()
                 self.cur.execute("select count(*) from sales_detail where sales_header_id in (select sales_header_id from sales_header where sale_date LIKE %s",("%" + str(self.d1).strip("00:00:00")+ "%",))
                 self.result = self.cur.fetchall()
                 print("The total number of sales_header missing are: ",self.result[0])
             except Exception:
                 print(Exception)
         else:
             print('To date and from date is invalid')
    def countSalesPayment(self):
         self.connectDb()
         if self.d1 != '' and self.d2 != '':
             try:
                 self.cur = self.db.cursor()
                 self.cur.execute("select count(*) from sales_payment where sales_header_id in (select sales_header_id from sales_header where sale_date LIKE %s",("%" + str(self.d1).strip("00:00:00")+ "%",))
                 self.result = self.cur.fetchall()
                 print("The total number of sales_payment missing are: ",self.result[0])
             except Exception:
                 print(Exception)
         else:
             print('To date and from date is invalid')
    def countOdersModified(self):
        self.connectDb()
        if self.d1 != '' and self.d2 != '':
            try:
                self.cur = self.db.cursor()
                self.cur.execute("select count(*) from clinical_dispense_order where order_date LIKE %s",("%" + str(self.d1).strip("00:00:00")+ "%",))
                self.result = self.cur.fetchall()
                print("The total number of clinical_dispense_order updated are: ",self.result[0])
            except Exception:
                print(Exception)
        else:
            print('To date and from date is invalid')
    def countDispenseItem(self):
        self.connectDb()
        if self.d1 != '' and self.d2 != '':
            try:
                self.cur = self.db.cursor()
                self.cur.execute("select count(*) from dispense_item where clinical_dispense_order_id in (select clinical_dispense_order_id from clinical_dispense_order where order_date LIKE %s",("%" + str(self.d1).strip("00:00:00")+ "%",))
                self.result = self.cur.fetchall()
                print("The total number of dispense item missing are: ",self.result[0])
            except Exception:
                print(Exception)
        else:
            print('To date and from date is invalid')
    def countDispenseItemUpdated(self):
        self.connectDb()
        if self.d1 != '' and self.d2 != '':
            try:
                self.cur = self.db.cursor()
                self.cur.execute("select count(*) from dispense_item where collected_date like %s",("%" + str(self.d1).strip("00:00:00")+ "%",))
                self.result = self.cur.fetchall()
                print("The total number of dispense item updated are: ",self.result[0])
            except Exception:
                print(Exception)
        else:
            print('To date and from date is invalid')
    def countDispenseRx(self):
        self.connectDb()
        if self.d1 != '' and self.d2 != '':
            try:
                self.cur = self.db.cursor()
                self.cur.execute("select count(d.*) from dispense_rx d, dispense_item di, clinical_dispense_order c where d.dispense_rx_id=di.dispense_item_id and di.clinical_dispense_order_id=c.clinical_dispense_order_id and c.order_date LIKE %s",("%" + str(self.d1).strip("00:00:00")+ "%",))
                self.result = self.cur.fetchall()
                print("The total number of dispense rx missing are: ",self.result[0])
            except Exception:
                print(Exception)
        else:
            print('To date and from date is invalid')
    def countNhsVoucher(self):
        self.connectDb()
        if self.d1 != '' and self.d2 != '':
            try:
                self.cur = self.db.cursor()
                self.cur.execute("select count(*) from nhsvoucher where nhs_voucher_id in (select nhs_voucher_id from sight_test where tr_number in (select record_id from record where customer_arrival_time LIKE %s",("%" + str(self.d1).strip("00:00:00")+ "%",))
                self.result = self.cur.fetchall()
                print("The total number of NHS voucher missing are: ",self.result[0])
            except Exception:
                print(Exception)
        else:
            print('To date and from date is invalid')

    def searchCustomerinDumps(self):
             self.connectDb()
             if self.d1 != '' and self.d2 != '':
                 #try:
                     cur = self.db.cursor()
                     #self.cur.execute("select n.first_name,n.last_name,c.date_of_birth, d.doctor_id from customer c inner join name n on n.name_id = c.name_id left outer join doctor d on d.doctor_id = c.doctor_id where c.date_first_registered LIKE  %s", ("%" + str(self.d1).strip("00:00:00") + "%",))
                     self.cur.execute("SELECT count(*) FROM customer WHERE date_first_registered LIKE %s", ("%" + str(self.d1).strip("00:00:00") + "%",))
                     self.result = self.cur.fetchall()
                     self.result = pd.DataFrame()
                     print(self.result)
                 #except Exception:
                    # print(Exception)
             else:
                     print('To date and from date is invalid')



 #      HIGH LEVEL ANALYSIS     #
a = recovery()
a.inputDate()
a.countCustomer()
a.countRecord()
a.countSchemes()
a.countOdersModified()
a.countDispenseItem()
a.countDispenseItemUpdated()
a.countDispenseRx()
a.countNhsVoucher()
a.searchCustomerinDumps()

def searchCustomerinlive(self):
        self.connectDb()
        if self.d1 != '' and self.d2 != '':
            try:
                cur = db.cursor()
                self.liveCustomerDf = pd.read_sql_query("select n.first_name,n.last_name,c.date_of_birth, d.doctor_id from customer c inner join name n on n.name_id = c.name_id left outer join doctor d on d.doctor_id = c.doctor_id where c.date_first_registered >=  %s", ("%" + str(self.d1).strip("00:00:00") + "%",))
                #result = cur.fetchall()
                #print(result)
            except Exception:
                print("Error with query: " + query)
        else:
            print('To date and from date is invalid')


def compareCustomer():
     dumpcustomer = open('dumpcus.txt','r')
     livecustomer = open('livecus.txt','r')
     same = set(dumpcustomer).intersection(livecustomer)
     same.discard('\n')
     file_out = ('output_file.txt','w')
     for line in same:
         file_out.write(line)
def checkSchemes():
     connectDb()
     if fromdate != '' and todate != '':
         try:
             cur = db.cursor()
             query = """select * from customer_contact_lens_scheme where customer_id in (select customer_id from customer where date_first_registered >= '%s' and date_first_registered <= '%s') order by customer_id;""" %d1,d2
             cur.execute(query)
             result = cur.fetchall()
             print(result)
         except Exception:
             print("Error with query: " + query)
     else:
         print('To date and from date is invalid')
