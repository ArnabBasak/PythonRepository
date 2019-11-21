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
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount = amount
    @classmethod
    def from_string(cls,emp_str):
        first,last,pay = emp_str.split('-')
        return cls(first,last,pay)

employee1 =  Employee('arnab','basak',50000)
employee2 =  Employee('test','testing',60000)
