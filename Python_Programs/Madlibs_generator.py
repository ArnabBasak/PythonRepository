"""
3. Mad Libs Generator

The Goal: Inspired by Summer Son’s Mad Libs project with Javascript.
The program will first prompt the user for a series of inputs a la Mad Libs.
For example, a singular noun, an adjective, etc. Then, once all the information
has been inputted, the program will take that data and place them into a premade
story template. You’ll need prompts for user input, and to then print out the full story at the end with the input included.
Concepts to keep in mind:

Strings
Variables
Concatenation
Print

A pretty fun beginning project that gets you thinking about how to manipulate userinputted data.
Compared to the prior projects, this project focuses far more on strings and concatenating.
Have some fun coming up with some wacky stories for this!

"""

class Madlibs:
    def __init__(self):
        pass
    def userInput(self):
        self.name = input("Enter a name of a person ")
        self.place = input("Enter the name of a place")
        self.animal = input("enter the name of an animal")
        self.thing = input("enter the name of random thing")
        self.verb = input("enter an action word that is verb")
        self.adverb = input("enter an adverb")
        self.adjective = input("enter and adjective")
    def display(self):
        print()
        print("Hello {0}".format(self.name))
        print("good to see you, how are you?,when did you came to {0},".format(self.place))
        print("how is your pet {0},".format(self.animal))
        print("what is the status of you buying a {0}".format(self.thing))
        print("Do you {0} to office".format(self.verb))
        print("Anyway {0} is good for health".format(self.adverb))
        print("ofcourse you are a {0} person".format(self.adjective))


ML = Madlibs()
ML.userInput()
ML.display()
