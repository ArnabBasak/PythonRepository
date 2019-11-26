import datetime
import pymysql
class recovery():
    def __init__(self):
        self.fromdate = ''
        self.todate = ''
        self.d1 = ''
        self.d2 = ''
        self.db = ''
        self.diff = 0
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
         print(self.d1)
         print(self.d2)
         if self.d1 != '' and self.d2 != '':
            try:
                 self.cur = self.db.cursor()
                 self.cur.execute("SELECT count(*) FROM customer WHERE date_first_registered LIKE %s", ("%" + str(self.d1).strip("00:00:00") + "%",))
                 self.result = self.cur.fetchone()
                 print(self.result[0])
            except Exception:
                 print(Exception)
         else:
                 print('To date and from date is invalid')

a = recovery()
a.inputDate()
a.countCustomer()

def searchCustomerinDumps():
         connectDb()
         if fromdate != '' and todate != '':
             try:
                 cur = db.cursor()
                 query = """select n.first_name,n.last_name,c.date_of_birth, d.doctor_id from customer c inner join name n on n.name_id = c.name_id left outer join doctor d on d.doctor_id = c.doctor_id where c.date_first_registered >= '%s' and c.date_first_registered <= '%s'""" %d1,d2
                 cur.execute(query)
                 result = cur.fetchall()
                 print(result)
             except Exception:
                 print("Error with query: " + query)
         else:
             print('To date and from date is invalid')

def searchCustomerinlive():
         try:
             db = pymysql.connect(host="localhost",user="root",passwd="library",db="soa")
         except Exception:
             print("Error in MySQL connection")
         if fromdate != '' and todate != '':
             try:
                 cur = db.cursor()
                 query = """select n.first_name,n.last_name,c.date_of_birth, d.doctor_id from customer c inner join name n on n.name_id = c.name_id left outer join doctor d on d.doctor_id = c.doctor_id where c.date_first_registered >= '%s' and c.date_first_registered <= '%s'""" %d1,d2
                 cur.execute(query)
                 result = cur.fetchall()
                 print(result)
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

def countRecord():
     connectDb()
     if fromdate != '' and todate != '':
         try:
             cur = db.cursor()
             query = """select count(*) from record where cast(customer_arrival_time as date) >= '%s' and cast(customer_arrival_time as date) <= '%s'""" %d1,d2
             cur.execute(query)
             result = cur.fetchall()
             print(result)
         except Exception:
             print("Error with query: " + query)
     else:
         print('To date and from date is invalid')
def countSchemes():
     connectDb()
     if fromdate != '' and todate != '':
         try:
             cur = db.cursor()
             query = """select count(*) from customer_contact_lens_scheme where cast(scheme_state_date as date) >= '%s' order by customer_contact_lens_scheme_id;""" %d1
             cur.execute(query)
             result = cur.fetchall()
             print(result)
         except Exception:
             print("Error with query: " + query)
     else:
         print('To date and from date is invalid')

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
