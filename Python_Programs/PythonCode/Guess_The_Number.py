"""
2. Guess the Number

The Goal: Similar to the first project, this project also uses the random module in Python.
The program will first randomly generate a number unknown to the user. The user needs to guess what that number is.
(In other words, the user needs to be able to input information.) If the user’s guess is wrong,
the program should return some sort of indication as to how wrong (e.g. The number is too high or too low).
If the user guesses correctly, a positive indication should appear.
You’ll need functions to check if the user input is an actual number,
to see the difference between the inputted number and the randomly generated numbers, and to then compare the numbers.
Concepts to keep in mind:

Random function
Variables
Integers
Input/Output
Print
While loops
If/Else statements

"""
import random
class NumberGuess:
    def __init__(self):
        self.score = 0
    def userInput(self):
        self.userinput = int(input('enter any number'))
        if self.userinput not in range(1,99999):
            print('sorry your inputed number is too large')
            self.userInput()
    def gamePlay(self):
        self.randomNumber = random.randrange(1,99999)
        if self.userInput == self.randomNumber:
            self.score += 1
            print("congratulation you won your score is",self.score)
            self.userchoice = int(input('press 1 to play again'))
            if self.userchoice == 1:
                self.userInput()
                self.gamePlay()
            else:
                print('Your final score is',self.score)
        elif self.userInput != self.randomNumber:
            self.score -= 1
            if self.randomNumber < self.userinput:
                print('Opps sorry you missed by',self.userInput - self.randomNumber,'as computer guessed',self.randomNumber)
                self.userchoice = int(input('press 1 to play again'))
                if self.userchoice == 1:
                    self.userInput()
                    self.gamePlay()
                else:
                    print('Your final score is',self.score)
            else:
                print('Opps sorry you missed by',self.randomNumber - self.userinput,'as computer guessed',self.randomNumber)
                self.userchoice = int(input('press 1 to play again'))
                if self.userchoice == 1:
                    self.userInput()
                    self.gamePlay()
                else:
                    print('Your final score is',self.score)

NG = NumberGuess()
NG.userInput()
NG.gamePlay()
