"""
1. Dice Rolling Simulator

The Goal: Like the title suggests, this project involves writing a program that simulates rolling dice. When the program runs, it will randomly choose a number between 1 and 6. (Or whatever other integer you prefer — the number of sides on the die is up to you.) The program will print what that number is. It should then ask you if you’d like to roll again. For this project, you’ll need to set the min and max number that your dice can produce. For the average die, that means a minimum of 1 and a maximum of 6. You’ll also want a function that randomly grabs a number within that range and prints it.
Concepts to keep in mind:

Random
Integer
Print
While Loops

"""
import random
class Simulator:
    def __init__(self):
        """This is the init funtion where it will only set the score variable"""
        self.playerScore = 0
    def getInput(self):
        """This funtion will take the input from the user and intimate it if its fine or not"""
        self.userchoice = int(input('enter any number between 1 and 6'))
        if self.userchoice not in range(1,6):
            print("the entereted number is not in range please enter again")
            self.getInput()
    def gamePlay(self):
        """This is the funtion where it will compare with the userchoice and the system choice"""
        self.randomNumber = random.randrange(1,6)
        if self.randomNumber == self.userchoice:
            self.playerScore += 1
            print("congratulation you won your score is: ",self.playerScore)
        else:
            print("Sorry you lost press 1 to play again")
            self.userchoice = int(input())
            if self.userchoice == 1:
                self.getInput()
                self.gamePlay()
            else:
                print("THANK YOU")
                print("your final score is",self.playerScore)



s = Simulator()
s.getInput()
s.gamePlay()
