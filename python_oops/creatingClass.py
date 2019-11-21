class Employee:
    num_of_emps = 0
    raise_amount = 1.04
    def __init__(self,firstname,lastname,pay):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.email = firstname + '.' + lastname + '@compamy.com'
        """since this should be constant for all the instence 
        of the class that's why there is no self"""
        Employee.num_of_emps+=1 
    def fullname(self):
        return '{} {}'.format(self.firstname,self.lastname)
    def apply_raise(self):
        #self.raise_amount is used since this has be to manupulated by the instence
        self.pay = int(self.pay * self.raise_amount)

employee1 =  Employee('arnab','basak',50000)
employee2 =  Employee('test','testing',60000)
#print(employee1.firstname,employee1.lastname,employee1.email,employee1.pay) 
#checking the scope of the instence of all
#print(employee1.__dict__)
#checking the scrope of the class
#print(Employee.__dict__)
employee1.raise_amount = 1.05
#print(employee1.__dict__)
employee1.apply_raise()
print(employee1.pay)
#calling using direct class name
#print(Employee.fullname(employee1))