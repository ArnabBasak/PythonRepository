class Addition:
    def getdata(self):
        self.num1 = int(input('enter number 1 '))
        self.num2 = int(input('enter number 2'))
    def calulcate(self):
        self.num3 = self.num1+self.num2
    def display(self):
           print('addition is',self.num3)

class Substration:
    def getdata(self):
        self.num1 = int(input('enter number 1 '))
        self.num2 = int(input('enter number 2'))
    def calulcate(self):
        self.num3 = self.num1 - self.num2
    def display(self):
           print('substraction is',self.num3)

class multiplication:
    def getdata(self):
        self.num1 = int(input('enter number 1 '))
        self.num2 = int(input('enter number 2'))
    def calulcate(self):
        self.num3 = self.num1 * self.num2
    def display(self):
           print('multiplication  is',self.num3)

class division:
    def getdata(self):
        self.num1 = float(input('enter number 1 '))
        self.num2 = float(input('enter number 2'))
    def calulcate(self):
        self.num3 = self.num1/self.num2
    def display(self):
           print('division is',self.num3)



