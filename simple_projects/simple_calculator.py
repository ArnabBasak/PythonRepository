class calculator:
    def simple_calculator(self):
        num1 = int(input('enter num1'))
        num2 = int(input('enter num2'))
        print(f'Addition of {num1} and {num2} is',num1 + num2)
        print(f'Substraction of {num1} and {num2} is',num1 - num2)
        print(f'Multiplication of {num1} and {num2} is',num1 * num2)
        print(f'Division of {num1} and {num2} is',num1 / num2)
        print(f'Modulus of {num1} and {num2} is',num1 % num2)
        print(f'Floor division of {num1} and {num2} is',num1 // num2)
    def simple_interest(self):
        """SIMPLE INTEREST"""
        p = float(input('enter the Principle amount'))
        n = float(input('enter the time duration in months'))
        r = float(input('enter the rate of interest'))
        if r == 0.0 or n == 0:
            a = float(input('You have not entered the rate of interest please enter the amount you have to pay to calculate the rate of interest'))
            r = ((p*n)/(100.0*a))
            print(f'The rate of interest for the amount {a} after {n} months is: ',r)
        else:
            a = ((p*n*r)/100)
            print(f'The total amount you have to pay after {n} months is {a+p}')
#c = calculator()
#c.simple_calculator()
#c.simple_interest()

class Calculate_area:
    def __init__(self):
        self.length = 0.0
        self.radius = 0.0
        self.breadth = 0.0
        self.height = 0.0
        self.userinput = 0
        self.area = 0.0
        self.side = 0.0
    def areaofcircle(self):
        self.radius = float(input('Enter the radius of the circle'))
        self.area =  3.14*self.radius**2
        print(f'The area of the circle is{self.area}')
    def circumferenceofcircle(self):
        self.radius = float(input('Enter the radius of the circle'))
        self.area = 2*3.14*self.radius
    def areaofrectangle(self):
        self.length = float(input('Enter the length of the rectangle'))
        self.breadth = float(input('Enter the breadth of the rectangle'))
        self.area = self.length * self.breadth
        print(f'area of rectangle is {self.area}')
    def areaoftriangle(self):
        self.length = float(input('Enter the length of the triangle'))
        self.breadth = float(input('Enter the breadth of the triangle'))
        self.height = float(input('Enter the height of the triangle'))
        self.area = self.length * self.breadth * self.height
        print(f'area of triangle is {self.area}')
    def areaofsquare(self):
        self.side = float(input('Enter the side of the square'))
        self.area = self.side ** 2
        print(f'area of square is{self.area}')
    def dataInput(self):
        print('-------PRESS 1 FOR AREA OF CIRCLE-------\n')
        print('-------PRESS 2 FOR CRICUMFERENCE OF CRICLE-------\n')
        print('-------PRESS 2 FOR AREA OF RECTANGLE-------\n')
        print('-------PRESS 3 FOR AREA OF TRIANGLE-------\n')
        print('-------PRESS 4 FOR AREA OF SQUARE-------\n')
        self.userinput = int(input('ENTER YOUR OPTION FROM THE ABOVE MENU'))
        if self.userinput == 1:
            self.areaofcircle()
        elif self.userinput == 2:
            self.circumferenceofcircle()
        elif self.userinput == 3:
            self.areaofrectangle()
        elif self.userinput == 4:
            self.areaoftriangle()
        elif self.userinput == 5:
            self.areaofsquare()
        else:
            print('Please select a valid option')
#cal = Calculate_area()
#cal.dataInput()


class Pythongorus:
    def __init__(self):
        self.one_side = 0.0
        self.other_side = 0.0
        self.hyp = 0.0
        self.area = 0.0
    def checkifrightangletriangle(self):
        self.area = (self.one_side ** 2) + (self.other_side ** 2)
        if self.area ** 2 == self.hyp ** 2:
            print('The triangle is right angle triangle')
        else:
            print('The triangle is not a right angle triangle')
    def userinput(self):
        self.one_side = float(input('Enter the values for 1st side'))
        self.other_side = float(input('Enter the values for 2nd side'))
        self.checkifrightangletriangle()

p = Pythongorus()
p.userinput()
