"""
THIS IS THE PROGRAMS TO PRACTICE ON THE LIST DATA TYPE
"""


import random
class listOperation:
    def __init__(self):
        self.lower_range = random.randint(1,50)
        self.higher_range = random.randint(51,100)
        self.practice_list = list(range(self.lower_range,self.higher_range))
    """
    1. SUM OF ALL THE ELEMENTS IN THE LIST
    """
    def SumOfAllElements(self):
        print(f'sum of all elements in the lists are {sum(self.practice_list)}')
    """
    2. multiples OF ALL THE ELEMENTS IN THE LIST
    """
    def multiplesofallElements(self):
        pass


l = listOperation()
l.SumOfAllElements()
 
