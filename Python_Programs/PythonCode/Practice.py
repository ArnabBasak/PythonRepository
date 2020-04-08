import datetime

import math

import sys

import calendar

class Excerise:

    #Excerise 1

    def Display(self):

        """This funtion will create a poem twinkle twinkle little star"""

        print('Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are')

    #Excerise 2

    def version_check(self):

        """This funtion will return the python version running in the system"""

        print("The current Python version is: \n",sys.version_info)

    #Excerise 3

    def current_datetime(self):

        """This funtion will return the current date and time"""

        print("The current date and time is: ",datetime.datetime.now())

    #Excerise 4

    def area_of_circle(self):

        """This funtion will calculate the area of circle and radius of the circle"""

        self.choice = int(input('enter 1 if you know the radius else press 2'))

        if self.choice == 1:

            self.radius = int(input('enter the radius of the circle'))

            print('area of the circle is: ',3.14*self.radius*self.radius)

        elif self.choice == 2:

            self.area = int(input('enter the area of the circle'))

            print('The radius of the circle is:',math.sqrt(self.area/3.14))

        else:

            print("invalid choice")

    #Excerise 5

    def reverse_name(self):

        """This funtion will reverse the inputed first name and last name"""

        self.first_name = input('enter your first name')

        self.last_name = input('enter your last name')

        print(self.first_name[::-1],'',self.last_name[::-1])

    #Excerise 6

    def usercreated_list_tupple(self):

        """This funtion will take input from user in the form of list and convert it into tupple"""

        self.values = input('enter number in a comman seperated manner')

        print("Entered values in a list: ",self.values.split(","))

        print("Entered values in a tupple: ",tuple(self.values.split(",")))

    #Excerise 7

    def color_list(self):

        """This funtion will give the first color present in the list and  the last color present in the list"""

        self.color_list = ["Red","Green","White","Black"]

        print("First color in the list: ",self.color_list[0],"","Last color in the list: ",self.color_list[-1])

    #Excerise 8

    def  compute_value_of_n(self):

        """This funtion will calculate n+nn+nnn where n is a string variable and will return an output in integer"""

        self.n = input("enter the value of n")

        #print("The value of n: ",self.n," ","The value of nn",self.n*self.n," ","The value of nnn",self.n*self.n*self.n)

        #print("The value of n+nn+nnn",(self.n)+(self.n*self.n)+(self.n*self.n*self.n))

        self.n1 = self.n+self.n

        self.n2 = self.n+self.n+self.n

        self.answer = int(self.n) + int(self.n1) + int(self.n2)

        print("The output is: ",self.answer)

    def farm_problem(self):

        """This funtion will calculate the number of animal legs of present in

        each farm in this we will consider chickens have 2 legs cows have 4 legs and pigs have 4 legs"""

        self.number_chicken = int(input('enter the number of chickens you have'))

        self.number_cows = int(input('enter the number of cows you have'))

        self.number_pigs = int(input('enter the number of pigs you have'))

        print('Total number of legs in your farm is: ',(self.number_chicken*2)+(self.number_cows*4)+(self.number_pigs*4))





ex = Excerise()

#ex.Display()

#print()

#ex.version_check()

#print()

#ex.current_datetime()

#print()

#ex.area_of_circle()

#print()

#ex.reverse_name()

#print()

#ex.usercreated_list_tupple()

#print()

#ex.color_list()

#ex.compute_value_of_n()

#print(ex.compute_value_of_n.__doc__)

ex.farm_problem()
