import pymysql
import csv
import os
#employees database connection
conn_employees =  pymysql.connect(host = "localhost",user = "root",password = "library",db = "employees") # database connection for employees

#for table employees in employees database
cur_employees = conn_employees.cursor() # cursor for employees table in employees database
cur_employees.execute("select * from employees")
result_employees = cur_employees.fetchall()
employees_employees = csv.writer(open('C:/Users/arnab.jaydeb.basak/Documents/programs/pythonprograms/employees_employees.csv','w',encoding = 'utf-8'))
columnnames = [desc[0] for desc in cur_employees.description]
employees_employees.writerow(columnnames)
employees_employees.writerows(result_employees)
#print('employees tables data has been written in employees_employees.csv file')
conn_employees.close()

#emp database connection
conn_emp = pymysql.connect(host = "localhost",user = "root",password = "library",db = "emp") 
#for table employees in emp database
cur_employees = conn_emp.cursor() # cursor for employees table in emp database
cur_employees.execute("select * from employees")
result_employees = cur_employees.fetchall()
emp_employees = csv.writer(open('C:/Users/arnab.jaydeb.basak/Documents/programs/pythonprograms/emp_employees.csv','w',encoding = 'utf-8'))
columnnames = [desc[0] for desc in cur_employees.description]
emp_employees.writerow(columnnames)
emp_employees.writerows(result_employees)
#print('employees tables data has been written in emp_employees.csv file')
conn_emp.close()

#employee database connection
conn_employee = pymysql.connect(host = "localhost",user = "root",password = "library",db = "employee") 
#for table employees in employee database
cur_employees = conn_employee.cursor() # cursor for employees table in employee database
cur_employees.execute("select * from employees")
result_employees = cur_employees.fetchall()
employee_employees = csv.writer(open('C:/Users/arnab.jaydeb.basak/Documents/programs/pythonprograms/employee_employees.csv','w',encoding = 'utf-8'))
columnnames = [desc[0] for desc in cur_employees.description]
employee_employees.writerow(columnnames)
employee_employees.writerows(result_employees)
#print('employees tables data has been written in empployee_employees.csv file')
conn_employee.close()

def  CsvDifference():
    "This a CSV difference function"
    file1 = open('C:/Users/arnab.jaydeb.basak/Documents/programs/pythonprograms/employees_employees.csv', 'r')
    file2 = open('C:/Users/arnab.jaydeb.basak/Documents/programs/pythonprograms/emp_employees.csv', 'r')
    file3 = open('C:/Users/arnab.jaydeb.basak/Documents/programs/pythonprograms/employee_employees.csv','r')
    fileone = file1.readlines()
    filetwo = file2.readlines()
    filethree = file3.readlines()
    with open('C:/Users/arnab.jaydeb.basak/Documents/programs/pythonprograms/updated_EmployeesDiff.csv', 'w') as outFile:
        for line in fileone:
            if line not in filetwo or line not in filethree:
                #print(line)
                outFile.write(line)
        #print('difference file has been created')
            else:
                print('There is no difference in the csv file')
                break

CsvDifference()

def CsvLenCompare():
    "This is a CSV export"
    employee_employeesFile = open("C:/Users/arnab.jaydeb.basak/Documents/programs/pythonprograms/employee_employees.csv")
    emp_employeesFile = open("C:/Users/arnab.jaydeb.basak/Documents/programs/pythonprograms/emp_employees.csv")
    employees_employeesFile = open("C:/Users/arnab.jaydeb.basak/Documents/programs/pythonprograms/employees_employees.csv")

    employee_employeesFilelen = len(employee_employeesFile.readlines())
    emp_employeesFilelen = len(emp_employeesFile.readlines())
    employees_employeesFilelen = len(employees_employeesFile.readlines())
    
    #comparing for the employees database
    if employees_employeesFilelen >= employee_employeesFilelen and employees_employeesFilelen >= emp_employeesFilelen:
        print("There is data in the employees table in the employees database if something is missing it cannot be restored from other database")
    else:
        print("data missing in the employees table in the employees database restoring it using updated_EmployeesDiff csv file")
        

    #comparing for the emp database
    if  emp_employeesFilelen >= employee_employeesFilelen and emp_employeeFilelen >= employees_employeesFilelen:
        print("data in the employees table of emp database is present if something is missing it connot be restored from other databases")
    else:
        print("data missing in the employees table in the emp database restoring  it using updated_EmployeesDiff csv file")
        conn_emp =  pymysql.connect(host = "localhost",user = "root",password = "library",db = "emp") # database connection for employees
        cursor = conn_emp.cursor()
        csv_data = csv.reader(open('C:/Users/arnab.jaydeb.basak/Documents/programs/pythonprograms/updated_EmployeesDiff.csv','r'))
        for row in csv_data:
            cursor.execute('INSERT INTO employees(emp_no,birth_date,first_name,last_name,gender,hire_date)''VALUES(%s","%s","%s","%s","%s","%s")')
        conn_emp.commit()    
        conn_emp.close()
        print('data has been restored please check from backend')

    #comparing for the employee database
    if employee_employeesFilelen >= emp_employeesFilelen and employee_employeesFilelen >= employees_employeesFilelen:
        print("data in the employees table of employee database is present if something is missing it canoot be restored from other databases")
    else:
        print("data is missing in the employees table of the employee database restoring it using updated_EmployeesDiff csv file")
    
    

CsvLenCompare()
    
